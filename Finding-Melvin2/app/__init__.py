from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='/static')
    app.config['SECRET_KEY'] = 'finding-melvin-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finding_melvin.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    CORS(app)

    from app.blueprints.game import game_bp
    app.register_blueprint(game_bp)

    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    with app.app_context():
        db.create_all()

    return app

