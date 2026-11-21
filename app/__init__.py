import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

from flask import Flask

from .config import DevelopmentConfig, ProductionConfig, TestingConfig
from .extensions import db, migrate


def create_app():
    config_name = os.getenv("FLASK_CONFIG", "development")
    config_map = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }
    instance_path = Path(__file__).resolve().parent / "instance"
    instance_path.mkdir(exist_ok=True)

    app = Flask(__name__, instance_path=str(instance_path))
    app.config.from_object(config_map[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
