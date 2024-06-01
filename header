#!/bin/bash
# This script runs the specified command using mpirun

# Number of CPUs to use
num_cpus=$1
num_nodes=$2
cpu_per_task=$3

# Number of tasks to run
num_tasks=$4

# Run the command with mpirun for each task
for ((i=1; i<=num_tasks; i++)); do
  mpirun -np $num_cpus python run.py --location=hillingdon --measures_yml=measures_uk --disease_yml=disease_covid19 --vaccinations_yml=vaccinations --starting_infections=1 --simulation_period=10
done

