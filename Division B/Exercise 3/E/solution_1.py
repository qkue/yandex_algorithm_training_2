with open('input.txt', 'rt', encoding = 'utf-8') as file_input:
    m = int(file_input.readline().rstrip())
    withness = [set(file_input.readline().rstrip()) for _ in range(m)]
    n = int(file_input.readline().rstrip())
    plate = [file_input.readline().rstrip() for _ in range(n)]
    count_plate = [0] * n
    max_count = 0

    for num in withness:
        for plate_number in range(n):
            if num <= set(plate[plate_number]):
                count_plate[plate_number] += 1

                max_count = max(max_count, count_plate[plate_number])
    
    for num in range(n):
        if count_plate[num] == max_count:
            print(plate[num])
