n = int(input())
people = []


for i in range(n):
    a, b = list(input().split(' '))
    people.append((int(a),b))

sortedPeople = list(sorted(people, key = lambda x: x[0]))
for i in sortedPeople:
    print(i[0], i[1])