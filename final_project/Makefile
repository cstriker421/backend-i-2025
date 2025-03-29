# ==============================
# Default Variables
# ==============================
BOOK="Dune"
AUTHOR="Frank Herbert"
GENRE="Sci-Fi"
STATUS="reading"
RATING=5
ID=1
MINUTES=30
NOTES=""

# ==============================
# Docker Commands
# ==============================
.PHONY: docker-up docker-down docker-shell docker-migrate docker-makemigrations docker-superuser

docker-up: ## Build and start Docker containers
	docker compose up --build

docker-down: ## Stop Docker containers
	docker compose down

docker-shell: ## Open a shell inside web container
	docker compose run web sh

docker-migrate: ## Run Django migrations
	docker compose run --rm web poetry run python manage.py migrate

docker-makemigrations: ## Make Django migrations
	docker compose run --rm web poetry run python manage.py makemigrations

docker-superuser: ## Create Django superuser
	docker compose run --rm web poetry run python manage.py createsuperuser

# ==============================
# Pytest Commands
# ==============================
.PHONY: docker-test docker-test-django docker-test-cli pytest-local

docker-test: ## Run all tests (Django + CLI)
	docker compose run --rm --remove-orphans web poetry run pytest -v tests/

docker-test-django: ## Run Django tests
	docker compose run --rm --remove-orphans web poetry run pytest -v \
		tests/test_views.py tests/test_models.py tests/test_forms.py tests/test_urls.py

docker-test-cli: ## Run CLI tests
	docker compose run --rm --remove-orphans web poetry run pytest -v tests/test_cli.py

pytest-local: ## Run tests locally (only if not in Docker)
	python -m pytest

# ==============================
# Django Local Commands
# ==============================
.PHONY: runserver migrate makemigrations createsuperuser

runserver: ## Run Django server locally
	python manage.py runserver

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

createsuperuser:
	python manage.py createsuperuser

# ==============================
# Book CLI Commands (Dockerized)
# ==============================
.PHONY: book-add book-list book-summary book-mark-read book-log book-help

book-add: ## Add a new book (Override vars: make book-add BOOK="..." AUTHOR="..." etc.)
	docker compose run --rm web poetry run python -m cli.cli book add \
		--title=$(BOOK) \
		--author=$(AUTHOR) \
		--genre=$(GENRE) \
		--status=$(STATUS) \
		--rating=$(RATING)

book-list: ## List all books
	docker compose run --rm web poetry run python -m cli.cli book list

book-summary: ## Show reading summary
	docker compose run --rm web poetry run python -m cli.cli book summary

book-mark-read: ## Mark a book as read (ID variable)
	docker compose run --rm web poetry run python -m cli.cli book mark-read $(ID)

book-log: ## Log reading session (ID, MINUTES, NOTES variables)
	docker compose run --rm web poetry run python -m cli.cli book log-reading $(ID) $(MINUTES) --notes=$(NOTES)

book-help: ## Show CLI options
	docker compose run --rm web poetry run python -m cli.cli --help

# ==============================
# Help
# ==============================
.PHONY: help

help:
	@echo ""
	@echo "📚 Book Tracker Makefile Commands"
	@echo "----------------------------------"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-22s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "🔹 Example (override book variables):"
	@echo '    make book-add BOOK="Neuromancer" AUTHOR="William Gibson"'
	@echo "🔹 Run 'make book-help' to see CLI options"
	@echo ""

