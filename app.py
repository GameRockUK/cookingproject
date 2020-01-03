import os
from flask import Flask
from flask_pymongo import PyMongo
from bason.objectid import ObjectID

app = Flask(__name__)