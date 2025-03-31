build:
	docker compose build

start:
	docker compose up -d --force-recreate --build

down:
	docker compose down --volumes

logs:
	docker compose logs -f

api-logs:
	docker compose logs -f api

db-logs:
	docker compose logs -f db

test:
	docker compose run --rm api poetry run pytest -v
