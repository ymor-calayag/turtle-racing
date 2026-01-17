from turtle import Turtle, Screen
import turtle
import random

s = Screen()
s.setup(width=500, height=400)

color_list = ["red", "orange", "green", "blue", "violet"]
y_pos = [60, 30, 0, -30, -60]
turtle_list = []

user_bet = turtle.textinput("Make your bet",'Which turtle will win the race? (red, orange, green, blue, violet)')
print(user_bet)

for ti in range(0, 5):
    t = Turtle("turtle")
    t.up()
    t.color(color_list[ti])
    t.goto(x=-230, y=y_pos[ti])
    turtle_list.append(t)

game_over = False
while not game_over:
    move = random.randrange(0, 11)
    random_turtle = random.choice(turtle_list)
    random_turtle.forward(move)

    # this works, but im not okay with it just printing, and also it prints the user input
    if random_turtle.xcor() >= 220:
        game_over = True
        if random_turtle.color()[0] == user_bet:
            print("Your turtle won!")


s.exitonclick()