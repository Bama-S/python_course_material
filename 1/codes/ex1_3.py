#program for calculating compound interest
p = 1000.0
r = 0.05
t = 2
y = 5
amount = float(p*(1+(r/t))**(t*y))
amount = round(amount,2)
print ("Amount is Rs. ", amount)
