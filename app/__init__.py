from flask import Flask
from flask_migrate import Migrate
from app.models import db, User
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
        return User.query.get(id)

    login_manager.login_view='home.login'

def register_blueprints(app):
    from .main import home,admin,company,job
    app.register_blueprint(home)
    app.register_blueprint(admin)
    app.register_blueprint(company)
    app.register_blueprint(job)


from app import models