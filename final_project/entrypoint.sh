#!/bin/sh

# Exit on any error
set -e

# Apply DB migrations
echo "🛠️ Running migrations..."
export PYTHONPATH=/app
python manage.py migrate

# Optional: collect static files (skip if not needed)
# echo "📦 Collecting static files..."
# python manage.py collectstatic --noinput

# Launch app
echo "🚀 Starting server..."
exec "$@"
