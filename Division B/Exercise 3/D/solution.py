# Python 3.12.1

with open('input.txt', 'rt', encoding = 'utf-8') as file_input:
    numbers = {num for num in range(1, int(file_input.readline().rstrip()))}

    beatris = None
    august = None


    while beatris != 'HELP':
        beatris = file_input.readline().rstrip()
        if beatris != 'HELP':
            beatris = set(map(int, beatris.split()))
            august = file_input.readline().rstrip()
            if august == 'YES':
                numbers &= beatris
            elif august == 'NO':
                numbers -= beatris

print(*sorted(numbers))
