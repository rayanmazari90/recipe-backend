from flask import Flask, request, jsonify
from recipe_api import db, app
from recipe_api.models import Recipe
import pytest
from flask_cors import CORS
import sys



CORS(app)


@app.route('/', methods=["GET"])
def hello_world():
    return 'HELLO DEAR CUSTOMER, WELCOME TO THE NEW COLABORATIVE PLATFORM FOR RECIPES'

@app.route('/recipes', methods=['POST'])
def create_recipe():
    print("hello",request.json)
    name = request.json["name"]
    ingredients = request.json["ingredients"]
    steps = request.json["steps"]
    rating = request.json["rating"]
    if request.json["favourites"].str.lower()== "true":
        favourites = True
    else:
        favourites = False

    recipe = Recipe(name, ingredients, steps, rating, favourites)
    db.session.add(recipe)
    db.session.commit()
    return format_recipes(recipe)


@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return {'recipes': [format_recipes(recipe) for recipe in recipes]}

#
@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    return format_recipes(recipe)

#
@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipes(id):
    recipe = Recipe.query.get(id)
    recipe.name = request.json['name']
    recipe.ingredients = request.json['ingredients']
    recipe.steps = request.json['steps']
    recipe.rating = request.json['rating']
    db.session.commit()
    return format_recipes(recipe)
#
@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipes(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return format_recipes(recipe)

def format_recipes(recipe):
    return {
        'id': recipe.id,
        'name': recipe.name,
        'favourites': recipe.favourites,
        'ingredients':  recipe.ingredients,
        'steps': recipe.steps,
        'date_created': recipe.date_created,
        'rating': recipe.rating
    }
