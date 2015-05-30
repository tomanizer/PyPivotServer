from flask import Flask
from config import config
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    #Bootstrap(app)
    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    
    from .pypivot import pypivot as pypivot_blueprint
    app.register_blueprint(pypivot_blueprint)
    
    return app