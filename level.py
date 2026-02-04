
class Level:
    def __init__(self,name,size,win):
        self.name = name
        self.size = size
        self.win = win

@classmethod
def classic(cls):
    return cls("Classic",3,3)

@classmethod
def advanced(cls):
    return cls("Advanced",4,4)
