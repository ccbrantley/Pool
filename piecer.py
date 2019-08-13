import turtle
import ball
import time
turtle.pu()
turtle.ht()
temporaryBall = ball.ball(-500,-500,0)
class piecer():
    def animateScene(self,scenes):
        for frame in scenes:
            turtle.clearstamps()
            frame.getData()
            for each in frame.getData():
                temporaryBall.stampBallScene(each)
            turtle.update()
            time.sleep(.05)
                
                
                
            
        


