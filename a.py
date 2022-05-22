s_input = int(input())
result = ""
while s_input >= 10:
    result = '9' + result
    s_input -= 9
result = str(s_input) + result
print(result)
