import googlemaps
import csv

# Initialize the Google Maps client with your API key
API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'
gmaps = googlemaps.Client(key=API_KEY)

# Grid_sites list here
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
    # Add more sites as become available: https://www.gridpp.ac.uk/wiki/Main_Page
]

def calculate_distance_matrix(grid_sites):
    """
    Calculates the distance between each pair of grid sites and returns a matrix.
    """
    distance_matrix = []
    site_names = [site["name"] for site in grid_sites]
    
    for origin in grid_sites:
        origin_coords = (origin["latitude"], origin["longitude"])
        row = []
        
        for destination in grid_sites:
            dest_coords = (destination["latitude"], destination["longitude"])
            # API call to get the distance
            result = gmaps.distance_matrix([origin_coords], [dest_coords], mode="driving")
            distance = result['rows'][0]['elements'][0]['distance']['value'] / 1000  # Convert meters to km
            row.append(distance)
        
        distance_matrix.append(row)
        
    return site_names, distance_matrix

def save_distance_matrix_csv(site_names, distance_matrix, filename="distance_matrix.csv"):
    """
    Saves the distance matrix to a CSV file with the provided filename.
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row with site names
        writer.writerow([""] + site_names)
        
        # Write each row with distances
        for i, row in enumerate(distance_matrix):
            writer.writerow([site_names[i]] + row)

# Calculate and save the distance matrix
site_names, distance_matrix = calculate_distance_matrix(grid_sites)
save_distance_matrix_csv(site_names, distance_matrix)

print("Distance matrix saved to distance_matrix.csv")

