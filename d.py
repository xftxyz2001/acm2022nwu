list_input = input().split()
n = int(list_input[0])
m = int(list_input[1])
t = int(list_input[2])
a = []
for i in range(n):
    line = input()
    row = []
    for j in range(m):
        if line[j] == '0':
            row.append(1)
        else:
            row.append(1 + t)
    a.append(row)
a[0][0] = 0

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            a[i][j] += a[i][j-1]
        elif j == 0:
            a[i][j] += a[i-1][j]
        else:
            a[i][j] += min(a[i][j-1],a[i-1][j])
print(a[n-1][m-1])
