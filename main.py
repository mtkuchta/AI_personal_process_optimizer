from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

db=SQLAlchemy()
login_manager=LoginManager()

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"]=os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"]=(
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )

    db.init_app(app)
    login_manager.init_app(app)


    return app

if __name__=="__main__":
    create_app()