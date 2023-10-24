class RepetetiveIterator:
    def __init__(self, seq, count) -> None:
        self.seq = seq
        self.count = count
        self.loop = 0
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.loop >= self.count:
            raise StopIteration
        else: 
            val = self.seq[self.index]
            self.index += 1
            if len(self.seq) == self.index:
                self.index = 0
                self.loop += 1 # measures the number of times looped over the seq
            return val
         
seq = ['a', 'b', 'c']
iter = RepetetiveIterator(seq, 2)
print([item for item in iter])