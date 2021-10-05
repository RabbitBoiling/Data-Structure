NONZERO=0
temp = 1
Sparse = [[0,0,22,0,00,12],
          [0,0,0,0,0,14],
          [3,0,0,0,0,41],
          [0,0,1,0,9,0],
          [7,0,0,0,0,0],
          [0,2,0,0,0,8],
          [0,2,0,0,0,8]]
# 统计稀疏矩阵的非零元素的个数
N = 0
for i in range(len(Sparse)):
    for j in range(len(Sparse[0])):
        if Sparse[i][j] != 0:
            N += 1

# 声明压缩矩阵
Compress = [[None] * 3 for i in range(N + 1)] # 行数与列数要交换
# Compress的第一行记录Sparse的行数，列数，非零元素个数
Compress[0][0] = len(Sparse)
Compress[0][1] = len(Sparse[0])
Compress[0][2] = N
# Compress从第二行开始记录Sparse每一个非零元素
for i in range(len(Sparse)):
    for j in range(len(Sparse[0])):
        if Sparse[i][j] != 0:
            Compress[temp][0] = i+1
            Compress[temp][1] = j+1
            Compress[temp][2] = Sparse[i][j]
            temp += 1
print("稀疏矩阵压缩后的形式为：")
for i in range(N+1):
    for j in range(3):
        print('%d' % Compress[i][j], end='\t')  # end='\t'表示不换行
    print()  # 表示换行

