import requests
import os
from dotenv import load_dotenv

load_dotenv()

HEADERS = {
    'X-Api-Key': os.getenv('API_KEY')
}


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    """
    url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    animals_res = requests.get(url, headers=HEADERS).json()
    return animals_res