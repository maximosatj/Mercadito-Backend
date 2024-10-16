from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
from app.config.database import db, migrate, FULL_URL_DB
from app.models import *
from flask_marshmallow import Marshmallow

ma = Marshmallow()

def create_app():
    app=Flask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #app.debug = True
    
    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.resources import home, client, product, product_brand
    app.register_blueprint(home, url_prefix="/api/v1")
    app.register_blueprint(client, url_prefix="/api/v1")
    app.register_blueprint(product, url_prefix="/api/v1")
    app.register_blueprint(product_brand, url_prefix="/api/v1")

    return app
    