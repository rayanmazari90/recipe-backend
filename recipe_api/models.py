from recipe_api import db
from datetime import datetime
import string, random

class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ingredients = db.Column(db.String(255))
    name = db.Column(db.String(255))
    steps = db.Column(db.String(255))
    favourites = db.Column(db.Boolean, default=False)
    rating = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Event %r>' % self.name+"ID : "

    def __init__(self, name,steps, ingredients):
        self.ingredients = ingredients
        self.steps= steps
        self.name = name
        self.favourites = False
        self.rating = 5


"""class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    Ingredients= db.Column(db.String(300), nullable=False)
    steps= db.Column(db.String(250), nullable=False, default ="step1")
    rating = db.Column(db.Integer,nullable=False, default =5)
    favorite= db.Column(db.Boolean,nullable=False, default = 0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        return '<Event %r>' % self.name+"ID : "+ self.id

    def __init__(self, name,Ingrediants, steps):
        self.name = name
        self.Ingrediants = Ingrediants
        self.favorite = 0 
        self.steps= steps
        self.rating=5
"""