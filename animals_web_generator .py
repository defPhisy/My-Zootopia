import json

with open("animals_data.json", "r") as handle:
    data = json.loads(handle.read())


# Name: American Foxhound
# Diet: Omnivore
# Location: North-America
# Type: Hound
for animal in data:
    name = animal["name"]
    diet = animal["characteristics"]["diet"]
    location = animal["locations"][0]
    animal_type = animal["characteristics"].get("type")
    print("Name:", name)
    print("Diet:", diet)
    print("Location:", location)
    if animal_type:
        print("Type:", animal_type)
    print("-------------")
