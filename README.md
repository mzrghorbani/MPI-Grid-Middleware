## Prerequisites:

Before proceeding, ensure that you meet the following requirements:

### Certification Authority (CA): 

You must have a certificate from the UK eScience Certification Authority (UKCA) "https://ca.grid-support.ac.uk/". This certificate is essential for accessing grid resources. 

### Grid Virtual Organisation (VO): 

You must be a registered member of a Grid Virtual Organisation, such as GridPP. Membership is required for job submission and resource access.

### Certificate Installation: 

Install your certificate in the $HOME/.globus directory on your local machine. This is necessary for authentication during grid operations.

## Overwriting Middleware Configuration on the Primary Node of the Grid Cluster

The middleware is designed to override the existing configuration files in the existing DIRAC grid middleware.

### Steps to Clone the Repository and Override the Existing Configuration Files

    1. Clone the repository:

        git clone https://github.com/mzrghorbani/MPI-Grid-Middleware.git

    2. Navigate to the repository directory:

        cd MPI-Grid-Middleware

    3. Configuring UKCA by executing .ca:

        chmod .ca && bash .ca

The .ca script is designed to convert UKCA certificates to .pem and initialize the DIRAC proxy with the specified Grid user group.

## If DIRAC is installed on your local machine, skip the following installation section.

### Useful resources:

    https://dirac.readthedocs.io/en/latest/UserGuide/GettingStarted/InstallingClient/index.html

### Install DIRAC:

    wget -np -O dirac-install https://github.com/DIRACGrid/DIRAC/raw/integration/Core/scripts/dirac-instachmod +x dirac-install

### Directory structure:

    drwxr-xr-x 8 mghorbani root 2048 Mar 25 2010 Linux_x86_64_glibc-2.5
    drwxr-xr-x 16 mghorbani root 2048 Oct 12 12:13 DIRAC
    -rwxr-xr-x 1 mghorbani root 21224 Oct 12 13:37 dirac-install
    drwxr-xr-x 2 mghorbani root 10240 Oct 12 17:11 scripts
    -rw-r--r-- 1 mghorbani root 998 Oct 12 17:15 bashrc

### Install VO Client:

    wget -np -O dirac-install http://lhcbproject.web.cern.ch/lhcbproject/dist/Dirac_project/dirac-installchmod +x dirac-install
    dirac-install -V formation
    source bashrc
    dirac-proxy-init
    dirac-configure defaults_formation.cfg

### Configure VO Client:

    dirac-configure -V dirac -S Dirac-Production -C dips://dirac.in2p3.fr:9135/Configuration/Server

### Modify (SOURCE_DIR and TARGET_DIR) in override.sh in MPI-Grid-Middleware:

This script is executed first during job submission to add the middleware to the grid. The source directory (SOURCE_DIR) is the /path/to/MPI-Grid-Middleware and the target directory (TARGET_DIR) is the DIRAC parent directory.

    chmod +x override.sh && bash override.sh

Note: By this point, we have installed DIRAC and integrated all scripts from MPI-Grid-Middleware repository into it.

## Pool GridPP Sites and Available Resources using Google Maps API:

An automation script `pool_sites.py` is designed to initialize the [Google Maps](https://developers.google.com/maps) client using an API key to enable distance calculations.

1. Provide a list of grid sites with their names, identifiers, and geographic coordinates.
2. Set a target_cpus value representing the number of CPUs needed for the simulation tasks.
3. Start from a predefined grid site, setting an initial search_radius to limit the area for each search iteration.
4. Once pooling is complete, save the pooled computing elements information into a hostfile.
5. The hostfile contains availabe CEs with their available CPUs.

Note: Ensure that you have your API_KEY set and DIRAC commands configured for querying grid information.

Optional: Create a distance matrix `distance_matrix.py` for all sites, if required!

## Simple MPI Configuration Test:

A simple MPI test can be executed to ensure all configurations are correct. 

### In MPI-Grid-Middleware directory, run:

    python3 test_MPI.py

This script is designed to return all available CPUs on the local machine.

### If you prefer JDL, you can create a simple MPI job using MPItest.sh:

    Executable = "MPItest.sh";
    Arguments = "";
    StdOutput = "std.out";
    StdError = "std.err";
    OutputSandbox = {"std.out", "std.err"};
    CPUTime = 10;

Check the status of a job:

    dirac-wms-job-status <jobid>

Get the output:

    dirac-wms-job-get-output <jobid>

### For flexibility and simplicity, we recommend using DIRAC Python API. 

The DIRAC API interface looks like this:

    from DIRAC.Interfaces.API.Job import Job
    from DIRAC.Interfaces.API.Dirac import Dirac
    dirac = Dirac()
    j = Job()
    j.setCPUTime(500)
    j.setExecutable('/path/to/MPItest.sh')
    j.setName('MPI Test Job')
    jobID = dirac.submit(j)
    print('Submission Result: ', jobID)

DIRAC Job Monitoring:

    from DIRAC.Interfaces.API.Dirac import Dirac
    from DIRAC.Interfaces.API.Job import Job
    import sys
    dirac = Dirac()
    jobid = sys.argv[1]
    print dirac.status(jobid)

Job Output:

    from DIRAC.Interfaces.API.Dirac import Dirac
    from DIRAC.Interfaces.API.Job import Job
    import sys
    dirac = Dirac()
    jobid = sys.argv[1]
    print dirac.getOutputSandbox(jobid)

## Practical Example:

The following instructions are designed to automate MPI job submission containing 200 simulations. 

### Ensure mpi4py libraries are installed on your local machine. 

If not, please follow the instructions below for Ubuntu 22.04:

    mkdir -p $HOME/opt/openmpi
    cd $HOME/Downloads
    wget https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-4.1.2.tar.gz
    tar -xf openmpi-4.1.2.tar.gz
    cd openmpi-4.1.2
    ./configure --prefix=$HOME/opt/openmpi
    make all && make install

    export CC=$HOME/opt/openmpi/bin/mpicc
    export PATH=$PATH:$HOME/opt/openmpi/bin

    pip install mpi4py

### Set up MPI-Grid-Middleware Environment:

    source /path/to/MPI-Grid-Middleware/.bashrc

The .bashrc script is configured for User "mghorbani" with Brunel University GridPP credentials. Please modify this script with your username and credentials.

### Configure Your Resources:

Edit the config.yml file to specify the number of CPUs, nodes, and CPUs per task.

### Make the Executable Script Executable or use the existing template:

    chmod +x run_simulation.sh

### Submit MPI Jobs:

Please follow the instructions in the Flu And Coronavirus Simulator (FACS) "https://facs.readthedocs.io/en/latest/" to clone the FACS (simulation model).

Modify config.yml to point to run.py in facs directory. Also, the required resources can be set here:

    num_cpus: 16384
    num_nodes: 64
    cpu_per_task: 8
    num_tasks: 2
    script_path: "/path/to/facs/run.py"

### Modify run_simulation.sh to contain all locations. Currently, for simplicity, two locations are set:

    locations=("hillingdon" "greater_manchester")

### Run the Python script to submit 100 jobs of "hillingdon" and "greater_manchester":

    python3 submit_simulation.py

### Monitor and Retrieve Results:

Use DIRAC commands to monitor job status and retrieve results.

    dirac-wms-job-status <JobID>
    dirac-wms-job-get-output <JobID>

#### Alternatively, you can use the monitoring script:

    python3 test/monitor.py <JobID>

### Note: The installation process can be complex. Please raise a GitHub issue as soon as you encounter a problem. 

