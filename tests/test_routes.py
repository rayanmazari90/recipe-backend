from recipe_api import app
import pytest


def test_get_recipes(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/recipes')
    assert response.status_code == 200


def test_non_existing_path():
    """
    GIVEN a Flask application
    WHEN the '/non_existing_path' page is requested (GET)
    THEN check the response is valid with response code(404)
    """
    with app.test_client() as client:
        response = client.get('/non_existing_path')
        assert response.status_code == 404


def test_create_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post(
        '/recipes', json={  
                            'name': 'Paella',
                            'ingredients': 'rice, and others',
                            'steps':'put in the water,cook', 
                            'rating':5, 
                            'favourites': "true"
                        })
    assert response.status_code == 200


def test_get_account_by_id(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get(
        '/recipes/1')
    assert response.status_code == 200


def test_update(testing_client):
    response = testing_client.put('/recipes/1',json={   'name': 'Paella',
                                                        'ingredients': 'rice, and others',
                                                        'steps':'put in the water,cook', 
                                                        'rating':5, 
                                                        'favourites': "false"
                                                     })
    assert response.status_code == 200

def test_update_failing(testing_client):
    response = testing_client.put('/recipes/1',json={   'name': 'Paella',
                                                        'ingredients': 'rice, and others',
                                                        'steps':'put in the water,cook', 
                                                        'rating':5, 
                                                        'favourites': "false",
                                                        'NONPARAMETER':"FAIL"
                                                     })
    assert response.status_code == 500

def test_delete(testing_client):
    response = testing_client.delete('/recipes/1')
    assert response.status_code == 200
