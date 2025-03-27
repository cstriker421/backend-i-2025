FROM python:3.12-slim

# Sets working directory
WORKDIR /app

# Installs system dependencies for psycopg2 and other native builds
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Installs Poetry
RUN pip install poetry

# Copies pyproject.toml and lock file first for caching dependencies
COPY pyproject.toml poetry.lock* /app/

# Copies the rest of the project before installing
COPY . /app/

# Debugs what files are present
RUN ls -la /app

# Installs Python dependencies without creating a virtualenv
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Copies the entrypoint script and ensures it's executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Uses entrypoint to handle migrations before app launchcd
ENTRYPOINT ["/entrypoint.sh"]

# Exposes port 8000 for Uvicorn
EXPOSE 8000

# Starts the server
CMD ["poetry", "run", "uvicorn", "booktracker.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
