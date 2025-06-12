#!/bin/bash
set -e

USER="${POSTGRES_USER:-admin}"
IFS=',' read -ra DBS <<< "${POSTGRES_DATABASES:-postgres}"

for DB in "${DBS[@]}"; do
  pg_isready -U "$USER" -d "$DB" > /dev/null 2>&1
  if [ $? -ne 0 ]; then
    echo "❌ Database $DB is not ready"
    exit 1
  fi
done

echo "✅ All databases are ready"
exit 0