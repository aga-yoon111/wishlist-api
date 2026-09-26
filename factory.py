from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from spectree import SecurityScheme, SpecTree


from config import Config

db = SQLAlchemy()
migrate = Migrate()

api = SpecTree(
    "flask",
    title="Wishlist API",
    version="v.1.0",
    path="docs",

)


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)
    from models import WishlistItem
    from controllers import wish_controller
    app.register_blueprint(wish_controller)

    api.register(app)

    return app
