num_list = input().split('\n')

num_lenth = len(num_list)
del num_list[num_lenth-1]

for i in range(0, num_lenth-2):
    num = num_list[i]
    reversed_num = num[::-1]

    if(num == reversed_num):
        print('yes')
    else:
        print('no')
