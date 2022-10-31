#get kth column of a matrix
mat1 = [[1,2,3,4],[1,2,1,4],[2,3,5,4]]
#number of rows and columns
print ("The matrix is ", mat1)
rows = len(mat1)
print ("Number of rows = ", rows)
colnum = int(input("Enter the column number to be printed "))
print ("The column ", colnum, "is: ")
for i in range(0,rows):
    print (mat1[i][colnum])
