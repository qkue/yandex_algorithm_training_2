# Python 3.12.1
# большие ограничения и мало тестов

children = dict()

answer = []

def check(child, ancestor, kids):
    res = 0
    target = kids.get(child, 0)
    while target:
        if target == ancestor:
            return True
        
        target = kids.get(target, 0)
    return False


with open("input.txt", 'rt', encoding='utf-8') as file_input:
    n = int(file_input.readline().rstrip())
    for _ in range(n - 1):
        ch, parent = file_input.readline().rstrip().split()
        children[ch] = parent

    for line in file_input.readlines():
        name_left, name_right = line.rstrip().split()
        pre_ans = 0
        if check(name_left, name_right, children):
            pre_ans = 2
        elif check(name_right, name_left, children):
            pre_ans = 1
        answer.append(pre_ans)

print(*answer)   
