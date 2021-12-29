import os


class Config:
    SECRET_KEY ='hgfjhguaLMAirmhGvt'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


@staticmethod
def init_app(app):
    pass


class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://evance:0701003610sue@localhost/pitch2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    pass

config_options = {
        'development': DevConfig,
        'production': ProdConfig,
        'test': TestConfig
    }
