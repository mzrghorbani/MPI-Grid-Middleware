Overwriting Middleware Configuration on the Primary Node of the Grid Cluster

The middleware is designed to override the existing configuration files in the grid middleware.

Note: This modification requires admin access.

Steps to Clone the Repository and Override the Existing Configuration Files
Clone the repository:

    git clone https://github.com/mzrghorbani/MPI-Grid-Middleware.git

Navigate to the repository directory:

    cd MPI-Grid-Middleware

Make the override script executable:

    chmod +x override.sh

Modify (SOURCE_DIR and TARGET_DIR), and run the override script:

    bash override.sh <SOURCE_DIR> <TARGET_DIR>

If you are familiar with the job submission process, please skip to the Practical Example section.

Useful resources:

    https://dirac.readthedocs.io/en/latest/UserGuide/GettingStarted/InstallingClient/index.html


Install DIRAC:

    wget -np -O dirac-install https://github.com/DIRACGrid/DIRAC/raw/integration/Core/scripts/dirac-instachmod +x dirac-install

Directory structure:

    drwxr-xr-x 8 mghorbani root 2048 Mar 25 2010 Linux_x86_64_glibc-2.5
    drwxr-xr-x 16 mghorbani root 2048 Oct 12 12:13 DIRAC
    -rwxr-xr-x 1 mghorbani root 21224 Oct 12 13:37 dirac-install
    drwxr-xr-x 2 mghorbani root 10240 Oct 12 17:11 scripts
    -rw-r--r-- 1 mghorbani root 998 Oct 12 17:15 bashrc

Install VO Client:

    wget -np -O dirac-install http://lhcbproject.web.cern.ch/lhcbproject/dist/Dirac_project/dirac-installchmod +x dirac-install
    dirac-install -V formation
    source bashrc
    dirac-proxy-init
    dirac-configure defaults_formation.cfg

Configure VO Client:

    dirac-configure -V dirac -S Dirac-Production -C dips://dirac.in2p3.fr:9135/Configuration/Server

Simple Test JDL:

    Executable = "/bin/cp";
    Arguments = "my.file my.copy";
    InputSandbox = {"my.file"};
    StdOutput = "std.out";
    StdError = "std.err";
    OutputSandbox = {"std.out","std.err","my.copy"};
    CPUTime = 10;

Status:

    dirac-wms-job-status <jobid>

Get output:

    dirac-wms-job-get-output <jobid>

DIRAC API:

    from DIRAC.Interfaces.API.Job import Job
    from DIRAC.Interfaces.API.Dirac import Dirac
    dirac = Dirac()
    j = Job()
    j.setCPUTime(500)
    j.setExecutable('/bin/echo hello')
    j.setExecutable('/bin/hostname')
    j.setExecutable('/bin/echo hello again')
    j.setName('API')
    jobID = dirac.submit(j)
    print 'Submission Result: ',jobID

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

Practical Example:

Ensure mpi4py libraries are installed. If not, plesae follow instructions below for Ubuntu 22.04:

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

Set Up DIRAC Environment:

    source /path/to/DIRAC/bashrc

Configure Your Resources:

    Edit the config.yml file to specify the number of CPUs, nodes, and CPUs per task.

Make the Executable Script Executable or use existing template:

    chmod +x run_simulation.sh

Submit Jobs:

Run the python script to submit 100 jobs, each containing 20 tasks to DIRAC.

    python3 submit_simulation.py

Monitor and Retrieve Results:

Use DIRAC commands to monitor job status and retrieve results.

    dirac-wms-job-status <JobID>
    dirac-wms-job-get-output <JobID>

The added template setup has been used to submit 100 jobs each containing 20 tasks in parallel. Please feel free to modify for different settings.
