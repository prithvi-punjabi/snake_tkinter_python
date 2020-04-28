import turtle
import time
import random
from tkinter import *
from PIL import ImageTk, Image


def play():
    root.destroy()
    p = open("Output.txt", "w")
    p.write("The Score List:\n")

    delay = 0.1

    # Score
    score = 0
    high_score = 0

    # Set up the screen
    wn = turtle.Screen()
    wn.title("Snake Game by PP")
    wn.bgpic(picname="/Users/mackbook/Downloads/3adeac2aaa868c8e3b11656e7217a337.gif")
    wn.setup(width=600, height=600)
    wn.tracer(0)

    # Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("white")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    # Snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)

    segments = []

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


    # Functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"


    def go_down():
        if head.direction != "up":
            head.direction = "down"


    def go_left():
        if head.direction != "right":
            head.direction = "left"


    def go_right():
        if head.direction != "left":
            head.direction = "right"


    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)


    # Keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, "Up")
    wn.onkeypress(go_down, "Down")
    wn.onkeypress(go_left, "Left")
    wn.onkeypress(go_right, "Right")


    def score_board():
        root2 = Tk()
        root2.title("Snake")
        root2.resizable(False, False)
        canvas2 = Canvas(root2, width=300, height=300, )
        canvas2.pack()

        w = Label(canvas2, text="\nOOPS...GAME IS OVER\n\nYOUR SCORE = "
                                + str(score) + "\n\n")
        w.pack()

        button3 = Button(canvas2, text="PLAY AGAIN", bg="green",
                         command=lambda: play_again(root2))
        button3.pack()

        button4 = Button(canvas2, text="EXIT", bg="red",
                         command=lambda: exit_handler(root2))
        button4.pack()


    # Function for handling the play again request
    def play_again(root2):
        root2.destroy()
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    # Function for handling exit request
    def exit_handler(root2):

        root2.destroy()
        turtle.bye()
        turtle.Terminator()


    # Main game loop
    while True:
        wn.update()
        wn.update()

        # Check for a collision with the border
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            # Check for a collision with the food
        if head.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            # Shorten the delay
            delay -= 0.001

            # Increase the score
            score += 10

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            # Move the end segments first in reverse order
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"

                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

                # Clear the segments list
                segments.clear()

                # Reset the score
                score = 0

                # Reset the delay
                delay = 0.1

                # Update the score display
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 24, "normal"))
                score_board()
                p.write(str(score) + "\n")

        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            score_board()
            p.write(str(score) + "\n")

        time.sleep(delay)




def inst():

    root3=Tk()
    root3.geometry("500x300")
    root3.title("Instructions")
    root3.configure(bg="blue")
    l1 = Label(root3,text="This is a simple snake game",bg="blue",fg="white")
    l1.pack()
    l2 = Label(root3, text="Use the arrow keys on your keyboard to move up, down left and right",bg="blue",fg="white")
    l2.pack()
    l3 = Label(root3, text="Everytime the snake consumes food, your score increaseas by 10",bg="blue",fg="white")
    l3.pack()
    l4 = Label(root3, text="The game ends when the snake hits the wall, or eats itself",bg="blue",fg="white")
    l4.pack()
    l5 = Label(root3, text="The speed of the snake increases every time food is consumed",bg="blue",fg="white")
    l5.pack()
    l6 = Label(root3, text="After the snake dies, you are presented with 2 options",bg="blue",fg="white")
    l6.pack()
    l7 = Label(root3, text="You can either Play Again, or Exit the game",bg="blue",fg="white")
    l7.pack()
    l8 = Label(root3, text="If you do choose to exit, you can view your score in the Output.txt file",bg="blue",fg="white")
    l8.pack()
    b1 = Button(root3, width=15, text="PLAY", command=play)
    b1.place(x=180, y=220)



def quitt():
    root.destroy()
root=Tk()
root.geometry("400x400")
root.title("Snake")
image2=Image.open('/Users/mackbook/Downloads/0a99178f683587474d0485bc85335c30.jpg')
image1 = ImageTk.PhotoImage(image2)
l00=Label(root,height=400, width=400, image=image1)
l00.place(x=0,y=0)
label1 = Label(root,text="Snake Game",font="Verdana 32 bold",bg="black",fg="white")
label1.place(x=30,y=15)
b=Button(root,width=15,text="PLAY",command=play)
b.place(x=120,y=200)
b1 = Button(root,width=15,text="QUIT",command=quitt)
b1.place(x=120,y=250)
b2 = Button(root,width=15,text="INSTRUCTION",command=inst)
b2.place(x=120,y=310,anchor="w")
label = Label(root,text="Created by Prithvi",bg="black", fg="white")
label.place(x=125,y=360)

root.mainloop()

