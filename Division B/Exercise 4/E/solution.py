# Python 3.12.1

forum = dict()
order_message = dict()
counter = 0

n = int(input())
for _ in range(n):
    identificator = int(input())
    if identificator == 0:
        topic = input()
        forum[topic] = forum.get(topic, 0) + 1
        temp = input()
        
    else:
        temp = input()
        topic = order_message[identificator]
        forum[topic] += 1

    counter += 1
    order_message[counter] = topic

result = []
cntr = 1
for key, value in forum.items():
    result.append((key, value, cntr))
    cntr += 1
result.sort(key = lambda p: (-p[1], p[2]))
print(result[0][0])
