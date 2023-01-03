#!/bin/sh

# {"Shell":[".bashrc",".ca",".install",".run"],"Python":["make_dirac_copies.py","nfs.py","params.py","pingPongHandler    .py","plot.py","test/getOutput.py","test/monitor.py","test/submit.py","test_MPI.py"]}
 
 export GLOBUS_LOCATION=/usr
 
 if [ "x$1" = "x0" ]; then
   # Set environment variable containing queue name
   env_idx=0
   env_var="joboption_env_$env_idx"
   while [ -n "${!env_var}" ]; do
      env_idx=$((env_idx+1))
      env_var="joboption_env_$env_idx"
   done 
   eval joboption_env_$env_idx="NORDUGRID_DIRAC_QUEUE=$joboption_queue"
 	
   export RUNTIME_ENABLE_MULTICORE_SCRATCH=1
 
 fi
 
 if [ "x$1" = "x1" ]; then
   # Set grid environment
   if [ -e /etc/profile.d/env.sh ]; then
      source /etc/profile.d/env.sh
   fi 
   if [ -e /etc/profile.d/zz-env.sh ]; then
      source /etc/profile.d/zz-env.sh
   fi
   export LD_LIBRARY_PATH=/opt/xrootd/lib
 
   # Set basic environment variables
   export GLOBUS_LOCATION=/usr
   HOME=`pwd`
   export HOME
   USER=`whoami`
   export USER
   HOSTNAME=`hostname -f`
   export HOSTNAME
 fi
 
 export DPM_HOST=dc2-grid-64.brunel.ac.uk
 export DPNS_HOST=hepgrid11.ph.lon.ac.uk
 export GLEXEC_LOCATION=/usr
 export RFIO_PORT_RANGE=20000,25000
 export SITE_GIIS_URL=hepgrid4.ph.lon.ac.uk
 export SITE_NAME=dc2-grid-22.brunel.ac.uk
 export MYPROXY_SERVER=lcgrbp01.gridpp.rl.ac.uk
 
 
 export VO_ALICE_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_ALICE_SW_DIR=/opt/exp_soft_sl5/alice
 export VO_ATLAS_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_ATLAS_SW_DIR=/cvmfs/atlas.cern.ch/repo/sw
 export VO_BIOMED_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_BIOMED_SW_DIR=/opt/exp_soft_sl5/biomed
 export VO_CALICE_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_CALICE_SW_DIR=/opt/exp_soft_sl5/calice
 export VO_CAMONT_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_CAMONT_SW_DIR=/opt/exp_soft_sl5/camont
 export VO_CDF_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_CDF_SW_DIR=/opt/exp_soft_sl5/cdf
 export VO_CERNATSCHOOL_ORG_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_CERNATSCHOOL_ORG_SW_DIR=/opt/exp_soft_sl5/cernatschool
 export VO_CMS_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_CMS_SW_DIR=/opt/exp_soft_sl5/cms
 export VO_DTEAM_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_DTEAM_SW_DIR=/opt/exp_soft_sl5/dteam
 export VO_DZERO_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_DZERO_SW_DIR=/opt/exp_soft_sl5/dzero
 export VO_EPIC_VO_GRIDPP_AC_UK_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_EPIC_VO_GRIDPP_AC_UK_SW_DIR=/opt/exp_soft_sl5/epic
 export VO_ESR_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_ESR_SW_DIR=/opt/exp_soft_sl5/esr
 export VO_FUSION_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_FUSION_SW_DIR=/opt/exp_soft_sl5/fusion
 export VO_GEANT4_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_GEANT4_SW_DIR=/opt/exp_soft_sl5/geant4
 export VO_GRIDPP_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_GRIDPP_SW_DIR=/opt/exp_soft_sl5/gridpp
 export VO_HYPERK_ORG_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_HYPERK_ORG_SW_DIR=/cvmfs/hyperk.egi.eu
 export VO_ILC_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_ILC_SW_DIR=/cvmfs/ilc.desy.de
 export VO_LHCB_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_LHCB_SW_DIR=/cvmfs/lhcb.cern.ch
 export VO_LZ_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_LZ_SW_DIR=/opt/exp_soft_sl5/lsst
 export VO_LSST_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_LSST_SW_DIR=/opt/exp_soft_sl5/lsst
 export VO_MAGIC_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_MAGIC_SW_DIR=/opt/exp_soft_sl5/magic
 export VO_MICE_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_MICE_SW_DIR=/cvmfs/mice.egi.eu
 export VO_NA62_VO_GRIDPP_AC_UK_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_NA62_VO_GRIDPP_AC_UK_SW_DIR=/cvmfs/na62.cern.ch
 export VO_NEISS_ORG_UK_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_NEISS_ORG_UK_SW_DIR=/opt/exp_soft_sl5/neiss
 export VO_OPS_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_OPS_SW_DIR=/opt/exp_soft_sl5/ops
 export VO_PHENO_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_PHENO_SW_DIR=/opt/exp_soft_sl5/pheno
 export VO_PLANCK_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_PLANCK_SW_DIR=/opt/exp_soft_sl5/planck
 export VO_SNOPLUS_SNOLAB_CA_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_SNOPLUS_SNOLAB_CA_SW_DIR=/cvmfs/snoplus.egi.eu
 export VO_T2K_ORG_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_T2K_ORG_SW_DIR=/cvmfs/t2k.egi.eu
 export VO_VO_NORTHGRID_AC_UK_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_VO_NORTHGRID_AC_UK_SW_DIR=/opt/exp_soft_sl5/northgrid
 export VO_ZEUS_DEFAULT_SE=hepgrid11.ph.liv.ac.uk
 export VO_ZEUS_SW_DIR=/opt/exp_soft_sl5/zeus
 
 export RUCIO_HOME=/cvmfs/cms.cern.ch/repo/sw/ddm/rucio-clients/0.1.12
 export RUCIO_AUTH_TYPE=x509_proxy 
 
 export LCG_GFAL_INFOSYS="lcg-bdii.gridpp.ac.uk:2170,topbdii.grid.hep.ph.ic.ac.uk:2170,dc2-grid-64.brunel.ac.uk:2170"
 
 # Fix to circumvent DIRAC Globus Libraries
 # (i.e. this error: lcg-cr: /usr/lib64/dirac/libglobus_common.so.0: no version information available (required by /usr/lib64/libcgsi_plugin.so.1)
 export LD_LIBRARY_PATH=/usr/lib64/:$LD_LIBRARY_PATH

requirements = (OpSysName == "linux")
universe = mpich_g2
executable = openmpiscript
arguments = arguments = -np 160 my_mpi_linked_executable arg1 arg2 arg3
ntasks=20
machine_count = 3
request_cpus = 160
cpu_per_task=7
input = infile.$(Node)
output = outfile.$(Node)
error = errfile.$(Node)
should_transfer_files = yes
when_to_transfer_output = on_exit
transfer_input_files = my_openmpi_linked_executable
queue

dirac_status -const '!isUndefined(DedicatedScheduler)' \
      -format "%s\t" Machine -format "%s\n" DedicatedScheduler

+ParallelShutdownPolicy = "WAIT_FOR_ALL"
on_exit_remove = (ExitBySignal == False) && (ExitCode == 0)

# YOU MUST CHANGE THIS TO THE PREFIX DIR OF MPICH-G2
MPDIR=/usr

#if `uname -m | grep "64" 1>/dev/null 2>&1` 
#then 
    #MPDIR=/usr/lib64/mpich
#fi

PATH=/usr/bin:$MPDIR:.:$PATH
export PATH
LD_LIBRARY_PATH=/usr/lib/openmpi/lib:/usr/bin:.:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH

_DIRAC_PROCNO=$_DIRAC_PROCNO
_DIRAC_NPROCS=$_DIRAC_NPROCS

DIRAC_SSH=`dirac_config_val libexec`
DIRAC_SSH=$DIRAC_SSH/dirac_ssh

SSHD_SH=`dirac_config_val libexec`
SSHD_SH=$SSHD_SH/sshd.sh

. $SSHD_SH $_DIRAC_PROCNO $_DIRAC_NPROCS 

# If not the head node, just sleep forever, to let the sshds run
if [ $_DIRAC_PROCNO -ne 0 ]
then
  wait
  sshd_cleanup
  exit 0
fi

WDIR=$1
shift
EXECUTABLE=$1
shift

# the binary is copied but the executable flag is cleared.
# so the script have to take care of this
chmod +x $EXECUTABLE

DIRAC_CONTACT_FILE=$_DIRAC_SCRATCH_DIR/contact
export DIRAC_CONTACT_FILE

# The second field in the contact file is the machine name
# that dirac_ssh knows how to use
sort -n -k 1 < $DIRAC_CONTACT_FILE | awk '{print $2}' > machines

## run the actual mpijob
echo -e "---\non nodes:"
cat machines

#insert here some commands needed to run your job
source /home/common/Planck15/plc-2.0/bin/clik_profile.sh

echo -e "---\n`date`\n---\nrunning:"
echo mpirun.openmpi -v --prefix $MPDIR --mca btl_tcp_if_exclude lo,docker0 --mca plm_rsh_agent $DIRAC_SSH -n $_DIRAC_NPROCS  --host `paste -sd',' machines` -wdir $WDIR $EXECUTABLE $@
mpirun.openmpi -v --prefix $MPDIR --mca btl_tcp_if_exclude lo,docker0 --mca plm_rsh_agent $DIRAC_SSH -n $_DIRAC_NPROCS  --host `paste -sd',' machines` -wdir $WDIR $EXECUTABLE $@ 
err=$?
echo mpirun ended

sshd_cleanup
rm -f machines

echo exiting $err
exit $err

DedicatedScheduler = "scheduler_middleware"
START          = True
SUSPEND        = False
CONTINUE       = True
PREEMPT        = False
KILL           = False
WANT_SUSPEND   = False
WANT_VACATE    = False
RANK = Scheduler =?= $(brunel_hep) 
MPI_CONDOR_RSH_PATH = $(LIBEXEC)
CONDOR_SSHD = /usr/sbin/sshd
CONDOR_SSH_KEYGEN = /usr/bin/ssh-keygen
STARTD_EXPRS = $(STARTD_EXPRS), DedicatedScheduler
MPICH_INSTALL_PATH = /usr
MPICH_EXCLUDE_NETWORK_INTERFACES = dirac,condor,arc
MOUNT_UNDER_SCRATCH = /
MPI_Init(&argc, &argv)
MPI_Comm_size = nprocs
MPI_Comm_rank = myrank)
gethostname = $(hostname)

mpirun -v -wdir /vagrant/ejemplo/openfoam/damBreak \
      --prefix $MPDIR --mca $mca_ssh_agent $DIRAC_SSH \ 
      -n $_DIRAC_NPROCS -hostfile machines $EXECUTABLE $@ &

ALLOW_READ = *                        
ALLOW_WRITE = * 
HOSTALLOW_READ = *
HOSTALLOW_WRITE = *
ALLOW_NEGOTIATOR = *
ALLOW_ADMINISTRATOR = *
COLLECTOR_DEBUG = D_FULLDEBUG
NEGOTIATOR_DEBUG = D_FULLDEBUG
MATCH_DEBUG = D_FULLDEBUG
SCHEDD_DEBUG = D_FULLDEBUG
TRUST_UID_DOMAIN = TRUE
DIRAC_HOST = controller
UID_DOMAIN = controller
FILESYSTEM_DOMAIN = controller
DAEMON_LIST = MASTER, STARTD
ALLOW_WRITE = $(ALLOW_WRITE), $(CONDOR_HOST)
STARTER_ALLOW_RUNAS_OWNER = true
USE_SHARED_PORT = FALSE
NETWORK_INTERFACE = eth1

data_path = '/home/gridpp/mydata'
lfn_dir = '/gridpp/user/m/maziar.ghorbani/mydata'
replicate ${lfn_dir} UKI-NORTHGRID-LONDON-HEP-disk

for dir in tempdir
do
  cd ${PWD}/${dir}
  rm -f logs.*
  dirac_submit submitfile
done

rmreplica ${lfn_dir} UKI-NORTHGRID-LONDON-HEP-disk

if [${PROCESS} = 'Failed']
then
  echo 'fail'
else
  echo 'complete'
fi

date
