import random


N = int(input('Input N :'))
M = int(input('Input M : '))
K = int(input('Input K : '))

X = [[1 for i in range(M)]
         for j in range(N)]
Y = [[1 for i in range(K)] 
         for j in range(M)]
Z = [[0 for i in range(K)]
         for j in range(N)]

for i in range(N):
    for j in range(M):
        X[i][j] = random.randint(1,9)
        
for i in range(M):
    for j in range(K):
        Y[i][j] = random.randint(1,9)

i=0      
while i<N:
    for j in range(K):
        for K in range(M):
            Z[i][j] += (X[i][K] * Y [K][j]) 
    i+=1    
print('Matrix A ==> ', X)
print('Matrix B ==> ', Y)
print('Multiplication  : ', Z)
