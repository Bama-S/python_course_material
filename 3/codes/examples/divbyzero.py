def divide(nr,dr):
    try:
        quotient = nr/dr
    except ZeroDivisionError:
        print("You cannot divide a number by 0")

n = 10
divide(n,0)
