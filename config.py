import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

basedir = os.path.abspath(os.path.dirname(__file__))    
class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tgtlse99'
    SQLALCHEMY_DATA_URL = os.environ.get('DEV_DATABASE_RUL') or 'sqlite:////' + os.path.join(basedir, 'data-dev.sqlite')
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATA_URL = os.environ.get('TEST_DATABASE_RUL') or 'sqlite:////' + os.path.join(basedir, 'data-test.sqlite')
    
class ProductionConfig(Config):
    SQLALCHEMY_DATA_URL = os.environ.get('DATABASE_RUL') or 'sqlite:////' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig

}