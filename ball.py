import turtle
import math
turtle.penup()
turtle.ht()
class ball():
    def __init__(self, x, y, typeBall):
        self.x = x
        self.oldX = x
        self.y = y
        self.oldY = y
        self.typeBall = typeBall
        self.frame = 1
        self.imgAddr = ("./Balls/ball"+str(self.typeBall)\
                    +str(self.frame)+".gif")
        self.direction = 0
        self.stampId = ""
        self.populateTable()  
    def populateTable(self):
        turtle.goto(self.x,self.y)
        turtle.shape("./Balls/ball"+str(self.typeBall)\
                    +str(self.frame)+".gif")
        self.stampId = turtle.stamp()
        
    def deleteBall(self):
        turtle.clearstamp(self.stampId)

    def getDirection(self):
        return self.direction
    
    def setDirection(self,direction):
        self.direction = direction
        
    def setCoordinates(self,vector):
        self.x = (vector[0])
        self.y = (vector[1])
        self.setOldCoordinates()
        
    def getCoordinates(self):
        return (self.x,self.y)
    
    def setOldCoordinates(self):
        if(self.updateFrame() == True):
            self.oldX = self.x
            self.oldY = self.y
            
    def getData(self):
        return [(self.x,self.y),\
                self.typeBall,self.frame]

    def updateFrame(self):
        x1 = self.x
        x2 = self.oldX
        y1 = self.y
        y2 = self.oldY
        if(x2 > x1):
            temporary = x1
            x1 = x2
            x2 = temporary
        if(y2 > y1):
            temporary = y1
            y1 = y2
            y2 = temporary
        if(((x1-x2)>15) or((y1-y2)>15)):
            if(self.frame==3):
                self.frame=1
            else:
                self.frame+=1
            return True
        return False
            
    def stampBall(self):
        self.setCoordinates(turtle.pos())
        self.collisionWTable()
        

# Parameters ->((x,y),typeBall,frame)       
    def stampBallScene(self,passedData):
        coordinate = passedData[0]
        typeBall = passedData[1]
        frame = passedData[2]
        turtle.shape("./Balls/ball"+str(typeBall)\
                    +str(frame)+".gif")
        turtle.setpos(coordinate)
        turtle.stamp()
        
    def edgeBounce(self,modifier):
        if(modifier == True):
            turtle.seth(self.direction)
            turtle.seth(180-turtle.heading())
            self.direction = turtle.heading()
        else:
            turtle.seth(self.direction)
            turtle.seth(turtle.heading()*-1)
            self.direction = turtle.heading()


#Currently only focuses on diagonal strikes
#Needs solution
    def ballBounce(self,deflection):
        angleDiff = self.direction - deflection
        if((angleDiff)>0):
            newDirection = 30
        else:
            newDirection = -30
        turtle.setheading(self.direction+newDirection)
        self.direction = turtle.heading()

    def collisionWBall(self,ball2):
        x1 = self.x
        x2 = ball2.x
        if(x2 > x1):
            temporary = x1
            x1 = x2
            x2 = temporary
        if(-30<(x1 - x2)<30):
            y1 = self.y
            y2 = ball2.y
            if(y2 > y1):
                temporary = y1
                y1 = y2
                y2 = temporary
            if(-30<(y1 - y2)<30):
                selfBorder = self.getBallBorder()
                ball2Border = ball2.getBallBorder()
                for each in selfBorder:
                    if(each in ball2Border):
                        if(self.x<ball2.x):
                            sectorHit = "L"
                            selfHit = "R"
                        else:
                            sectorHit = "R"
                            selfHit = "L"
                        if(self.y<ball2.y):
                            sectorHit+= "B"
                            selfHit = "T"
                        else:
                            sectorHit+="T"
                            selfHit = "B"
                        deflection = ball2.getDeflection(each[0],sectorHit)
                        ball2.direction = deflection
                        self.ballBounce(deflection)
                        return True
        return False
    
    def getDeflection(self, xCollision,sectorHit):
        xCollision-=self.x     
        if(sectorHit == "LT"):
            xCollision*=-1
            radian = math.acos(xCollision/16)
            angle = 90-(radian/0.0174532925)
            angle+=270
            return angle
        if(sectorHit == "RT"):
            radian = math.acos(xCollision/16)
            angle = radian/0.0174532925
            angle+=180
            return angle
        if(sectorHit == "RB"):
            radian = math.acos(xCollision/16)
            angle = 90-(radian/0.0174532925)
            angle+=90
            return angle
        if(sectorHit == "LB"):
            xCollision*=-1
            radian = math.acos(xCollision/16)
            angle = radian/0.0174532925
            return angle
        return 180 
    
    def collisionWTable(self):
        if((self.x>165)or(self.x<-165)):
            if((self.y>16)or(self.y<-16)):
                self.edgeBounce(True)
        if((self.y>330)or(self.y<-330)):
            self.edgeBounce(False)

    def collisionWPocket(self):
        if((self.x<-160)):
            if(self.y>315):
                return True
        if((self.x>160)):
            if(self.y>315):
                return True
        if((self.x<-160)):
            if(self.y<-315):
                return True
        if((self.x>160)):
            if(self.y<-315):
                return True
        if(self.x<-165):
            if((self.y>-16)and(self.y<16)):
                return True
        if(self.x>165):
            if((self.y>-16)and(self.y<16)):
                return True
        return False
    
    
    def getBallBorder(self):
        ballBorder = list()
        for x in range(-15,16):
            y = math.sqrt(16**2-(x)**2)
            ballBorder.append((int(self.x+x),int(self.y+y)))
            if(-15<(x)<15):
                ballBorder.append((int(self.x+x),int(self.y+(-y))))
        return ballBorder
            
