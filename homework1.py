#读入excel文件
import pandas as pd
import numpy  as np
import math
from pandas.core.common import not_none
a = pd.read_excel(r'C:\Users\86130\Desktop\data1.xls',header=None).to_numpy()
b = pd.read_excel(r'C:\Users\86130\Desktop\data2.xls',header=None).to_numpy()
#H(Y),H(X)
#输入a得hx，a.T得hy
def hx(mat):
    i,j=mat.shape
    x=0
    y=0
    _sum=0
    hx=0
    hy=0
    while x<i:
        while y<j:
            _sum+=mat[x][y] #第x行的和
            y+=1
        y = 0
        if _sum==0:
            _sum=1      #利用log1=0
        hy+=_sum*math.log2(_sum)
        _sum=0
        x+=1
    hy=hy*(-1)
    return hy
#H(X|Y)
def hxy(b):
    i,j=b.shape
    a = np.copy(b)
    n=0
    m=0
    p=0
    hxy_n=0
    hxy=0
    while n<j :
        while m<i:
            if np.sum(a[:,n])!=0:
                a[m][n]=a[m][n]/np.sum(a[:,n]) #归一化
                if a[m][n]==0:
                    a[m][n]=1
                m+=1
            else:
                return 0
        while p<i:
            hxy_n+=a[p][n]*math.log2(a[p][n])    #H（X|yn）
            p+=1
        hxy+=np.sum(a[:,n])*hxy_n
        hxy_n=0
        n+=1
    hxy=hxy*(-1)
    return hxy
print("data1")
print("H(X):",hx(a))
print("H(Y):",hx(a.T))
print("H(X|Y)",hxy(a))
print("H(Y|X)",hxy(a.T))
print("I(X,Y)",hx(a)+hxy(a))
print("data2")
print("H(X):",hx(b))
print("H(Y):",hx(b.T))
print("H(X|Y)",hxy(b))
print("H(Y|X)",hxy(b.T))
print("I(X,Y):",hx(b)+hxy(b))