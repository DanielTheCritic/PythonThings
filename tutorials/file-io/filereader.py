import json
with open("myfile.json", "r") as input:
    obj = json.load(input)
    print(obj["name"])
