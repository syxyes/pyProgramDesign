import turtle
turtle.setup(650, 350, 400, 200) # 启动一个窗口，指定长、宽、左边距、上边距。
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor('red')
turtle.seth(-40)
for i in range(8):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()
