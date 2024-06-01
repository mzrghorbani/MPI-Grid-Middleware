#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <source_directory> <target_directory>"
    exit 1
fi

# Assign the arguments to variables
SOURCE_DIR=$1
TARGET_DIR=$2

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' does not exist."
    exit 1
fi

# Check if the target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Target directory '$TARGET_DIR' does not exist."
    exit 1
fi

# Loop through all files in the source directory
for file in "$SOURCE_DIR"/*; do
    if [ -f "$file" ]; then
        # Get the base name of the file
        base_file=$(basename "$file")
        # Copy the file to the target directory, overriding if it exists
        cp "$file" "$TARGET_DIR/$base_file"
        echo "Overridden: $TARGET_DIR/$base_file"
    fi
done

echo "All files have been overridden."

