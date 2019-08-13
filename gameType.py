import ball
import turtle
class gameType():
    def __init__(self,gameType):
        self.allBalls = list()
        self.gameType = gameType
        self.gameBalls = list()
        self.setGameBalls()
        
        #0 -> 8Ball
        #1 -> 9Ball
        #2 -> Smaller Triangle
    def setGameBalls(self):
        ball1 = ball.ball(-60,-200,15)#15
        ball2 = ball.ball(-30,-200,11)#11
        ball3 = ball.ball(0,-200,4)#4
        ball4 = ball.ball(30,-200,13)#13
        ball5 = ball.ball(60,-200,12)#12
        ball6 = ball.ball(-45,-170,5)#5
        ball7 = ball.ball(-15,-170,7)#7
        ball8 = ball.ball(15,-170,14)#14
        ball9 = ball.ball(45,-170,3)#3
        ball10 = ball.ball(-30,-140,10)#10
        ball11 = ball.ball(0,-140,8)#8
        ball12 = ball.ball(30,-140,9)#9
        ball13 = ball.ball(-15,-110,6)#6
        ball14 = ball.ball(15,-110,2)#2
        ball15 = ball.ball(0,-80,1)#1
        self.allBalls = [ball1,ball2,ball3,\
                         ball4,ball5,ball6,ball7,ball8,\
                         ball9,ball10,ball11,ball12,ball13,\
                         ball14,ball15]
        
        if(self.gameType == 0):
            self.gameBalls=self.allBalls
            
        if(self.gameType == 1):
            self.gameBalls=[ball3,ball7,ball8,\
                    ball10,ball11,ball12,ball13,\
                    ball14,ball15]
            
        if(self.gameType == 2):
            self.gameBalls=[ball10,ball11,ball12,\
                    ball13,ball14,ball15]
        if(self.gameType == 3):
            self.gameBalls=[ball1]
        self.hideBalls()
            
    def getGameBalls(self):
        return self.gameBalls
        
    def hideBalls(self):
        for balls in self.allBalls:
            if (balls not in self.gameBalls):
                balls.setCoordinates((-1000,-1000))
                balls.deleteBall()
        turtle.update()
        
        
