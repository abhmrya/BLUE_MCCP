#!/usr/bin/env bash

echo "Hello , Abhay!"
echo "I am learning bash scripting"
echo "TOday I Wrote my first scripts."

name="Abhay Kumar Maurya"

echo "$name"
echo "$name"

APP_NAME="pergo-api"
APP_ENV="staging"
APP_VERSION="1.0.0"

echo "Application: $APP_NAME"
echo "Environment: $APP_ENV"
echo "Version: $APP_VERSION"


# *********lession 2 *************

#!/usr/bin/env bash

# TODO 1: Create a variable named SERVER_NAME
#         and assign it the value "production-server".
SERVER_NAME="production-server"

# TODO 2: Create a variable named SERVER_IP
#         and assign it the value "192.168.1.10".
SERVER_IP="192.168.1.10"
# TODO 3: Print the server name.
echo "server name: $SERVER_NAME"
# TODO 4: Print the server IP.
echo "server ip: $SERVER_IP"

# TODO 5: Print this message:
#         "Server is ready for deployment."
echo "Server is ready for deployment."

#************* lession 3  **********
echo "Enter server name."
read SERVER_NAME
echo "you selected: $SERVER_NAME"


read -r -p "Enter server name: " SERVER_NAME