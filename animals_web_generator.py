from data_fetcher import get_animals
import json


def main():
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


def save_file(new_html):
    with open("animals.html", "w") as handle:
        try:
            handle.write(new_html)
        except Exception as error:
            print(error)
        else:
            print(
                "Website was successfully generated to the file animals.html."
            )


def get_animal_specs(json) -> str:
    output = ""
    for animal in json:
        name = animal["name"]
        diet = animal["characteristics"]["diet"]
        location = animal["locations"][0]
        animal_type = animal["characteristics"].get("type")

        output += get_html_serialization(name, diet, location, animal_type)

    return output


def get_html_serialization(name, diet, location, animal_type):
    output = "<li class='cards__item'>\n"
    output += f"<div class='card__title'>{name}</div>\n"
    output += "<div class='card__text'>\n"
    output += "<ul>\n"
    output += f"<li><strong>Location:</strong> {location}</li>\n"

    if animal_type:
        output += f"<li><strong>Type:</strong> {animal_type}</li>\n"

    output += f"<li><strong>Diet:</strong> {diet}</li></ul></div></li>"

    return output


def get_html_message(message: str) -> str:
    if "Error" in message[0]:
        output = json.loads(message[-1])
        output = output["error"].capitalize()
    else:
        output = message

    return f"<h2>{output}</h2>"


if __name__ == "__main__":
    main()
