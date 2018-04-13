from flask import Flask
from flask_migrate import Migrate
from app.models import db
from config import configs
from flask_login import LoginManager


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    db.init_app(app)
    Migrate(app,db)
    login_manager=LoginManager()
    login_manager.init_app(app)
    @login_manager.user_loader
    def user_loader(id):
        pass
        # return User.query.get(id)
    login_manager.login_view='home.login'

def register_blueprints(app):
    from .main import home
    from .main import admin
    app.register_blueprint(home)
    app.register_blueprint(admin)


from app import models