# Python 3.12.1

arr = input()
parenthesis = 0
flag_wrong = 0

for element in arr:
    if element == '(':
        parenthesis += 1
    else:
        parenthesis -= 1
    flag_wrong = min(parenthesis, flag_wrong)

print('NO' if flag_wrong != 0 or parenthesis else 'YES')
