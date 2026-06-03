from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Import et enregistrement des modules internes
    from app.routes import bp_routes
    from app.errors import register_errors

    app.register_blueprint(bp_routes)
    register_errors(app)

    return app

