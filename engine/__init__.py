from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, jsonify, render_template as cast, redirect, url_for 
from backend import config
# package name for config
pckg = __name__.split(".")

# main application / flask-app
app = Flask(pckg[0], template_folder="../frontend/views", static_folder="../frontend/assets")
app.config.from_object(config.Config)

# universal database sqlite-format
db = SQLAlchemy(app)