#!/bin/bash
DATE=$(date)
SERVER_URL="http://localhost:8080/upload"
FILES_DIR=$(pwd)
for file in "$FILES_DIR"/*; do
  if [ -f "$file" ]; then
    filename=$(basename "$file")
    new_filename="${filename%.*}-$(hostname)-$DATE.${filename##*.}"
    curl -X POST -F "file=@$file;filename=$new_filename" $SERVER_URL
  fi
done
