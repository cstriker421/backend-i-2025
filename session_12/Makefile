start:
	COMPOSE_BAKE=True docker compose up -d --force-recreate --build

down:
	docker compose down --volumes

logs:
	docker compose logs -f

api-logs:
	docker compose logs -f app

test:
	docker compose run --rm app pytest -v