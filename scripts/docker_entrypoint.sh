#!/bin/bash
echo "Running post-build commands..."
# Run migrations, create folders, etc.
make migrate-up
# Start the main application
exec uvicorn main:app --host 0.0.0.0 --port 8000
