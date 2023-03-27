#!/bin/bash

# Get the current working directory
CWD="$(pwd)"

# Navigate to the directory where the script is located
cd "$CWD"

# Give read - write - execute permission to the src directory and its contents
chmod +rwx src

# Check if the build was successful before launching the executable
if [ -f "./src/apprentice_generator_gui" ]; then
    ./src/apprentice_generator_gui
else
    echo "./src/apprentice_generator_gui not found"
fi
