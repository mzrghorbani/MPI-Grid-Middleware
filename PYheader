import yaml
from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.Interfaces.API.Dirac import Dirac
from DIRAC.Interfaces.API.Job import Job

# Function to create a DIRAC job
def create_job(executable, num_cpus, num_nodes, cpu_per_task, num_tasks):
    # Create a new job instance
    job = Job()
    # Set a name for the job
    job.setName("MyParallelJob")
    # Set the executable to run using mpirun with the specified number of CPUs and parameters
    job.setExecutable(executable, arguments=[str(num_cpus), str(num_nodes), str(cpu_per_task), str(num_tasks)])
    # Specify the output files to be retrieved after the job completes
    job.setOutputSandbox(["*.out", "*.log", "*.err"])
    return job

# Read configuration from the YAML file
with open("config.yml", 'r') as config_file:
    config = yaml.safe_load(config_file)

# Initialize the DIRAC interface
dirac = Dirac()

# Extract parameters from the configuration
num_cpus = config['num_cpus']
num_nodes = config['num_nodes']
cpu_per_task = config['cpu_per_task']
num_tasks = config['num_tasks']

# Path to the executable script
executable = "./run_simulation.sh"

# List to keep track of submitted job IDs
job_ids = []

# Loop to submit the job 100 times
for i in range(100):
    # Create a DIRAC job with the specified parameters
    job = create_job(executable, num_cpus, num_nodes, cpu_per_task, num_tasks)
    # Submit the job to the DIRAC system
    result = dirac.submit(job)
    # Check if the job submission was successful
    if result['OK']:
        # If successful, retrieve the Job ID and add it to the list of job IDs
        job_id = result['JobID']
        job_ids.append(job_id)
        print(f"Submitted job {job_id}")
    else:
        # If submission failed, print the error message
        print(f"Failed to submit job: {result['Message']}")

# Print all submitted job IDs
print("All jobs submitted. Job IDs:", job_ids)

