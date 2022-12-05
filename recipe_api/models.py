from recipe_api import db
from datetime import datetime
import string, random



class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(32), nullable=False)
    favorite= db.Column(db.Bool, nullable=False, default = False)
    description= db.Column(db.String(250), ullable=False, default ="")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Event %r>' % self.recipe_name+"ID : "+ self.id

    def __init__(self, recipe_name,description):
        self.recipe_name = recipe_name
        self.desciption = description
        self.favorite = 0 