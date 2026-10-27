#!/bin/bash

set -Eeuo pipefail

BACKUP_NAME="myapp-backup-$(date +%Y%m%d-%H%M%S).tar.gz"

if [[ ! -f deploy.sh ]]; then
    echo "ERROR: deploy.sh not found" >&2
    exit 1
fi

tar -czf "$BACKUP_NAME" deploy.sh

tar -tzf "$BACKUP_NAME" > /dev/null

echo "Backup created and verified: $BACKUP_NAME"