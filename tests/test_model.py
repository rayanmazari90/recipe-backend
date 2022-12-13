from recipe_api.models import Recipe
import pytest


def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    recipe = Recipe('Tacos', 'step1, step2, step3','eggs ,butter',5, True)
    assert recipe.name == 'Tacos'
    assert recipe.steps == 'step1, step2, step3'
    assert recipe.ingredients == 'eggs ,butter'
    assert recipe.rating == 5
    assert recipe.favourites == True
