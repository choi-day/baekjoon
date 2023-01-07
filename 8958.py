n = int(input())

test_list = []
for i in range(0, n):
    test = input()
    test_list.append(test)

for i in test_list:
    test = []
    score = 0
    assignedScore = 0
    for j in i:
        test.append(j)
    for k in range(0, len(test)):
        if(test[k] == 'O'):
            if(k == 0): #첫번째 문제 배점
                assignedScore = 1
                score += assignedScore
            elif(test[k] == test[k-1]): #문제들 배점 (앞 거랑 같을 경우)
                assignedScore += 1
                score += assignedScore
            else: #문제들 배점 (앞 거랑 다른 경우)
                assignedScore = 1
                score += assignedScore
        else:
            assignedScore = 0
            score += assignedScore
    print(score)