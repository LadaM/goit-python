import pickle


class Reader:
    def __init__(self, file):
        self.file = file
        self.fh = open(self.file)
        self.position = 0

    def close(self):
        self.fh.close()

    def read(self, size=1):
        data = self.fh.read(size)
        self.position = self.fh.tell()
        return data

    # picle will call this method when serializing the Reader object
    def __getstate__(self):
        attributes = {**self.__dict__}
        attributes['fh'] = None # files aren't serializable
        return attributes

    # this method will be called when Reader deserealizes
    def __setstate__(self, value):
        self.__dict__ = value
        self.fh = open(value['file'])
        self.fh.seek(value['position'])