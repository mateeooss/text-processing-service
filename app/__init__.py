from flask import Flask

from app.controllers.ner_controller import ner_controller


def create_app():
    app = Flask(__name__)

    # Registra os controllers com o Flask
    app.register_blueprint(ner_controller)

    return app
