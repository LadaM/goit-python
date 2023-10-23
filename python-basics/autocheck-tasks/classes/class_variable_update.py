class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts
        
    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append({
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite,
        })
        Contacts.increase_id()   
                
    @classmethod
    def increase_id(cls):
        cls.current_id += 1

# Another implementation -- is it really better?
class Contacts1:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts1.current_id += 1