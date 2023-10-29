import pickle
import json


def write_contacts_to_json_file(filename, contacts):
    with open(filename, 'w') as file:
        json.dump({"contacts": contacts}, file)


def read_contacts_from_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data.get("contacts")


def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as f:
        f.write(pickle.dumps(contacts))


def read_contacts_from_file(filename):
    with open(filename, 'rb') as f:
        return pickle.loads(f.read())


if __name__ == "__main__":
    file_name = "pickle_dump.txt"
    contacts = [{
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }]
    write_contacts_to_file(file_name, contacts)
    print(read_contacts_from_file(file_name))

    json_file = "json_dump.json"
    write_contacts_to_json_file(json_file, contacts)
    print(read_contacts_from_json_file(json_file))
