import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    
    APP_TITLE = "Wishlist API"
    SQLALCHEMY_DATABASE_URI = (
            "sqlite:///" + os.path.join(basedir, "app.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False