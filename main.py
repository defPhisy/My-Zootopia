"""Small cli script to search for animals and list them in a simple html file."""

from data_fetcher import get_animals
import json


def main() -> None:
    # read json and html template
    with open("animals_template.html", "r") as handle:
        html_template = handle.read()

    json_data, message = get_animals()
    if not json_data:
        message = get_html_message(message)
        new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", message)

    else:
        animal_specs = get_animal_specs(json_data)
        # replace placeholder in html template with new animal specs
        new_html = html_template.replace(
            "__REPLACE_ANIMALS_INFO__", animal_specs
        )

    # write modified html template to new file
    save_file(new_html)


def save_file(new_html: str) -> None:
    """Writes generated HTML content to 'animals.html' in the root folder.

    Args:
        new_html (str): The HTML content to be written to the file.
    """

    with open("animals.html", "w") as handle:
        try:
            handle.write(new_html)
        except Exception as error:
            print(error)
        else:
            print(
                "Website was successfully generated to the file animals.html."
            )


def get_animal_specs(json: list) -> str:
    """Extracts animal data from JSON and converts it to an HTML format string.

    Args:
        json (list): A list of animal dictionaries with details such as name,
        diet, and location.

    Returns:
        str: HTML-formatted string containing animal details.
    """

    output = ""
    for animal in json:
        name = animal["name"]
        diet = animal["characteristics"]["diet"]
        location = animal["locations"][0]
        animal_type = animal["characteristics"].get("type")

        output += get_html_serialization(name, diet, location, animal_type)

    return output


def get_html_serialization(
    name: str, diet: str, location: str, animal_type: str
) -> str:
    """Formats provided animal details into an HTML list item structure.

    Args:
        name (str): The animal's name.
        diet (str): The animal's diet type.
        location (str): The location where the animal is found.
        animal_type (str): The type of animal, if available.

    Returns:
        str: HTML-formatted string with animal details as list items.
    """

    output = "<li class='cards__item'>\n"
    output += f"<div class='card__title'>{name}</div>\n"
    output += "<div class='card__text'>\n"
    output += "<ul>\n"
    output += f"<li><strong>Location:</strong> {location}</li>\n"

    if animal_type:
        output += f"<li><strong>Type:</strong> {animal_type}</li>\n"

    output += f"<li><strong>Diet:</strong> {diet}</li></ul></div></li>"

    return output


def get_html_message(message: str|list) -> str:
    """Formats an error or informational message from the API response for HTML display.
    
    Args:
        message (str or list): The API message detailing errors or information.
    
    Returns:
        str: HTML-formatted message for display in the template.
    """
    
    if "Error" in message[0]:
        output = json.loads(message[-1])
        output = output["error"].capitalize()
    else:
        output = message

    return f"<h2>{output}</h2>"


if __name__ == "__main__":
    main()
