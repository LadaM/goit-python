from copy import copy, deepcopy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        return copy.copy(self)


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        copy_obj = Contacts(self.filename)
        copy_obj.contacts = copy(self.contacts)
        return copy_obj

    def __deepcopy__(self, memo):
        copy_obj = Contacts(self.filename)
        memo[id(copy_obj)] = copy_obj
        copy_obj.contacts = deepcopy(self.contacts)
        return copy_obj

if __name__ == "__main__":
    contacts = [
        Person(
            "Allen Raymond",
            "nulla.ante@vestibul.co.uk",
            "(992) 914-3792",
            False,
        ),
        Person(
            "Chaim Lewis",
            "dui.in@egetlacus.ca",
            "(294) 840-6685",
            False,
        ),
    ]
    persons = Contacts("user_class.dat", contacts)

    persons_copy = copy(persons)
    persons_deepcopy = deepcopy(persons)
    print(persons_copy.filename)
    print(persons_deepcopy.contacts)