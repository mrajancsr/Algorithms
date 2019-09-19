class Reverse:
    """class that prints a list in reverse"""
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self 

    def __next__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration("out of index")
        return self.data[self.index]

chk = [34,978,42,1000,200]
bek = Reverse(chk)
print(chk)
print(list(bek))