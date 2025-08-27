#!/bin/bash

# Define the path to your JupyterBook content
CONTENT_DIR="book"  # Adjust this to your content directory
STATIC_DIR="_static"  # Path to the _static directory

# Find all markdown files and build them individually
find $CONTENT_DIR -name '*oppgave*.md' | while read file; do
    echo "Building PDF for file: $file"
    
    # Get the directory of the current file
    FILE_DIR=./$(dirname "$file")
    
    # Temporarily copy the _static directory to the file's directory
    cp -r "$STATIC_DIR" "${FILE_DIR}"
    
    # Run the jb build command for each file
    jb build "$file" --builder pdfhtml
    
    # Remove the _static directory from the file's directory once build is complete
    rm -rf "${FILE_DIR}/_static"
done