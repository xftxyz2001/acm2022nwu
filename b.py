list_input = input().split()
n = int(list_input[0])
k = int(list_input[1])
xiyin = input().split()

xiyin = [int(i) for i in xiyin]
day = 0
result = []
for i in range(k):
    current_max = sorted(xiyin)[-1]
    if current_max <= 0:
        break
    index = xiyin.index(current_max)
    result.append(index+1)
    xiyin[index] = xiyin[index] - int(xiyin[index] /2 +0.5)
    day +=1
print(day)
for i in range(day):
    print(result[i], end = "")
    if i < day - 1:
        print(" ", end = "")
print()
