# Python 3.12.1

children = dict()

answer = []

def check(child, kids, other_branch):
    while child not in other_branch:
        child = kids.get(child, 0)
    return child

with open("input.txt", 'rt', encoding='utf-8') as file_input:
    n = int(file_input.readline().rstrip())
    for _ in range(n - 1):
        ch, parent = file_input.readline().rstrip().split()
        children[ch] = parent

    for line in file_input.readlines():
        name_left, name_right = line.rstrip().split()
        first_tree = set()
        target = name_left
        while target:
            first_tree.add(target)
            target = children.get(target, 0)

        common_ancestor = check(name_right, children, first_tree)
        answer.append(common_ancestor)

print('\n'.join(answer)) 
