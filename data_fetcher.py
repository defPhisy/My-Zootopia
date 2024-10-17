import requests


API_KEY = "tXh7qQhJw4VRGSeKr97JRg==lg5I8cRuDZAbXgiT"


def get_animals():
    animal = ask_for_animal()
    return fetch_animals(animal)


def ask_for_animal():
    return input("Animal: ")


def fetch_animals(animal: str):
    url = "https://api.api-ninjas.com/v1/animals"
    headers = {"X-Api-Key": API_KEY, "name": animal}
    response = requests.get(url, headers)
    if not response:
        return "No animals found"
    elif response.status_code == requests.codes.ok:
        return response
    else:
        return "Error:", response.status_code, response.text
