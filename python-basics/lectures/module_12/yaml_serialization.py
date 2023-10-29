import yaml
from user_data import users

serialized_users = yaml.dump(users)
print(serialized_users)

deserialized_users = yaml.load(serialized_users, yaml.Loader)
print(deserialized_users)

for user in deserialized_users:
    if user.is_active:
        print(user)