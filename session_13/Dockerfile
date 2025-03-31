FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app/

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "src.session_13.exercise_with_challenge.main:app", "--host", "0.0.0.0", "--port", "8000"]
