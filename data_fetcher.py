import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_animals():
    animal = ask_for_animal()
    return fetch_animals(animal)


def ask_for_animal():
    return input("Enter a name of an animal: ")


def fetch_animals(animal: str):
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
