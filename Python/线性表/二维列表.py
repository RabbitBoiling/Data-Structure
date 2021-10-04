# 声明[3,2]的二维数组，并将所有元素设置为None
row = 2 # 行数
column = 3 # 列数
# for使按照维度顺序来的，列数是第一个维度，沿着x的方向，行数是第二个维度，沿着y的方向
arr = [[None for i in range(column)] for k in range(row)] # 先是最里层的for，也就是后面的for,
arr[0][0] = input('请输入第1行第1列元素：')
arr[0][1] = input('请输入第1行第2列元素：')
arr[0][2] = input('请输入第1行第3列元素：')
arr[1][0] = input('请输入第2行第1列元素：')
arr[1][1] = input('请输入第2行第2列元素：')
arr[1][2] = input('请输入第2行第3列元素：')
# 数组的每个元素的类型为字符串，想进行数值运算，需要转换
# 计算二维数组构成的行列式的所有元素的和
resulit = float(arr[0][0]) + float(arr[0][1]) + float(arr[0][2]) + float(arr[1][0]) + float(arr[1][1]) + float(arr[1][2])
print('行列式的所有元素的和为：%d'%resulit)
print('数组第一行的元素为 %d %d %d'%(float(arr[0][0]),float(arr[0][1]),float(arr[0][2])))
print(arr)
