# 二维数组的声明
A = [[2,3,4,9],[12,33,7,9],[22,52,4,3]]
B = [[22,36,74,2],[12,14,25,31],[21,42,63,20]]
# 先生成空矩阵C
row = 3 # 行数
column = 4 # 列数
# for使按照维度顺序来的，列数是第一个维度，沿着x的方向，行数是第二个维度，沿着y的方向
C = [[None for i in range(column)] for k in range(row)] # 先是最里层的for，也就是后面的for,
for i in range(row):
    for j in range(column):
        C[i][j] = A[i][j] + B[i][j]
print('矩阵A与矩阵B的相加结果为：')
for i in range(row):
    for j in range(column):
        print('%d' %C[i][j],end='\t')
print()
print('矩阵C为：')
print(C)
