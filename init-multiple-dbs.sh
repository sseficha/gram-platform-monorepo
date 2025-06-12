#!/bin/bash
set -e

# Esperamos a que postgres esté aceptando conexiones
until pg_isready -U "$POSTGRES_USER"; do
  echo "Waiting for postgres to be ready..."
  sleep 2
done

DATABASES=${POSTGRES_DATABASES}

IFS=',' read -ra DBS <<< "$DATABASES"

for DB in "${DBS[@]}"; do
  echo "Checking if database '$DB' exists..."
  DB_EXIST=$(psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -tAc "SELECT 1 FROM pg_database WHERE datname='${DB}'")
  if [ "$DB_EXIST" != "1" ]; then
    echo "Creating database: $DB"
    createdb -U "$POSTGRES_USER" -O "$POSTGRES_USER" -T template0 "$DB"
  else
    echo "Database '$DB' already exists"
  fi
done
