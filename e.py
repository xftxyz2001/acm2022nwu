a = []
n = int(input())
for i in range(n):
    list_line = input().split()
    first = list_line[0]
    end = list_line[1]


def hs(begin, end, num):
    left = begin
    right = end
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == num:
            return mid
        elif a[mid] < num:
            left = mid - 1
        else:
            right = mid + 1
    return -mid - 1
