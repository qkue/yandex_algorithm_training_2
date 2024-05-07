# Python 3.12.1

number = int(input())

max_element = 0
count_elements = 0

while number != 0:
    if number > max_element:
        max_element = number
        count_elements = 1
    elif number == max_element:
        count_elements += 1

    number = int(input())
  
print(count_elements)
