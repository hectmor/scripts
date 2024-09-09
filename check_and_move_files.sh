#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <name_file>"
    exit 1
fi

name_file="$1"
file_success="files_copied.txt"
file_error="files_copy_error.txt"

if [ ! -f "$name_file" ]; then
    echo "File $name_file does not exist."
    exit 1
fi

if [ -f "$file_success" ]; then
    rm $file_success
fi

if [ -f "$file_error" ]; then
   rm $file_error
fi

# Create the 'copy' folder if it doesn't already exist
mkdir -p zz_id_errors

success=0
errors=0
# Read each folder name from the file and process it
while IFS= read -r folder; do
    if [ -z $folder]; then
      break 
    fi
    if [ -d "$folder" ]; then
        echo "Copying $folder to the 'copy' folder..."
        echo $folder >> $file_success
        cp -r "$folder" zz_id_errors/
        success=$((success+1))
    else
        echo "ERROR $folder does not exist."
        echo $folder >> $file_error
        errors=$((errors+1))
    fi
done < "$name_file"

echo "Successes: $success, Errors: $errors"
echo "Operation completed."
