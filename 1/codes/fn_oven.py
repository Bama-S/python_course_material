#example of function 
def heat(item,time):
    n = time
    while (time>0):
        time = time -1
        print (time, end = ',')
    print()
    print(item, "is ready in ", n, "seconds")

dish = str(input("enter the item whether veg or tea: "))
if dish == "veg":
    heat ("veg",200)
elif dish == "tea":
    heat ("tea",40)
