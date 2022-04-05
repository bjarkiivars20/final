class Test1:
    def __init__(self, data):
        data = data
    
    def __eq__(self, other):
        if other == None:
            return False
        else:
            return self.data == other.data


t1 = Test1(4)
t2 = None

print(t1 == t2)