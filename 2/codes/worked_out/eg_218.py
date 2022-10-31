#Get the digit from the user and print the corresponding number in letters. Use dictionary
n_dict = {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8: "Eight", 9: "Nine"}
n = int(input("Enter the number from 0 to 9: "))
print ("The entered number is ", n)
for i,j in n_dict.items():
    if i == n:
        print ("In letters ", n_dict[i])
