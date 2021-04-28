from flask import Flask
from .config import DevConfig
from app import views
from app import error 
from flask_bootstrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate






# # initializing application



app = Flask(__name__, __name__,instance_relative_config = True)
        

# # Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")

# Initializing Flask Extensions
bootstrap = Bootstrap(app)