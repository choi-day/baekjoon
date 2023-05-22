A, B, N = map(int, input().split(' '))
if(A < B):
    for i in range(N):
        C = int(A*10 / B)
        A = A*10 - B*C
else:
    A = A - B*int(A/B)
    for i in range(N):
        C = int(A*10 / B)
        A = A*10 - B*C
print(C)