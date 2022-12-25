import json

def retrieve_json(filename="../user_data.json"):
    with open(filename) as f:
        json_object = json.load(f)
    return json_object

def add_update_user(username, password, filename="../user_data.json"):
    data = retrieve_json(filename)
    data[username] = password
    json_object = json.dumps(data)

    with open(filename, "w") as f:
        f.write(json_object)
    return True
