import turtle

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

turtle.bgcolor('black')
turtle.speed(0)
turtle.pensize(3)

for i in range(360):
    turtle.pencolor(colors[i % len(colors)])
    turtle.forward(i)
    turtle.right(59)
    
turtle.exitonclick()
