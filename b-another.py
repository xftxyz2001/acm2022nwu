list_input = input().split()
n = int(list_input[0])
k = int(list_input[1])
xiyin = input().split()

xiyin = [[int(xiyin[i]), i+1] for i in range(len(xiyin))]


day = 0
result = []
for i in range(k):
    xiyin = sorted(xiyin, key=lambda x: x[0] - x[1] / 1000001)

    current_max = xiyin[-1][0]
    if current_max <= 0:
        break
    index = xiyin[-1][1]
    result.append(index)
    xiyin[-1][0] = xiyin[-1][0] - int(xiyin[-1][0] / 2 + 0.5)
    day += 1
print(day)
for i in range(day):
    print(result[i], end="")
    if i < day - 1:
        print(" ", end="")
print()
