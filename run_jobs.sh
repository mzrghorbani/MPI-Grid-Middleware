#!/bin/bash
# This script runs the specified command using mpirun in parallel

# Number of CPUs to use
num_cpus=$1

# Number of jobs to run
num_jobs=$2

# Path to the Python script (run.py)
script_path=$3

# Array of locations
locations=("hillingdon" "greater_manchester" "berkshire" "blackburn_with_darwen" "blackpool" "brent" "buckinghamshire" "calarasi" "cheshire_east" "cheshire_west_and_chester" "cumbria" "east_sussex" "hillingdon" "kent" "lancashire" "merseyside" "oxfordshire" "surrey" "warrington" "west_sussex")

# Loop to run the jobs in parallel
for ((job=1; job<=num_jobs; job++)); do
  echo "Running job $job in parallel..."

  # Loop through locations, running each in the background
  for location in "${locations[@]}"; do
    mpirun -np $num_cpus python "$script_path" --location=$location --measures_yml=measures_uk --disease_yml=disease_covid19 --vaccinations_yml=vaccinations --starting_infections=10 --simulation_period=365 &
  done

  # Wait for all background jobs to complete before starting the next set
  wait
done

echo "All jobs completed."
