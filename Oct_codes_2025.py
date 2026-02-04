#    0 1 2
a=[ [1,2,3],   # 0
    [4,5,6],   # 1
    [7,8,9]]   # 2

#    0 1 2 3
b=[ [9,8,7,3], # 0
    [6,5,4,5], # 1
    [3,2,1,7]] # 2

#    0 1 2 3
c=[ [0,0,0,0], # 0
    [0,0,0,0], # 1
    [0,0,0,0]] # 2

"""
      0 1 2
a[i]=[1 2 3]
b[j]=[8 5 2]

i=row (a[0])
j=column (b[1])
c[0][1]=1*8 + 2*5 + 3*2 = 8+10+6 = 24
c[0][1]=a[0][0]*b[0][1] + a[0][1]*b[1][1] + a[0][2]*b[2][1]
c[i][j]=a[i][k]*b[k][j] + a[i][k]*b[k][j] + a[i][k]*b[k][j]
"""
def matrix_multiplication(a,b):
    for i in range(0,len(a)):
        for j in range(0,len(b[0])):
            sum_of_elements=0
            for k in range(0,len(a)):
                product=a[i][k]*b[k][j]
                sum_of_elements=sum_of_elements+product
            c[i][j]=sum_of_elements
    return c

# print(matrix_multiplication(a,b))

candles=[4,4,1,3]

def birthdayCakeCandles(candles):
    present_max=0
    for i in range(0,len(candles)):
        if present_max<candles[i]:
            present_max=candles[i]   
    candles_count=0
    for i in range(0,len(candles)):
        if present_max==candles[i]:
            candles_count=candles_count+1
    return candles_count

# print(birthdayCakeCandles(candles))
