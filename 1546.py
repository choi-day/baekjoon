def changedScore (n, max) :
    return n /max*100

n = int(input())
scoreList = []
changedScoreList = []
score = input()

for i in score.split():
    scoreList.append(int(i))

for i in scoreList:
    changedScoreList.append(changedScore(i, max(scoreList)))
scoreSum = sum(changedScoreList)
print(scoreSum / n)