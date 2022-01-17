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

    SQLALCHEMY_DATABASE_URI = "postgres://qpnqxwnvtfdtrd:2081c16f16ececec2f344970b223797008c3f29d957ebe4c947781b2932fc9b9@ec2-54-208-139-247.compute-1.amazonaws.com:5432/d6nrchh98f5d3e"


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
