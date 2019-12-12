import json
with open("mywrittenfile.json", "w") as output:
    obj = {}
    obj["name"] = "Daniel"
    obj["occupation"] = "Software Developer"
    obj["dateOfBirth"] = "1988-05-26"
    output.write(json.dumps(obj))
