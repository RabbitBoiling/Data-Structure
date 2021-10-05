arrA = [[1,2,3,4],[5,6,7,8],[9,0,7,2]]
row = 3
column = 4
# 声明[3,4]的数组
arrB = [[None for i in range(row)] for j in range(column)] # 行数与列数要交换
print('原矩阵为：')
for i in range(row):
    for j in range(column):
        print('%d'%arrA[i][j],end='\t') # end='\t'表示不换行
    print() # 表示换行
# 进行矩阵转置操作
for i in range(column):
    for j in range(row):
        arrB[i][j] = arrA[j][i]
print('转置后的矩阵为：')
for i in range(column):
    for j in range(row):
        print('%d'%arrB[i][j],end='\t') # end='\t'表示不换行
    print() # 表示换行
