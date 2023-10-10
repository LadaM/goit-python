from faker import Faker 

def get_mocked_user():
    fake = Faker()

    mock = {
        "name": fake.name(),
        "email": fake.email(),
        "city": fake.city(),
        "phone": fake.phone_number(),
    }

if(__name__) == "main": 
    user = get_mocked_user()
    print(user)