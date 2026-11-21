# Backend Flask Project

A Flask API for BE106.

## Setup:

```bash
# create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, then fill in the values below.

### Run the app:

```bash
export FLASK_APP=app
flask run
```

`FLASK_APP=app` tells Flask to load the `app` package (it uses `create_app()` inside).

## Environment variables:

Set these in `.env`:

```
FLASK_CONFIG=development
JWT_SECRET=your-secret-key-here
DATABASE_URL=sqlite:///dev.db
```

## Database migrations:

Flask-Migrate is set up, but there are no migrations yet.
