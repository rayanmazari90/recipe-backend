from flask import Flask, request, jsonify
from recipe_api import db, app
from recipe_api.models import Recipe
import pytest
from flask_cors import CORS
import sys



CORS(app)


@app.route('/', methods=["GET"])
def hello_world():
    return 'HELLO WORLD'

@app.route('/recipes', methods=['POST'])
def create_recipe():
    print("hello",request.json)
    name = request.json["name"]
    ingredients = request.json["ingredients"]
    steps = request.json["steps"]
    recipe = Recipe(name, ingredients, steps)
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
        'recipe_name': recipe.name,
        'recipe_favourites': recipe.favourites,
        'ingredients':  recipe.ingredients,
        'Steps': recipe.steps,
        'created_at': recipe.date_created
    }
