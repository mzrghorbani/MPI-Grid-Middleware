Useful resources:

    https://buildmedia.readthedocs.org/media/pdf/dirac/rel-v6r15/dirac.pdf


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
