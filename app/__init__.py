from flask import Flask
from flask_bootstrap import Bootstrap
from config import config

def create_app(config_name):
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(config[config_name])
    
    from .pypivot import pypivot as pypivot_blueprint
    app.register_blueprint(pypivot_blueprint)
    
    return app