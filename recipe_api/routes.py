from flask import Flask, request
from recipe_api import db, app
from recipe_api.models import Recipe
import pytest


@app.route('/')
def hello_world():
    return 'WHATSUPPP NIGGA'


@app.route('/recipes', methods=['POST'])
def create_recipe():
    recipe_name = request.json['recipe_name']
    Ingrediants = request.json['Ingrediants']
    recipe = Recipe(recipe_name, Ingrediants)
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
    recipe.recipe_name = request.json['recipe_name']
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
        'recipe_name': recipe.recipe_name,
        'recipe_favorite': recipe.favorite,
        'Ingrediants':  recipe.Ingrediants,
        'Steps': recipe.steps,
        'created_at': recipe.created_at
    }

