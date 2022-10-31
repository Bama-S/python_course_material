course = input("Enter your course: ")
day = input("Enter the day as mon, tues, wed, thurs, fri, sat, sun: ")
if (course == "MCA"):
    if (day == "mon" or day == "wed" or day == "fri"):
        print("You have a class at 8.30 a.m. Get ready!")
