#recursive multiplication of 5
def mul(n):
    count = 0
    if n<=1:
        return 1
    else:
        count  = count +1
        return ("5X",count,"=",(n-1)*5)
n = 12
for i in range (n):
    print (mul(i))
