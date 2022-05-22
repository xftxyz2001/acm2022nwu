n = int(input())
a = input().split()
a = [int(i) for i in a]
d = {}
for i in range(n-1):
    num2 = input().split()
    d[int(num2[1]) - 1] = int(num2[0]) - 1
current_max = 0
dp = a[:]

for i in range(len(dp)):
    father_idx = d.get(i, -1)
    if father_idx != -1:
        dp[i] = max(dp[i], dp[father_idx]+dp[i])
        if current_max < dp[i]:
            current_max = dp[i]
print(current_max)
