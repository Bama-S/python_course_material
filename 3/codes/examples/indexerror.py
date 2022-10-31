#demonstration of index error
def count(list1):
    print("The number of elements in list ", len(list1))
    try:
        last_element = list1[3]
    except IndexError:
        print("Index value should be less than 3")

n = [10,20,30]
count(n)
