from turtle import Turtle, mainloop
def tree(plist, l, a, f):
    """ plist is list of pens
    l is length of branch
    a is half of the angle between 2 branches
    f is factor by which branch is shortened
    from level to level."""
    if l > 6:
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst, l*f, a, f)
def main():
    p = Turtle()
    p.color("blue")
    p.pensize(5)
    p.hideturtle()
    p.speed(10)
    p.left(90)
    p.penup()
    p.goto(0,-200)
    p.pendown()
    t = tree([p], 200, 65, 0.6)

main()
