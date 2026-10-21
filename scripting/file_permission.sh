# 1. Understand the operators
# Operator	Meaning	Example
# -r	File is readable	[[ -r "$FILE" ]]
# -w	File is writable	[[ -w "$FILE" ]]
# -x	File is executable	[[ -x "$FILE" ]]
# -f	Path is a regular file	[[ -f "$FILE" ]]


#!/bin/bash

# FILE="app.sh"

# echo "$FILE"

# if [[ -r "FILE" ]]; then
#     echo "File is readable."
# else
#     echo "File is not readable."
# fi






#!/usr/bin/env bash

FILE="$1"

# TODO 1:
# If FILE is empty:
# Print "Error: File path is required."
# Exit with code 1.

if [[ -z "$FILE" ]]; then
    echo "Error: File path is required."
    exit 1
fi

# TODO 2:
# If FILE is not a regular file:
# Print "Error: File not found."
# Exit with code 1.



# TODO 3:
# If FILE is readable:
# Print "File is readable."

# TODO 4:
# If FILE is writable:
# Print "File is writable."

# TODO 5:
# If FILE is executable:
# Print "File is executable."







