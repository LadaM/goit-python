import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['email', 'phone', 'name', 'favorite'])
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)


def read_contacts_from_file(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        return [contact for contact in reader]


if __name__ == "__main__":
    filename = "contatcts.csv"
    contacts = [{
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }]

    write_contacts_to_file(filename, contacts)
    print(read_contacts_from_file(filename))
