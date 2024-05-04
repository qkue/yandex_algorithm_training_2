# Python 3.12.1
# "Гарантируется, что запросы PRINTTREE будут вызываться только в моменты, когда дерево не пустое", но про команду SEARCH такого не говорится :-)

binary = []

def add_node(node, arr):
    if not arr:
        arr = [node, [None, None]]
        return arr, 'DONE'
    
    value = 'ALREADY'
    key = arr[0]
    if node < key:
        if arr[1][0] == None:
            arr[1][0] = [node, [None, None]]
            value = 'DONE'
        else:
            value = add_node(node, arr[1][0])[1]
    elif node > key:
        if arr[1][1] == None:
            arr[1][1] = [node, [None, None]]
            value = 'DONE'
        else:
            value = add_node(node, arr[1][1])[1]
    return arr, value

def find_node(node, arr):
    ans: Literal['NO'] = 'NO'
    if arr:
        key = arr[0]
        if node == key:
            ans = 'YES'
        elif node < key:
            if arr[1][0] == None:
                return 'NO'
            else:
                ans = find_node(node, arr[1][0])
        elif node > key:
            if arr[1][1] == None:
                return 'NO'
            else:
                ans = find_node(node, arr[1][1])
    return ans

def walk(binary):
    pre_ans = []
    counting = -1
    def walking(binary, cnt, x = 0):
        if binary == None:
            return
        cnt += 1
        walking(binary[1][0], cnt, 0)
        pre_ans.append(f'{"." * cnt}{binary[0]}')
        walking(binary[1][1], cnt, 1)
    walking(binary, counting)
    ans = ('\n'.join(str(a) for a in pre_ans))
    return ans 

with open("input.txt", 'rt', encoding='utf-8') as file_input:
    for line in file_input.readlines():
        command= line.rstrip().split()
        if command[0] == 'ADD':
            binary, res = add_node(int(command[1]), binary)
            print(res)
        elif command[0] == 'SEARCH':
            res = find_node(int(command[1]), binary)
            print(res)
        elif command[0] == 'PRINTTREE':
            print(walk(binary))
