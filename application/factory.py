from flask import Flask
from  application.api.mylocal import mylocal

def create_app():
    app = Flask(__name__)
    app.register_blueprint(mylocal.bp)
    return app
