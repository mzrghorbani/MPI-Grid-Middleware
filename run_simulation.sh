#!/bin/bash
# This script runs the specified command using mpirun

# Number of CPUs to use
num_cpus=$1

# Number of jobs to run
num_jobs=$2

# Path to the Python script (run.py)
script_path=$3

# Array of locations
locations=("hillingdon" "greater_manchester")

# Loop to run the jobs
for ((job=1; job<=num_jobs; job++)); do
  echo "Running job $job..."
  for location in "${locations[@]}"; do
    mpirun -np $num_cpus python "$script_path" --location=$location --measures_yml=measures_uk --disease_yml=disease_covid19 --vaccinations_yml=vaccinations --starting_infections=1 --simulation_period=10
  done
done

