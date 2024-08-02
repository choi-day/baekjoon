import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    sumVote = 0
    best = 0
    bestNum = 0
    same = 0
    for i in range(n):
        vote = int(input())
        sumVote += vote
        if best < vote:
            best = vote
            bestNum = i+1
            same = 0
        elif best == vote:
            same = 1
    if same == 1:
        print('no winner')
    elif best > sumVote//2:
        print('majority winner', bestNum)
    else:
        print('minority winner', bestNum)