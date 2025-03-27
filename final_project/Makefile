# Default Book values (Override with make BOOK="..." etc.)
BOOK="Dune"
AUTHOR="Frank Herbert"
GENRE="Sci-Fi"
STATUS="reading"
RATING=5

# Defaults for mark-read and log-reading
ID=1
MINUTES=30
NOTES=""

# Docker helpers
docker-up:
	@docker compose up --build

docker-down:
	@docker compose down

docker-shell:
	@docker compose run web sh

docker-migrate:
	@docker compose run web python manage.py migrate

docker-superuser:
	@docker compose run web python manage.py createsuperuser

# Django Management
.PHONY: runserver migrate makemigrations createsuperuser

runserver:
	@python manage.py runserver

migrate:
	@python manage.py migrate

makemigrations:
	@python manage.py makemigrations

createsuperuser:
	@python manage.py createsuperuser

# Book CLI commands
book-cli:
	@python -m cli.cli

book-add:
	@python -m cli.cli book add \
		--title=$(BOOK) \
		--author=$(AUTHOR) \
		--genre=$(GENRE) \
		--status=$(STATUS) \
		--rating=$(RATING)

book-list:
	@python -m cli.cli book list

book-summary:
	@python -m cli.cli book summary

book-mark-read:
	@python -m cli.cli book mark-read $(ID)

book-log:
	@python -m cli.cli book log-reading $(ID) $(MINUTES) --notes=$(NOTES)
