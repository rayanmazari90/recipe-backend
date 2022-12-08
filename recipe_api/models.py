from recipe_api import db
from datetime import datetime
import string, random


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(32), nullable=False)
    Ingredients= db.Column(db.String(300), nullable=False)
    steps= db.Column(db.String(250), nullable=False, default ="")
    rating = db.Column(db.Integer, default =5)
    favorite= db.Column(db.Boolean, default = 0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        return '<Event %r>' % self.recipe_name+"ID : "+ self.id

    def __init__(self, recipe_name,Ingrediants, steps):
        self.recipe_name = recipe_name
        self.Ingrediants = Ingrediants
        self.favorite = 0 
        self.steps= steps
        self.rating=5