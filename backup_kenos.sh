#!/data/data/com.termux/files/usr/bin/bash

DATE=$(date +%Y%m%d_%H%M%S)

BACKUP="$HOME/storage/shared/Documents/KenOS_Backup_$DATE"

echo "Creating KenOS backup..."

cp -r "$HOME/KenOS" "$BACKUP"

echo ""
echo "✓ Backup completed"
echo "Location:"
echo "$BACKUP"
