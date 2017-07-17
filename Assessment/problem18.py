class _list:
    def __init__(self):
        self.members = [] 

    def append(self,value):
        self.members.append(value)

    def delete(self,value):
        try:
            self.members.remove(value)
        except ValueError:
            print("given value is not present in the list")

    def display(self):
        print self.members


if __name__ == "__main__":

    l = _list()
    l.append(5)
    l.append(10)
    l.display()
    l.delete(7)
    l.delete(5)
    l.display()

    
