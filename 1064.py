xa, ya, xb, yb, xc, yc = map(int, input().split())

if (xc - xb)*(yb - ya) == (yc - yb) * (xb - xa):
    print(-1.0)
    exit(0)

ab_len = ((xb - xa) ** 2 + (yb - ya) ** 2)**0.5
ac_len = ((xc - xa) ** 2 + (yc - ya) ** 2)**0.5
bc_len = ((xb - xc) ** 2 + (yb - yc) ** 2)**0.5

maxLen = max([ab_len, ac_len, bc_len])
minLen = min([ab_len, ac_len, bc_len])
middleLen = sum([ab_len, ac_len, bc_len]) - maxLen - minLen

print((maxLen*2 + middleLen*2) - (middleLen*2 + minLen*2))
