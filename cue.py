import turtle
class cue():
    def __init__(self):
        self.stampId = ""
        self.angleFrame = 360
        self.imgAddr = ("./Sticks/stick"+str(self.angleFrame)+".gif")
        self.direction = self.getDirection()
        self.frameAdv = 5
    def populateTable(self,cueBall):
        self.stampPiece(cueBall.getX,cueBall.getY)
        
    def deleteCue(self):
        turtle.clearstamp(self.stampId)
        self.stampId = ""

    def stampCue(self,cueBall):
        turtle.shape(self.imgAddr)
        turtle.goto(cueBall.x,cueBall.y)
        self.deleteCue()
        self.stampId = turtle.stamp()
        turtle.update()
        
    def getDirection(self):
        turtle.seth((self.angleFrame)-90)
        return turtle.heading()
    
    def setFrameAdv(self):
        if(self.frameAdv == 1):
            self.frameAdv = 5
        else:
            self.frameAdv = 1
     
    def cueStickLeft(self,cueBall):
        self.updateFrame(1)
        self.stampCue(cueBall)
        turtle.update()
        
    def cueStickRight(self,cueBall):
        self.updateFrame(-1)
        self.stampCue(cueBall)
        turtle.update()
        
    def updateFrame(self, sequence):
        self.angleFrame+=(sequence*(self.frameAdv))
        if(self.angleFrame>360):
            self.angleFrame=1
        if(self.angleFrame<1):
            self.angleFrame=360
        self.imgAddr = ("./Sticks/stick"+str(self.angleFrame)+".gif")
       
        
        
