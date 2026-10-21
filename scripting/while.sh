#!/usr/bin/env bash

attempt=1
MAX_ATTEMPTS=5

# TODO 1:
# Create a while loop that runs while
# attempt is less than or equal to MAX_ATTEMPTS.

while [[ "$attempt" -le "$MAX_ATTEMPTS" ]]; do
    echo "attempt number $attempt"

    attempt=$((attempt+1))

done 
echo "complite task"

# TODO 2:
# Print "Attempt: <attempt>"

# TODO 3:
# Increase attempt by 1.

# TODO 4:
# After the loop, print:
# "All attempts completed."
