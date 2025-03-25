start:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

migrations:
	poetry run python manage.py makemigrations $(app)

createsuperuser:
	poetry run python manage.py createsuperuser

new-app:
	poetry run python manage.py startapp $(app)
	@# to execute run `make new-app app=things`

tests:
	poetry run pytest -vvv

py3clean:
	py3clean .

compose.start:
	docker compose up --build --force-recreate

compose.migrate:
	docker compose run -rm web poetry run python manage.py migrate