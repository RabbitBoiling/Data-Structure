global ARRAY_SIZE
ARRAY_SIZE = 5

num = int(ARRAY_SIZE * (ARRAY_SIZE+1) / 2)
B = [None] * (num+1)
def getvalue(i,j):
    index = int(ARRAY_SIZE*i - i*(i+1)/2 + j)
    return B[index]
A = [[1,2,5,3,2],
          [0,6,7,3,4],
          [0,0,2,7,4],
          [0,0,0,9,1],
          [0,0,0,0,8]]
print('上三角矩阵为：')
for i in range(ARRAY_SIZE):
    for j in range(ARRAY_SIZE):
        print('%d' % A[i][j], end='\t')  # end='\t'表示不换行
    print()  # 表示换行
# 将上三角矩阵压缩为一维数组：
index = 0
for i in range(ARRAY_SIZE):
    for j in range(ARRAY_SIZE):
        if A[i][j] != 0:
            index += 1
            B[index] = A[i][j]
print('以一维数组的形式表示为：')
print('[',end='')
for i in range(ARRAY_SIZE):
    for j in range(i+1,ARRAY_SIZE+1):
        print('%d' % getvalue(i,j), end=' ')  # end='\t'表示不换行
print(']',end='')