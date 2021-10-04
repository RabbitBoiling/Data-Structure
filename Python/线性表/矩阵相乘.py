def MatrixMulitply(arrA,arrB,arrC,M,N,P):
    global C
    if M<=0 or N<=0 or P <= 0:
        print('错误，维数M,N,P必须大于0')
        return
    for i in range(M):
        for j in range(P):
            Temp = 0
            for k in range(N):
                # A的i行k列的元素与B的k行j列的元素相乘
                Temp = Temp + float(arrA[i*N+k]) * float(arrB[k*P+j])
            # C的i行j列
            arrC[i*P+j] = Temp

print('请输入矩阵A的维数[M,N]:')
M = int(input('M = '))
N = int(input('N = '))
A = [None] * M *N #声明大小为[M,N]的列表A,始终是一维列表
print('请输入矩阵A的各个元素:')
for i in range(M):
    for j in range(N):
        A[i*N+j] = input('a%d%d='%(i,j)) # i*N表示了第i行，i*N+j表示了第i行的第j列
print('输入矩阵A为:')
print(A)

print('请输入矩阵B的维数[N,P]:')
N = int(input('N = '))
P = int(input('P = '))
B = [None] * N * P #声明大小为[N,P]的列表B
print('请输入矩阵B的各个元素:')
for i in range(N):
    for j in range(P):
        B[i*P+j] = input('b%d%d='%(i,j))
print('输入矩阵B为:')
print(B)

C = [None] * M * P #声明大小为[M,P]的列表c
MatrixMulitply(A,B,C,M,N,P)
print('矩阵A与矩阵B的相乘结果为：')
for i in range(M):
    for j in range(P):
        print('%d' %C[i*P+j],end='\t')
print(C)

