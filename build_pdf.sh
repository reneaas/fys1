#!/bin/bash

file=$1


# Define the path to your JupyterBook content
CONTENT_DIR="book"  # Adjust this to your content directory
STATIC_DIR="_static"  # Path to the _static directory

FILE_DIR=./$(dirname "$file")

cp -r "$STATIC_DIR" "${FILE_DIR}"

jb build "$file" --builder pdfhtml

rm -rf "${FILE_DIR}/_static"
