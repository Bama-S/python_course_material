#To find whether 'n' is available in the element and print the element
# See where "n" is appearing and if appearing, count the number of elements available in this list

list1 = ["Chennai","Bangalore","Delhi","25","67","University", "tamilnadu"]
n = len(list1)
count = 0
#"n" in list1[0]
for i in range(0,n):
    if "n" in list1[i]: # to check whether the particular character is in the string
        count += 1
        print(list1[i])
print("Number of elements with letter n:", count)

# Find the number of vowels in a list of items
# find the odd numbers between 1 and 100 - %2 ==1
# find the even numbers between 1 and 100 = %2 == 0
# sum the square of numbers between 1 and 100 
