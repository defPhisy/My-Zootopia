from data_fetcher import get_animals


def main():
    # read json and html template
    json_data = get_animals()

    with open("animals_template.html", "r") as handle:
        html_template = handle.read()

    animal_specs = get_animal_specs(json_data)

    # replace placeholder in html template with new animal specs
    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_specs)

    # write modified html template to new file
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


if __name__ == "__main__":
    main()
