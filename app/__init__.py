from flask import Flask
from app import views
from flask_bootstrap import Bootstrap 
from .config import DevConfig


# # initializing application



app = Flask(__name__, __name__,instance_relative_config = True)
        

# # Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")

# Initializing Flask Extensions
bootstrap = Bootstrap(app)