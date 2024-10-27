import googlemaps
import subprocess
import json

# Initialize the Google Maps client with your API key
API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'
gmaps = googlemaps.Client(key=API_KEY)

# List grid sites as become available: https://www.gridpp.ac.uk/wiki/Main_Page
grid_sites = [
    {"name": "UKI-LT2-Brunel", "identifier": "LCG.UKI-LT2-Brunel.uk", "latitude": 51.532, "longitude": -0.472}, 
    {"name": "UKI-NORTHGRID-LANCS-HEP", "identifier": "LCG.UKI-NORTHGRID-LANCS-HEP", "latitude": 54.044, "longitude": -2.798},
    {"name": "UKI-NORTHGRID-LIV-HEP", "identifier": "LCG.UKI-NORTHGRID-LIV-HEP.uk", "latitude": 53.406, "longitude": -2.922},
    {"name": "UKI-NORTHGRID-MAN-HEP", "identifier": "LCG.UKI-NORTHGRID-MAN-HEP", "latitude": 53.490, "longitude": -2.241},
    {"name": "UKI-NORTHGRID-SHEF-HEP", "identifier": "LCG.UKI-NORTHGRID-SHEF-HEP", "latitude": 53.382, "longitude": -1.472},
    {"name": "UKI-SCOTGRID-DURHAM", "identifier": "LCG.UKI-SCOTGRID-DURHAM", "latitude": 54.775, "longitude": -1.582},
    {"name": "UKI-SCOTGRID-GLASGOW", "identifier": "LCG.UKI-SCOTGRID-GLASGOW.uk", "latitude": 55.860, "longitude": -4.263},
    {"name": "UKI-SCOTGRID-ECDF", "identifier": "LCG.UKI-SCOTGRID-ECDF.uk", "latitude": 55.952, "longitude": -3.192},
    {"name": "UKI-SOUTHGRID-BRIS", "identifier": "LCG.UKI-SOUTHGRID-BRIS", "latitude": 51.455, "longitude": -2.598},
    {"name": "UKI-SOUTHGRID-RALPP", "identifier": "LCG.UKI-SOUTHGRID-RALPP.uk", "latitude": 51.574, "longitude": -1.314},
    {"name": "UKI-SOUTHGRID-BHAM-HEP", "identifier": "LCG.UKI-SOUTHGRID-BHAM-HEP.uk", "latitude": 52.492, "longitude": -1.888},
    {"name": "UKI-SOUTHGRID-SUSX", "identifier": "LCG.UKI-SOUTHGRID-SUSX", "latitude": 50.927, "longitude": -0.743},
    {"name": "UKI-SOUTHGRID-CAM-HEP", "identifier": "LCG.UKI-SOUTHGRID-CAM-HEP", "latitude": 52.195, "longitude": 0.138},
    {"name": "UKI-SOUTHGRID-OX-HEP", "identifier": "LCG.UKI-SOUTHGRID-OX-HEP", "latitude": 51.753, "longitude": -1.261},
    {"name": "UKI-LT2-IC-HEP", "identifier": "LCG.UKI-LT2-IC-HEP.uk", "latitude": 51.499, "longitude": -0.174},
    {"name": "UKI-LT2-IC-HEP", "identifier": "LCG.UKI-LT2-IC-HEP.uk", "latitude": 51.499, "longitude": -0.174},
    {"name": "UKI-LT2-RHUL", "identifier": "LCG.UKI-LT2-RHUL.uk", "latitude": 51.424, "longitude": -0.566},
    {"name": "UKI-LT2-QMUL", "identifier": "LCG.UKI-LT2-QMUL", "latitude": 51.524, "longitude": -0.040},
    # Add more sites here...
]

# Target number of CPUs
target_cpus = 8 * 2000
search_radius = 20000  # Initial search radius in meters

# Initial site configuration (use the first site as the initial point)
initial_site = grid_sites[0]

# Helper functions
def get_site_info(site_identifier):
    """
    Retrieves site information using the DIRAC command.
    """
    command = ["dirac-admin-site-info", site_identifier]
    result = subprocess.run(command, capture_output=True, text=True)
    try:
        site_info = json.loads(result.stdout.replace("'", '"'))
        return site_info.get("CE", "").split(", ")  # Return list of CEs
    except json.JSONDecodeError:
        print(f"Error decoding site info for {site_identifier}")
        return []

def get_ce_info(ce_host):
    """
    Retrieves the number of CPUs from the CE using the DIRAC command.
    """
    command = ["dirac-admin-ce-info", ce_host]
    result = subprocess.run(command, capture_output=True, text=True)
    try:
        ce_info = json.loads(result.stdout.replace("'", '"'))
        return int(ce_info.get("MaxProcessors", 0))
    except json.JSONDecodeError:
        print(f"Error decoding CE info for {ce_host}")
        return 0

def calculate_distance(origin, destinations):
    """
    Calculate the distance from the origin to multiple destination coordinates.
    """
    origins = [(origin["latitude"], origin["longitude"])]  # Wrap in a list for batch processing
    destinations_coords = [(site["latitude"], site["longitude"]) for site in destinations]
    
    # Call the Distance Matrix API
    result = gmaps.distance_matrix(origins, destinations_coords, mode="driving")
    
    distances = []
    for i, row in enumerate(result['rows'][0]['elements']):
        distance = row['distance']['value']  # distance in meters
        distances.append((destinations[i], distance))
        
    return distances

# Pool resources and create hostfile with distance sorting
def create_hostfile_with_distance(grid_sites, initial_site, target_cpus, search_radius):
    total_cpus = 0
    hostfile_entries = []

    while total_cpus < target_cpus:
        # Calculate distances to each site from the initial site
        distances = calculate_distance(initial_site, grid_sites)
        
        # Sort sites by distance
        sorted_sites = sorted(distances, key=lambda x: x[1])
        
        # Select sites within the search radius
        for site, distance in sorted_sites:
            if distance <= search_radius:
                ces = get_site_info(site["identifier"])
                
                for ce_host in ces:
                    max_processors = get_ce_info(ce_host)
                    
                    if max_processors > 0:
                        hostfile_entries.append(f"{ce_host} slots={max_processors}")
                        total_cpus += max_processors
                        
                        if total_cpus >= target_cpus:
                            break
            if total_cpus >= target_cpus:
                break

        # Expand the search radius if target CPUs not met
        if total_cpus < target_cpus:
            search_radius += 10000

    # Write hostfile entries to a file
    with open("hostfile", "w") as file:
        for entry in hostfile_entries:
            file.write(entry + "\n")
    
    print(f"Hostfile created with total pooled CPUs: {total_cpus}")

# Run the pooling and hostfile creation process with distance sorting
create_hostfile_with_distance(grid_sites, initial_site, target_cpus, search_radius)

