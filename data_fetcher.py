"""Fetches data for a specified animal from an external API.

This module allows the user to search for animals by name and retrieve
associated data, including species details and characteristics,
from an external animal API.
"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_animals() -> tuple:
    """Prompts the user for an animal name and fetches data about the animal.

    Returns:
        tuple: Contains the JSON response data and an informational or error message.
    """
    animal = ask_for_animal()
    return fetch_animals(animal)


def ask_for_animal() -> str:
    """Prompts the user to input the name of an animal.

    Returns:
        str: The name of the animal entered by the user.
    """

    return input("Enter a name of an animal: ")


def fetch_animals(animal: str) -> tuple:
    """Fetches data for a specified animal from the API.

    Args:
        animal (str): The name of the animal to search for.

    Returns:
        tuple: A tuple containing the JSON response data
        (or an empty string if no data is found)
        and an informational or error message.
    """

    url = "https://api.api-ninjas.com/v1/animals"
    headers = {"X-Api-Key": API_KEY, "name": animal}
    response = requests.get(url, headers)
    if not response.json():
        data = ""
        message = f"No animals found with '{animal}'"
    elif response.status_code == requests.codes.ok:
        data = response.json()
        message = response.status_code
    else:
        data = ""
        message = "Error:", response.status_code, response.text

    return data, message
