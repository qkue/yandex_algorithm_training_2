# Python 3.12.1

word = input()
answer = 0
    
if len(word) > 1:
    left = 0
    right = -1
    for sym in range(len(word) // 2):
        if word[left] != word[right]:
            answer += 1
        left += 1
        right -= 1

print(answer)
