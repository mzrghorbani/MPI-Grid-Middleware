#!/bin/bash
export DIRACBRANCH=v6r13
export PRERELEASE=True
export DEBUG=True
export USER=mghorbani
export PASSWORD=password
export ROOTUSER=admin
export ROOTPWD=password
export HOST=UKI-LT2-Brunel-disk
export PORT=5501
source source /cvmfs/dirac.egi.eu/dirac/bashrc_gridpp
python /cvmfs/dirac.egi.eu/dirac/Framework/testInstalledComponentsDB.py -dd
python /cvmfs/dirac.egi.eu/dirac/Framework/testComponentInstallUninstall.py -dd
python /cvmfs/dirac.egi.eu/dirac/RequestManagementSystem/TestClientReq.py -dd
python /cvmfs/dirac.egi.eu/dirac/WorkloadManagementSystem/TestJobDB.py -dd
python /cvmfs/dirac.egi.eu/dirac/WorkloadManagementSystem/TestJobLoggingDB.py -dd
python /cvmfs/dirac.egi.eu/dirac/WorkloadManagementSystem/TestTaskQueueDB.py -dd
python /cvmfs/dirac.egi.eu/dirac/WorkloadManagementSystem/TestClientWMS.py 
echo "Getting a non privileged user"
dirac-proxy-init -C /cvmfs/dirac.egi.eu/dirac/.globus/client.pem -K $/cvmfs/dirac.egi.eu/dirac/.globus/client.key $DEBUG
python /cvmfs/dirac.egi.eu/dirac/Integration/DataManagementSystem/TestClientDFC.py -dd
# Run it with the admin privileges
echo "getting the prod role again"
dirac-proxy-init -g prod -C /cvmfs/dirac.egi.eu/dirac/.globus/client.pem -K /cvmfs/dirac.egi.eu/dirac/.globus/client.key $DEBUG
python /cvmfs/dirac.egi.eu/dirac/DataManagementSystem/TestClientDFC.py -dd
python /cvmfs/dirac.egi.eu/dirac/Integration/DataManagementSystem/TestClientFTS.py -dd
echo "**** ENV TESTS ****"
python /cvmfs/dirac.egi.eu/dirac//TransformationSystem/TestClientTransformation.py -dd
clean
echo "*** DONE ****"