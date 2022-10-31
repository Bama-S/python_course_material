dish = str(input("enter the item whether veg or tea: "))
if dish == "veg":
    n = 2*60
    time = n
    while (n>0):
        n = n - 1
        print (n,end=',')
    print ("\n")
    print("Veg is cooked in", time, "seconds")
elif dish == "tea":
    n = 40
    time = n
    while (n>0):
        n = n-1
        print (n,end=",")
    print ("\n")
    print ("Tea is heated in", time, "seconds")
