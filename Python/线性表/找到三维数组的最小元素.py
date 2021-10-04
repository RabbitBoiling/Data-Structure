# 声明一个三维数组
num = [[[33,45,67],[23,71,66],[55,38,66]],[[21,19,15],[38,69,16],[90,101,89]]]
value = num[0][0][0]
# 列表的每一个[]就是一个维度的索引
for i in range(len(num)):
    for j in range(len(num[0])):
        for k in range(len(num[0][0])):
            if float(value) >= float(num[i][j][k]):
                value = num[i][j][k]
print('列表元素的最小值为：%d'%value)
