d = [list(map(int, input().split())) for _ in range(10)]
x = 1 
y = 1 
while d[x][y]!=2:
    while d[x][y]==0:
        d[x][y]=9
        y+=1 
    if d[x][y]==2:
        d[x][y]=9
        break 
    x=x+1 
    y=y-1 
    if d[x][y]==2:
        d[x][y]=9
        break 
    if d[x][y]==1:
        break 
for i in range(10):
    for j in range(10):
        print(d[i][j], end =' ')
    print()
