
import os

class Configuration:
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'EwORLeuMAS503519MANaYDAmAKHsUNaIAS'

class DevelopmentConfiguration(Configuration):

    DEBUG = True

    MAIL_SERVER = os.environ.get('FLASK_MAIL_SERVER_DEV')

    MAIL_PORT = os.environ.get('FLASK_MAIL_SERVER_DEV')

    MAIL_USE_TLS = True

    MAIL_USE_SSL = False

    MAIL_USERNAME = os.environ.get('FLASK_MAIL_USERNAME_DEV')

    MAIL_PASSWORD = os.environ.get('FLASK_MAIL_PASSWORD_DEV')

    DATABASE_URI = os.environ.get('FLASK_DATABASE_URI_DEV')

class TestConfiguration(Configuration):
    TEST = True

    MAIL_SERVER = os.environ.get('FLASK_MAIL_SERVER_TEST')

    MAIL_PORT = os.environ.get('FLASK_MAIL_SERVER_TEST')

    MAIL_USE_TLS = True

    MAIL_USE_SSL = False

    MAIL_USERNAME = os.environ.get('FLASK_MAIL_USERNAME_TEST')

    MAIL_PASSWORD = os.environ.get('FLASK_MAIL_PASSWORD_TEST')

    DATABASE_URI = os.environ.get('FLASK_DATABASE_URI_TEST')

class ProductionConfiguration(Configuration):

    PRODUCTION = True

    MAIL_SERVER = os.environ.get('FLASK_MAIL_SERVER_PRODUCTION')

    MAIL_PORT = os.environ.get('FLASK_MAIL_SERVER_PRODUCTION')

    MAIL_USE_TLS = True

    MAIL_USE_SSL = False

    MAIL_USERNAME = os.environ.get('FLASK_MAIL_USERNAME_PRODUCTION')

    MAIL_PASSWORD = os.environ.get('FLASK_MAIL_PASSWORD_PRODUCTION')

    DATABASE_URI = os.environ.get('FLASK_DATABASE_URI_PRODUCTION')

configuration = {
    'development': DevelopmentConfiguration,
    'test': TestConfiguration,
    'production': ProductionConfiguration,
    'default': DevelopmentConfiguration
}
