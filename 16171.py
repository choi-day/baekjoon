mix = input()
key = input()
skey = []
for i in mix:
    if i.isalpha():
        skey.append(i)
skey = ''.join(skey)
if key in skey:
    print(1)
else:
    print(0)