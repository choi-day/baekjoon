import sys
input = sys.stdin.readline

while True:
    nx, ny, w = map(float, input().split())
    nx, ny = int(nx), int(ny)
    
    if nx == 0 and ny == 0 and w == 0.0:
        break

    xi = sorted(map(float, input().split()))
    yi = sorted(map(float, input().split()))

    # Check if x-axis is fully covered
    x_covered = True
    if xi[0] > w/2 or (75 - xi[-1]) > w/2:
        x_covered = False
    for i in range(1, len(xi)):
        if xi[i] - xi[i-1] > w:
            x_covered = False
            break

    # Check if y-axis is fully covered
    y_covered = True
    if yi[0] > w/2 or (100 - yi[-1]) > w/2:
        y_covered = False
    for i in range(1, len(yi)):
        if yi[i] - yi[i-1] > w:
            y_covered = False
            break
    
    if x_covered and y_covered:
        print("YES")
    else:
        print("NO")