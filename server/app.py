from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from server.config import Config
from flask_jwt_extended import JWTManager

migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from server.models import db
    from server.models.user import User
    from server.models.guest import Guest
    from server.models.episode import Episode
    from server.models.appearance import Appearance
    
    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)

   
    return app 