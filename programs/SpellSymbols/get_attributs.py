from writer import load_attribute
import json


attributes = {
    "are_types": load_attribute("Attributes/area_types.txt"),
    "damage_types": load_attribute("Attributes/damage_types.txt"),
    "durations": load_attribute("Attributes/duration.txt"),
    "levels": load_attribute("Attributes/levels.txt"),
    "ranges": load_attribute("Attributes/range.txt"),
    "schools": load_attribute("Attributes/school.txt")
}

raw_data = json.dumps(attributes, indent=4)
with open("attributes.json", "w") as file:
    file.write(raw_data)
