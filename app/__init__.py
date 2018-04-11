from flask import Flask
from flask_migrate import Migrate
from app.models import db
from config import configs


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    db.init_app(app)
    Migrate(app,db)

def register_blueprints(app):
    from .main import home
    app.register_blueprint(home)


from app import models