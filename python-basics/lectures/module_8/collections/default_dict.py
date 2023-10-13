from collections import defaultdict

# to provide a default value for the case when the key isn't in the dictionary
d = defaultdict() # accepts a callable parameter -> str, int, list or custom function without ()

def get_default_status():
    return "New"
    
users = defaultdict(get_default_status)
users[1] = "Validating"
users[5] = "Verified"
users[755] = "Deleted"
users[3] = "Inactive"

def get_user_status(user_id):
    users[user_id]

print(get_user_status(4)) # -> "New"