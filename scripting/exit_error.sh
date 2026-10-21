#!/usr/bin/env bash

# echo "Application started"
# exit 0

# if [[ ! -f "requirements.txt" ]]; then
#     echo "ERROR: requirements.txt not found."
#     exit 1
# fi

# echo "Requirements file found."
# exit 0

#-------------------------------------

# pytest
# if [[ $? -ne 0 ]]; then
#     echo "Tests failed. Deployment stopped."
#     exit 1
# fi

# echo "Tests passed. Ready to deploy."


#----------------------------------------------

# if ! pytest; then
#     echo "Tests failed. Deployment stopped."
#     exit 1
# fi

# echo "Tests passed. Ready to deploy."


#---------------------------
#!/usr/bin/env bash

count=1

while [[ "$count" -le 5 ]]; do
    echo "Attempt: $count"
    count=$((count + 1))
done