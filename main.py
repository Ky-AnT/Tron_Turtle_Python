from turtle import *
import time
#Right -> 0
#Left -> left(180)
#Up -> left(90)
#Down -> left(270)
def main():
    class coordinates:
        def __init__(self,x,y,d):
            self.x = x
            self.y = y
            self.d = d

    def render():
        if abs(playerOne.x) >= 390 or abs(playerOne.y) >= 390:
            print(screensize())
            print(playerOne.x,playerOne.y)
            print("Game over!")
            penup()
            pencolor("white")
            goto(0,100)
            write("Yellow wins",font=("Arial",30))
            done()
        if abs(playerTwo.x) >= 390 or abs(playerTwo.y) >= 390:
            print(screensize())
            print(playerTwo.x,playerTwo.y)
            print("Game over!")
            penup()
            pencolor("white")
            goto(0,100)
            write("Red Wins!",font=("Arial",30))
            done()
        penup()
        goto(playerOne.x,playerOne.y)
        pendown()
        pencolor('red')
        left(playerOne.d)
        forward(10)
        right(playerOne.d)
        playerOne.x = round(xcor(),2)
        playerOne.y = round(ycor(),2)
        if [int(playerOne.x),int(playerOne.y)] in coordsLayout:
            coordsLayout.remove([int(playerOne.x),int(playerOne.y)])
        else:
            print("Game over!")
            penup()
            pencolor("white")
            goto(0,100)
            write("Yellow Wins!",font=("Arial",30))
            done()
        penup()
        goto(playerTwo.x,playerTwo.y)
        pendown()
        pencolor('yellow')
        left(playerTwo.d)
        forward(10)
        right(playerTwo.d)
        playerTwo.x = round(xcor(),2)
        playerTwo.y = round(ycor(),2)
        if [int(playerTwo.x),int(playerTwo.y)] in coordsLayout:
            coordsLayout.remove([int(playerTwo.x),int(playerTwo.y)])
        else:
            print("Game over!")
            penup()
            pencolor("white")
            goto(0,100)
            write("Red Wins!",font=("Arial",30))
            done()
    def rightOne():
        if playerOne.d != 180:
            playerOne.d = 0
    def leftOne():
        if playerOne.d != 0:
            playerOne.d = 180
    def upOne():
        if playerOne.d != 270:
            playerOne.d = 90
    def downOne():
        if playerOne.d != 90:
            playerOne.d = 270
        
    def rightTwo():
        if playerTwo.d != 180:
            playerTwo.d = 0
    def leftTwo():
        if playerTwo.d != 0:
            playerTwo.d = 180
    def upTwo():
        if playerTwo.d != 270:
            playerTwo.d = 90
    def downTwo():
        if playerTwo.d != 90:
            playerTwo.d = 270
    coordsLayout = []
    for i in range(-380,390):
        for n in range(-380,390):
            coordsLayout.append([n,-i])
    #print(coordsLayout)
    bgcolor("#1B4F72")
    window = Screen()
    setup(width=800,height=800)
    window.cv._rootwindow.resizable(False, False)
    tracer(0)
    hideturtle()
    title("Tron in Python Turtle - Ky-An Tran")
    pensize(10)
    playerOne = coordinates(-120,0,0)
    playerTwo = coordinates(120,0,180)
    playerOneBorder = []
    playerTwoBorder = []

    window.listen()
    window.onkey(rightOne,"d")
    window.onkey(leftOne,"a")
    window.onkey(upOne,"w")
    window.onkey(downOne,"s")

    window.onkey(rightTwo,"Right")
    window.onkey(leftTwo,"Left")
    window.onkey(upTwo,"Up")
    window.onkey(downTwo,"Down")
    while True:
        time.sleep(0.10)
        render()
        update()

