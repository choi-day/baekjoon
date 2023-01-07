from sympy import true


n, m = map(int, input().split())
n_list = []
m_list = []

n_list.append(int(n/100))
n_list.append(int((n%100)/10))
n_list.append(n%10)

m_list.append(int(m/100))
m_list.append(int((m%100)/10))
m_list.append(m%10)

n_list.reverse()
m_list.reverse()

bingo = 0
i = 0
while true:
    if(n_list[i]>m_list[i]):
        bingo = n_list
        break
    elif(n_list[i]<m_list[i]):
        bingo = m_list
        break
    else:
        i += 1

for i in bingo:
    print(i, end='')
