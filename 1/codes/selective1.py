day = input("Enter the day as mon, tues, wed, thurs, fri, sat, sun: ")
if (day == "mon" or day == "wed" or day == "fri"):
    print("You have a class at 8.30 a.m. Get ready")
elif (day == "tues"):
    print("You have a class at 11.20 a.m.")
elif (day == "thurs"):
    print("You have a class at 10.30 a.m.")
else:
    print("Either you have entered a wrong string or it is holiday")
