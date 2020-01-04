import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'Recipe_Book'
app.config["MONGO_URI"] = 'mongodb+srv://rootbeer:r00tb33r@myfirstcluster-utt5o.mongodb.net/Recipe_Book?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipe():
    return render_template("recipes.html", recipes=mongo.db.Recipes.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
    