import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")
t1 = turtle.Turtle()
t1.pensize(5)

clrs = ["yellow","red","purple","blue"]
for i in clrs:
    t1.color(i)
    t1.forward(50)
    t1.right(90)

wn.mainloop()
