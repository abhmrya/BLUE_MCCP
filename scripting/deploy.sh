# APP_NAME="$1"
# APP_ENV="$2"

# echo "Application: $APP_NAME"
# echo "Environment: $APP_ENV"
# echo "Arguments received: $#"
# echo "All Arguments: $@"


# APP_ENV="${1:-development}"

# echo "Environment: $APP_ENV"



#!/usr/bin/env bash

# APP_NAME="$1"
# APP_ENV="${2:-development}"

# if [[ -z "$APP_NAME" ]]; then
#     echo "Error: Application name is required."
#     exit 1
# fi

# echo "Application name: $APP_NAME"
# echo "Environment: $APP_ENV"
# echo "Number of arguments passed: $#"

# exit 0

# echo $?



AGE=2

if [[ "$AGE" -ge 18 ]]; then
    echo "Adult"
else
    echo "Minor"
fi