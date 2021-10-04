# 声明一个一维列表
score = [67,66,82,69,76]
Total_Score = 0
for count in range(len(score)):
    print('第 %d 位学生的分数为；%d' %(count+1,score[count]))
    Total_Score += score[count]
print('-------------------------------------')
print('5位学生的总分位：%d' %Total_Score)