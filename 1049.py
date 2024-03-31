n, m = map(int, input().split())

package = []
piece = [] 
best = 1000000

for i in range(m):
    a, b = map(int, input().split())
    package.append(a)
    piece.append(b)
bPack = min(package)
bPiece = min(piece)

if bPiece * 6 < bPack:
    best = bPiece * n
elif bPiece * ( n %6 ) > bPack:
    best = bPack * ( n//6 + 1 )
else:
    best = bPack * (n//6) + bPiece * (n % 6)
    
print(best)