# 2d list or matrix(matrice)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in matrix:
    print(i)
# print(matrix)
for i in matrix:
    for j in i:
        print(j)

numbers = [2,5,3,7,4]
numbers.append(20)#in append u insert inside an array on last index new number
numbers.insert(0,10)#inside of insert u put atributes 1st index than 2nd value
numbers.remove(3)#remove, remove value
print(numbers)