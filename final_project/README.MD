# BookTracker 📚

**BookTracker** is a Django-based reading tracker app, enhanced with a Typer-powered Command Line Interface (CLI). It allows you to manage books you are reading, plan to read, or have finished, and log reading sessions.

---

## Features

### Django Web Application

- Book and ReadingSession models.
- Class-based views:
  - List all books.
  - Detail view for individual books.
  - Add new books.
  - Edit existing books.
  - Delete books.
- User registration, login, and logout.
- Admin interface for managing models.
- Book form for data entry.
- Minimal HTML templates.

### Typer CLI

- Register and login users.
- Add new books.
- List books.
- Mark books as read.
- Log reading sessions.
- View reading summary.
- Optional `--verbose` flag for debug logs.

### Project Setup

- Poetry for dependency management.
- Docker & Docker Compose integration.
- PostgreSQL database.
- Structured project with Makefile shortcuts.
- Logging implemented in Django views, forms, models, and CLI.

---

## Installation & Setup

### Prerequisites

- Docker & Docker Compose
- GNU Make

### Quickstart

Clone the repository:

```bash
git clone <your-repo-url>
cd final_project
```

Build and run the containers:

```bash
make docker-up
```

Run migrations:

```bash
make docker-migrate
```

(Optional) Create superuser:

```bash
make docker-superuser
```

Access the app:

- Web: [http://localhost:8000](http://localhost:8000)
- Admin Panel: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## CLI Usage

Run the CLI inside the container:

```bash
make book-help
```

Available commands:

```bash
make book-add          # Add a new book (Override vars: make book-add BOOK="..." AUTHOR="..." etc.)
make book-list         # List all books
make book-summary      # Show reading summary
make book-mark-read    # Mark a book as read (ID variable)
make book-log          # Log a reading session (ID, MINUTES, NOTES variables)
```

**User management (manual commands):**
```bash
docker compose run --rm web poetry run python -m cli.cli register
docker compose run --rm web poetry run python -m cli.cli login
docker compose run --rm web poetry run python -m cli.cli logout
```

---

## Testing

The project includes test coverage for Django views, models, forms, and URLs using `pytest`.

To run all Django tests:

```bash
make docker-test-django
```

To run locally without Docker:

```bash
make pytest-local
```

---

### ⚠️ CLI Tests Notice

CLI tests were attempted but removed due to PostgreSQL transactional testing limitations.  
Testing CLI commands inside the pytest environment with a persistent Postgres connection can cause errors and data inconsistency.

**However, all CLI commands were tested manually and function as intended.**

Optional manual test script can be used:
```bash
sh manual_cli_tests.sh
```
*(script provided in the repo)*

---

## Development Timeline

**0.1.0**

- Project planning and setup.
- Created models for `Book` and `ReadingSession`.
- Django admin integration.
- Initial migrations and superuser creation.

**0.2.0**

- Implemented Typer CLI commands.
- Integrated CLI with Django ORM.
- Added commands: `add`, `list`, `mark-read`, and `log-reading`.

**0.2.1**

- Created Django forms and views.
- Added templates for listing, detail, create, update, and delete.
- Connected forms and models.
- User registration & login added.

**0.2.2**

- Added pytest test coverage for Django components.
- Integrated logging across CLI, views, forms, and models.
- Containerised the project with Docker and Compose.
- Added structured Makefile shortcuts.
- CLI tests excluded due to Postgres transactional behavior.

**1.0.0**

- Initial stable release.