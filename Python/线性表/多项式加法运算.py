ITEMS = 6
def PrintPoly(Poly,items):
    MaxExp = Poly[0]
    for i in range(1,Poly[0]+2):
        MaxExp -= 1
        if Poly[i] != 0:
            if (MaxExp+1) != 0:
                print(' %dx^%d '%(Poly[i],MaxExp+1),end='')
            else:
                print(' %d' % (Poly[i]),end='')
            if MaxExp >= 0:
                print('%c'%'+',end='')
    print()

def PolySum(Poly1,Poly2):
    result = [None] * ITEMS
    result[0] = Poly1[0]
    for i in range(1,Poly1[0]+2):
        result[i] = Poly1[i] + Poly2[i] #等幂次的系数相加
    PrintPoly(result, ITEMS)

PolyA = [4,3,7,0,6,2] # 多项式A，第一种方法存储多项式
PolyB = [4,1,5,2,0,9]
print('多项式A=> ',end='')
PrintPoly(PolyA,ITEMS) # 打印出多项式A
print('多项式B=> ',end='')
PrintPoly(PolyB,ITEMS) # 打印出多项式A
print('A+B=> ',end='')
PolySum(PolyA,PolyB)
