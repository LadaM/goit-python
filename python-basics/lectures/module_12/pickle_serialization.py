import pickle
from user_data import users

data = {"my key": 123}
byte_data = pickle.dumps(data) # obj -> bytes

print(byte_data)

restored_data = pickle.loads(byte_data)
print(restored_data)

serialized_users = pickle.dumps(users)
print(serialized_users)

deserialized_users = pickle.loads(serialized_users)
print(deserialized_users)
