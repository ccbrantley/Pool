class scene:
    def __init__(self):
        self.objects = list()
        self.counter = 0
        
    def getData(self):
        return self.objects
    
    def appendData(self, curObj):
        self.objects.append(curObj.getData())
    
    def getCounter(self):
        return self.colunter
    
    def setCounter(self,counter):
        self.counter = counter

    def modifyCounter(self,x):
        self.counter+= x
        
    def printData(self):
        print("#######START#######")
        for each in self.objects:
            print(each)
        print("#########END##########")
