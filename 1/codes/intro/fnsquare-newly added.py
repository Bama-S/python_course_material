def square(total):
    for i in range(1,101):
        sqr = i*i
        total = total+sqr
    print ("The square of the sum of first 100 numbers ", total)
    
tot=0
square(tot)
