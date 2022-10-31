#illustration of StopIteration
def add(num):
    while True:
        try:
            num = num + 1
            if num == 11:
                raise StopIteration
        except StopIteration:
            break
        else:
            print(num)

x = 0
add(x)
