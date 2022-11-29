def Lpuproject( matrix) :
    n = len(matrix)
    sumd1=0
    sumd2=0
    for i in range(n):
        sumd1+=matrix[i][i]
        sumd2+=matrix[i][n-i-1]
    if not(sumd1==sumd2):
        return False

    for i in range(n):
        sumr=0

        sumc=0

        for j in range(n):

            sumr+=matrix[i][j]

            sumc+=matrix[j][i]

    if not(sumr==sumc==sumd1):

        return False 

    return True
N = int(input("NxN:"))
  

matrix = []
print("enter theb matrix")
  

for i in range(N):          
    a =[]
    for j in range(N):      
         a.append(int(input()))
    matrix.append(a)
print("majic box")
for i in range(N):
    for j in range(N):
        print(matrix[i][j], end = " ")
    print()
sum=0
for i in range(N):
        sum+=matrix[i][i]  
if(Lpuproject(matrix)):
    print("this is a Magic Box",sum)
else:
    print("this is not a magic Box")
