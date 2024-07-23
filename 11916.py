n = int(input())
bList = list(map(int, input().split()))
one = False
two = False
three = False
lose = 0
ball = 0

def rotation1():
    global one
    global two
    global three
    global lose
    global ball

    if three == True and one == True and two == True:
        lose += 1
    elif two == True and one == True:
        three = True
    elif one == True:
        two = True
    one = True

for i in bList:
    if i == 1:
        ball +=1
    if i == 2:
        rotation1()
        ball = 0
    if i == 3:
        if three == True: lose += 1; three = False
        if two == True: three = True; two = False
        if one == True: two = True; one = False
        ball += 1
    if ball == 4:
        ball = 0
        rotation1()

print(lose)