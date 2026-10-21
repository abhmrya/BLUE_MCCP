# # #!/usr/bin/env bash

# # APP_ENV="staging"

# # if [[ "$APP_ENV" == "production" ]]; then
# #     echo "production deployment"
# # elif [[ "$APP_ENV" == "staging" ]]; then
# #     echo "staging deployment"
# # fi

# # #!/usr/bin/env bash

# # DB_FILE="assetops.db"

# # if [[ -f "$DB_FILE" ]]; then
# #     echo "Database file exists. Ready for backup."
# # else
# #     echo "Error: Database file not found."
# #     exit 1
# # fi



# #!/usr/bin/env bash

PROJECT_DIR="$1"
# APP_ENV="${2:-development}"

# # TODO 1:
# # If PROJECT_DIR is empty:
# # Print "Error: Project directory is required."
# # Exit with code 1.

# echo "$PROJECT_DIR"

# if [[ -z "$PROJECT_DIR" ]]; then
#     echo "Error: Project directory is required."
#     exit 1
# fi

# # TODO 2:
# # If PROJECT_DIR is not a directory:
# # Print "Error: Project directory not found."
# # Exit with code 1.

# if [[ ! -d "$PROJECT_DIR" ]]; then
#     echo "Error: Project directory not found."
#     exit 1
# fi

# echo "Project directory: $PROJECT_DIR"
# echo "Application environment: $APP_ENV"

# # TODO 3:
# # If APP_ENV equals "production":
# # Print "Production environment selected."

# if [[ "$APP_ENV" == "production" ]]; then
#     echo "Production environment selected."

# elif [[ "$APP_ENV" == "staging" ]]; then
#     echo "Staging environment selected."

# else 
#     echo "Development environment selected."
# fi

# # Else if APP_ENV equals "staging":
# # Print "Staging environment selected."
# #
# # Otherwise:
# # Print "Development environment selected."

# # TODO 4:
# # If all checks pass, print:
# # "Pre-deployment checks passed."

# echo "Pre-deployment checks passed."


if [[ ! -f "$PROJECT_DIR/requirements.txt" ]];then
    echo "ERROR: requiremnts.txt not found."
    exit 1
fi