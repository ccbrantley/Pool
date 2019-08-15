import turtle
import cue
import ball
import time
import scene
import gameType
#Making Images available
for x in range(1,361):
    turtle.register_shape("./Sticks/stick"+str(x)+".gif")
for x in range(0,16):
    for y in range(1,4):
        turtle.register_shape("./Balls/ball"+str(x)+str(y)+".gif")
import piecer
#Scene/Turtle settings
wn = turtle.Screen()
wn.setup(width = 1.0, height = 1.0)
turtle.title("Billiards")
wn.bgpic("./Background/pooltable0.gif")
turtle.tracer(0,0)
turtle.pu()
turtle.ht()
#Board Objects
sceneMaker = piecer.piecer()
cueStick = cue.cue()
game = gameType.gameType(0)
cueBall = ball.ball(0,200,0)
allBall = game.getGameBalls()
allBall.append(cueBall)
def main():
    setKeys()
    wn.listen()
    wn.mainloop()
def movStickLeft():
    cueBall.getBallBorder()
    cueStick.cueStickLeft(cueBall)
def movStickRight():
    cueStick.cueStickRight(cueBall)
def frameAdv():
    cueStick.setFrameAdv()
def getCoordinates(x,y):
    turtle.setpos(x,y)
    print(turtle.pos())
def setKeys():
    wn.onscreenclick(getCoordinates,1)
    wn.onkeypress(shootCueBall, "Up")
    wn.onkeypress(frameAdv, "Down")
    wn.onkeypress(movStickLeft, "Left")
    wn.onkeypress(movStickRight, "Right")
    wn.onkey(turtle.bye, "Escape")
    #wn.onkey(resetGame,"r")
def muteKeys():
    wn.onkeypress(None, "Up")
    wn.onkeypress(None, "Left")
    wn.onkeypress(None, "Right")
    
def shootCueBall():
    muteKeys()
    play = [cueBall]
    gameScene = list()
    cueBall.setDirection(cueStick.getDirection())
    for x in range(30,1,-1):
        #if(len(play)>0):
        #    x = int((x/((len(play)/4))))
        for y in range(x,1,-1):
            for balls in play:
                turtle.setpos(balls.getCoordinates())
                turtle.seth(balls.getDirection())
                turtle.forward(1)
                balls.stampBall()
                if (balls.collisionWPocket()) == True:
                    play.remove(balls)
                    balls.setCoordinates((-1000,-1000))
                    continue
                for ball in allBall:
                    if(balls != ball):
                        if(balls.collisionWBall(ball) == True):
                            if(ball not in play):
                                play.append(ball)
        gameFrame = scene.scene()
        for balls in allBall:
            temporary = balls
            gameFrame.appendData(temporary)
        gameScene.append(gameFrame)
    #Resetting Table
    if(cueBall not in play):
        cueBall.setCoordinates((0,200))
        turtle.goto(0,200)
        cueBall.populateTable()
    sceneMaker.animateScene(gameScene)
    wn.onkeypress(shootCueBall, "Up")
    wn.onkeypress(movStickLeft, "Left")
    wn.onkeypress(movStickRight, "Right")
    setKeys()
main()

     
