from datetime import datetime


class User:
    def __init__(self, name, surname, birth_date, is_active, nickname):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.is_active = is_active
        self.nickname = nickname
        self.__saved = None
        self.__restored = None

    @property
    def saved(self):
        return self.__saved

    @property
    def restored(self):
        return self.__restored

    def __str__(self):
        return f"{self.name} {self.surname} ({self.nickname}) - Birth Date: {self.birth_date}, Active: {self.is_active}"

    def __repr__(self) -> str:
        return f"name={self.name} surname={self.surname} nick={self.nickname} birthdate={self.birth_date} isactive={self.is_active} saved={self.saved} restored={self.restored}"

    # pickle will use this method when serializing the object
    def __getstate__(self) -> object:
        self.__saved = datetime.now()
        state = self.__dict__
        return state

    # will be called when deserializing the object
    def __setstate__(self, state):
        self.__dict__ = state
        self.__restored = datetime.now()
