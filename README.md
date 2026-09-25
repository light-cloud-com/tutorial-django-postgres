# tutorial-django-postgres

A small Django project used in the Light Cloud tutorial
[Django + PostgreSQL: migrations, static files and a live admin](https://blog.light-cloud.com/tutorials/deploy-django-with-postgres).

```mermaid
flowchart LR
  browser[Browser] -->|HTTPS| lc[Light Cloud edge]
  lc --> app[Django on gunicorn]
  app -->|DATABASE_URL| db[(PostgreSQL)]
  laptop[Your laptop] -->|manage.py migrate| db
```

Settings come from environment variables:

| Variable | Example |
|---|---|
| `SECRET_KEY` | a long random string |
| `ALLOWED_HOSTS` | `main-tutorial-django-postgres-yourworkspace.light-cloud.io` |
| `DATABASE_URL` | `postgresql://user:password@host:5432/db?sslmode=require` |
| `DEBUG` | `false` (default) |

## Run it locally

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Without `DATABASE_URL` it uses SQLite.
