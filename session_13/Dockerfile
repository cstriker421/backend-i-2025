FROM python:3.12-slim

WORKDIR /app

# Copy Poetry configuration files
COPY pyproject.toml poetry.lock* /app/

# Install Poetry and dependencies
RUN pip install poetry

# Copy application code
COPY . /app/

RUN poetry install -nq

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]