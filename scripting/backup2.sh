
#!/usr/bin/env bash

set -Eeuo pipefail

# 1. Define source and destination.
SOURCE_DIR="$HOME/backup-lab/myapp"
BACKUP_DIR="$HOME/backup-lab/backups"

# 2. Validate the source directory.
if [[ ! -d "$SOURCE_DIR" ]]; then
    printf 'ERROR: Source directory not found: %s\n' "$SOURCE_DIR" >&2
    exit 1
fi

# 3. Create the destination directory.
mkdir -p "$BACKUP_DIR"

# 4. Generate a unique-looking timestamped filename.
TIMESTAMP="$(date +%Y%m%d-%H%M%S)"
ARCHIVE="$BACKUP_DIR/myapp-$TIMESTAMP.tar.gz"

# 5. Create the archive with relative paths.
tar -czf "$ARCHIVE" -C "$(dirname "$SOURCE_DIR")" \
    "$(basename "$SOURCE_DIR")"

# 6. Verify that the archive can be listed.
tar -tzf "$ARCHIVE" >/dev/null

# 7. Report success only after verification.
printf 'Backup created and listing verified: %s\n' "$ARCHIVE"
