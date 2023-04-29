"""file for functions to handle pet data"""

import os
import requests
from random import choice
from models import Pet
from app import auth_token

CLIENT_ID = os.environ.get("PETFINDER_API_KEY")
CLIENT_SECRET = os.environ.get("PETFINDER_API_SECRET")
PETFINDER_BASE_URL = "https://api.petfinder.com/v2/animals"
PETFINDER_TOKEN_URL = "https://api.petfinder.com/v2/oauth2/token"


def update_auth_token_string():
    """Retrieve auth token using client id and secret key"""

    resp = requests.get(PETFINDER_TOKEN_URL,
        params={"grant_type": "client_credentials",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET
                })
    return resp.json().get("access_token")


def get_pet_data():
    """return single pet data"""

    resp = requests.get(PETFINDER_BASE_URL,
        params={"limit": "100"},
        headers={"Authorization": f"Bearer {auth_token}"}
        )
    pet_finder_pet =choice(resp.json().get("animals"))

    pet = Pet(pet_finder_pet)
    pet.photo_url = pet_finder_pet.photos[0].small

    return pet
