import json


def main():
    # read json and html template
    with open("animals_data.json", "r") as handle:
        json_data = json.loads(handle.read())

    with open("animals_template.html", "r") as handle:
        html_template = handle.read()

    animal_specs = get_animal_specs(json_data)

    # replace placeholder in html template with new animal specs
    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_specs)

    # write modified html template to new file
    with open("animals.html", "w") as handle:
        handle.write(new_html)


def get_animal_specs(json: dict) -> str:
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
    output += "<p class='card__text'>\n"
    output += f"<strong>Location:</strong> {location}<br/>\n"

    if animal_type:
        output += f"<strong>Type:</strong> {animal_type}<br/>\n"

    output += f"<strong>Diet:</strong> {diet}<br/></p></li>"

    return output


if __name__ == "__main__":
    main()
