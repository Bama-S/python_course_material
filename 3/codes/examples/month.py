#get the input of 1 to 12 for month. Else raise exception
month = int(input("Enter the month in values from 1 to 12 "))
if month < 1 or month > 12:
    raise ValueError("Enter only values between 1 to 12")
else:
    print("The value of month is ", month)
