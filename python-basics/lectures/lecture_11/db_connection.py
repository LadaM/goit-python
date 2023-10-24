class DatabaseConnection:

    # to implement Singleton pattern
    isinstance = None

    # is called before __init__
    def __new__(cls, *args):
        if cls.isinstance is None:
            cls.isinstance = super(DatabaseConnection, cls).__new__(cls)
        return cls.isinstance

    def __init__(self, database_name):
        self.database_name = database_name


db1 = DatabaseConnection("users")
db2 = DatabaseConnection("users")
