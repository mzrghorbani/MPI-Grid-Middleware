#!/bin/bash

# Paths for DIRAC and middleware directories (adjust these as needed)
DIRAC_DIR="$HOME/diracos"
MIDDLEWARE_DIR="$HOME/MPI-Grid-Middleware"
CONFIG_FILE="$MIDDLEWARE_DIR/config.yml"
INITIALIZE_SCRIPT="$MIDDLEWARE_DIR/pool_resources.py"  # Script for pooling resources
SUBMIT_SCRIPT="$MIDDLEWARE_DIR/submit_jobs.py"  # Script for job submission
LOG_FILE="$HOME/dirac_job_submission.log"

# Configure DIRAC if not already done
if [ ! -f "$DIRAC_DIR/etc/dirac.cfg" ]; then
    echo "Configuring DIRAC client..."
    dirac-proxy-init -g gridpp_user -M -U
fi

# Overwrite DIRAC files with middleware modifications
echo "Applying middleware modifications to DIRAC directories..."
if [ ! -f "MIDDLEWARE_DIR/override.sh" ]; then
    echo "Overriding dirac with grid middleware..."
    bash MIDDLEWARE_DIR/override.sh
fi

# Run configuration for Dirac and Middleware
echo "Applying middleware configuration to DIRAC..."
if [ ! -f "MIDDLEWARE_DIR/run_config.sh" ]; then
    echo "Add middleware configuration to dirac..."
    bash MIDDLEWARE_DIR/run_config.sh
fi

# Check if required middleware files are copied
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Configuration file ($CONFIG_FILE) missing. Ensure all middleware files are in place."
    exit 1
fi

# Run resource pooling initialization
echo "Pooling resources using initialization script..."
if [ -f "$INITIALIZE_SCRIPT" ]; then
    python "$INITIALIZE_SCRIPT"
else
    echo "Initialization script ($INITIALIZE_SCRIPT) not found. Aborting."
    exit 1
fi

# Submit jobs
echo "Submitting jobs..."
if [ -f "$SUBMIT_SCRIPT" ]; then
    python "$SUBMIT_SCRIPT" | tee -a "$LOG_FILE"
else
    echo "Job submission script ($SUBMIT_SCRIPT) not found. Aborting."
    exit 1
fi

echo "Job submission complete. Logs saved to $LOG_FILE."
