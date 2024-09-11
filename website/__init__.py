from flask import Flask
from flask_restful import Api
from .csapi import Weapon

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'askljflskadjfl;sdajfasdlf'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    api = Api(app)
    api.add_resource(Weapon, "/weapons", "/weapons/<string:weaponType>",
                     "/weapons/<string:weaponType>/<string:weaponName>")
    return app
