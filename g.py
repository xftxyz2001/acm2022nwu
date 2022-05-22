n = int(input())
count = n
string_i = input()
cf = []
c = 0
for i in range(n-1):
    if string_i[i] == string_i[i+1]:
        c += 1
    elif c != 0:
        cf.append(c)
        c = 0
if c != 0:
    cf.append(c)
if len(cf) != 0:
    c_max = max(cf)

    for j in range(c_max):
        cn0 = len(cf) - cf.count(0)
        n -= cn0
        count += n
        cf = [i - 1 for i in cf if i != 0]

print(count)
