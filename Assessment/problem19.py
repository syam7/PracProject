class Temp:

    def getString(self,_string):
        self.string = _string

    def displayString(self):
        print self.string


if __name__=="__main__":

    object1 = Temp()

    string = "Shyam kumar"
    object1.getString(string)
    object1.displayString()
