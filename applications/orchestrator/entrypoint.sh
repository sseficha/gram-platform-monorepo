#!/usr/bin/env bash
set -e

# 1. Run database migrations
echo "Running migrations..."
poetry run alembic upgrade head

# 2. Exit and run command passed
echo "Starting main process..."
exec "$@"
