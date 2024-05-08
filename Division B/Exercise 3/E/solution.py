# Python 3.12.1

with open('input.txt', 'rt', encoding = 'utf-8') as file_input:
    m = int(file_input.readline().rstrip())
    withness = {file_input.readline().rstrip() for _ in range(m)}
    n = int(file_input.readline().rstrip())
    plate = [file_input.readline().rstrip() for _ in range(n)]
    count_plate = [0] * n
    max_count = 0

    for num in withness:
        for plate_number in range(n):
            if set(num) <= set(plate[plate_number]):
                count_plate[plate_number] += 1

                if count_plate[plate_number] > max_count:
                    max_count = count_plate[plate_number]
    
    for num in range(n):
        if count_plate[num] == max_count:
            print(plate[num])
