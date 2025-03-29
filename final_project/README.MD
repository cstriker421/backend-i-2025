
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
- Admin interface for managing models.
- Book form for data entry.
- Minimal HTML templates.

### Typer CLI

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
make book-cli
```

Available commands:

```bash
make book-add               # Add a new book (edit Makefile variables to change default values)
make book-list              # List all books
make book-summary           # Show reading summary
make book-mark-read         # Mark a book as read (edit ID in Makefile)
make book-log               # Log a reading session (edit ID, MINUTES, NOTES in Makefile)
make book-cli-verbose       # Run CLI with verbose logging
```

You can also use Docker manually:

```bash
docker compose run --rm web poetry run python -m cli.cli --help
```

---

## Testing

The project includes test coverage for Django views, models, forms, URLs, and CLI commands using `pytest`.

To run all tests:

```bash
make docker-test
```

To run only Django tests:

```bash
make docker-test-django
```

To run only CLI tests:

```bash
make docker-test-cli
```

To run locally without Docker:

```bash
make pytest-local
```

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

**0.2.2**

- Added pytest test coverage for both for CLI and Django components.
- Integrated logging across CLI, views, forms, and models.
- Containerised the project with Docker and Compose.
- Added structured Makefile shortcuts.
- Final code cleanup and documentation.

**1.0.0**

- Initial stable release.