#!/bin/bash

# Get the current working directory
CWD="$(pwd)"

# Navigate to the directory where the script is located
cd "$CWD"

# Check if the build was successful before launching the executable
if [ -f "./apprentice_generator_gui" ]; then
    ./apprentice_generator_gui
else
    echo "./apprentice_generator_gui not found"
fi
