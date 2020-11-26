# def neighbors(matrix, rowNumber, colNumber):
#     result = []
#     for rowAdd in range(-1, 2):
#         newRow = rowNumber + rowAdd
#         if newRow >= 0 and newRow <= len(matrix)-1:
#             for colAdd in range(-1, 2):
#                 newCol = colNumber + colAdd
#                 if newCol >= 0 and newCol <= len(matrix)-1:
#                     if newCol == colNumber and newRow == rowNumber:
#                         continue
#                     result.append(matrix[newCol][newRow])
#     return result



matrix =[[0,  1,  2,  3,  4],\
         [5,  6 , 7,  8,  9], \
         [10, 11, 12, 13, 14], \
         [15, 16, 17, 18, 19],\
         [20, 21, 22, 23, 24]]


# a = matrix[0][0]
# print(a)
 
def neighbors(Matrix, row, column):
    
    Neighbors = []
    len_matrix = len(Matrix)-1
    

    if column < len_matrix:
        e = Matrix[row][column+1]
        Neighbors.append(e)
    if column < len_matrix and row > 0:
        c = Matrix[row-1][column+1]
        Neighbors.append(c)
    if column > 0:
        d = Matrix[row][column-1]
        Neighbors.append(d)
    if column > 0 and row > 0:
        a = Matrix[row-1][column-1]
        Neighbors.append(a)
    if row > 0:
        b = Matrix[row-1][column]
        Neighbors.append(b)
    if row < len_matrix:
        g = Matrix[row+1][column]
        Neighbors.append(g)
    if row < len_matrix and column < len_matrix:
        h = Matrix[row+1][column+1]
        Neighbors.append(h)
    if row < len_matrix and column > 0:
        f = Matrix[row+1][column-1]
        Neighbors.append(f)
    
    Neighbors.sort()    
    
    return Neighbors    

# matrix =[[0,  1,  2,  3,  4],\
#          [5,  6 , 7,  8,  9], \
#          [10, 11, 12, 13, 14], \
#          [15, 16, 17, 18, 19],\
#          [20, 21, 22, 23, 24]]
# print(neighbors(matrix,1,3))

# x = 0
# y = 0
# output = neighbors(matrix,x,y)
# # print(output)
# a = int(len(matrix))

# x= 0
# y= 0


# Adjacency_list = []

# while a > 0:
    
#     output = neighbors(matrix,x,y)
#     Adjacency_list.append(output)

#     y+=1

#     if y == len(matrix):
#         y = 0
#         x+=1
#         a-=1
    

# print(Adjacency_list)



