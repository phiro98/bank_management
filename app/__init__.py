from flask import Flask
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from config import Config

mongo = PyMongo()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    jwt.init_app(app)

    from app.views.customer import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.views.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from app.views.banker import banker as banker_blueprint
    app.register_blueprint(banker_blueprint, url_prefix='/banker')

    return app
