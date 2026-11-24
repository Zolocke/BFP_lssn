# Backend Flask Project

A Flask API for BE106 with a health check and user registration.

## Setup

```bash
# create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# copy env file at the project root
cp .env.example .env
```

Edit `.env` with the values below (local defaults work as-is for development).

## Run

```bash
export FLASK_APP=app
flask db upgrade
flask run
```

`FLASK_APP=app` tells Flask to load the `app` package (it uses `create_app()` inside). Run migrations before the first start so the database schema exists.

## Environment variables

Set these in `.env` at the project root:

```
FLASK_CONFIG=development
JWT_SECRET=your-secret-key-here
DATABASE_URL=sqlite:///dev.db
```

For production, set a real `DATABASE_URL` (for example Postgres) instead of SQLite.

## API

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/` | Liveness (`ok`) |
| GET | `/health` | Health JSON |
| POST | `/users/register` | Create user |

### `POST /users/register`

JSON body:

- `username` (required)
- `password` (required)
- `display_name` (optional)

Success (`201`):

```json
{ "id": 1, "username": "alice" }
```

Errors: `400` validation, `409` username taken.

## Testing

With the server running, use [`api_testing.http`](api_testing.http) (VS Code / Cursor REST Client) or curl against `http://127.0.0.1:5000`.

## Database migrations

Flask-Migrate is set up. The initial migration creates the `users` table.

```bash
# apply migrations
flask db upgrade
```

After model changes:

```bash
flask db migrate -m "describe your change"
flask db upgrade
```

## See also

- [`HTTP_STATUS_CODES.md`](HTTP_STATUS_CODES.md) — quick reference for API response codes
