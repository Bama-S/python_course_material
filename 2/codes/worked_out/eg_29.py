#addition of two matrices
mat1 = [[1,2,3],[1,2,1],[2,3,5]]
mat2 = [[1,2,3],[1,2,1],[2,3,5]]
total = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        total[i][j] = mat1[i][j]+mat2[i][j]
print ("Matrix 1", mat1)
print ("Matrix 2", mat2)
print ("Addition of matrix", total)
