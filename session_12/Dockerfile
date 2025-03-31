FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install

COPY ./src/session_12/exercise_with_challenge /app/

COPY ./tests /app/tests

RUN mkdir -p /app/logs

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
