# Python 3.12.1
# Задача разбиралась в лекции

def traverse(root, prefix = []):
    if root['left'] is None and root['right'] is None:
        return [''.join(prefix)]
    prefix.append('0')
    ans = traverse(root['left'], prefix)
    prefix.pop()
    prefix.append('1')

    ans.extend(traverse(root['right'], prefix))
    prefix.pop()
    return ans

def maketree(serialized):
    tree = {'left': None, 'right': None, 'up': None, 'type': 'root'}
    nownode = tree

    for sym in serialized:
        if sym == 'D':
            newnode = {'left': None, 'right': None, 'up': nownode, 'type': 'left'}
            nownode['left'] = newnode
            nownode = newnode
        elif sym == 'U':
            while nownode['type'] == 'right':
                nownode = nownode['up']
            nownode = nownode['up']
            newnode = {'left': None, 'right': None, 'up': nownode, 'type': 'right'}
            nownode['right'] = newnode
            nownode = newnode
    return tree

res = []
for _ in range(int(input())):
    haff_tree = maketree(input())
    codes = traverse(haff_tree)
    res.append(len(codes))
    res.extend(codes)

print(*res, sep='\n')
