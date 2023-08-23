import functions as f

input = f.openFile('004_input.txt')

sections = input.split("\n")

number = 0
false_number = 0
for section in sections:
    comma = section.find(",")
    length = len(section)
    first_half = section[:comma]
    second_half = section[comma+1:]

    first_dash = first_half.find("-")
    first_half_length = len(first_half)
    first_half_min = int(first_half[:first_dash])
    first_half_max = int(first_half[first_dash+1:])

    second_dash = second_half.find("-")
    second_half_length = len(second_half)
    second_half_min = int(second_half[:second_dash])
    second_half_max = int(second_half[second_dash+1:])
    
    if (
        first_half_min >= second_half_min 
        and first_half_min <= second_half_max 
        ):
        number = number + 1    
    elif (
        second_half_min >= first_half_min 
        and second_half_min <= first_half_max 
        ):
        number = number + 1
    elif (
        first_half_max >= second_half_min 
        and first_half_max <= second_half_max 
        ):
        number = number + 1    
    elif (
        second_half_max >= first_half_min 
        and second_half_max <= first_half_max 
        ):
        number = number + 1
    else:
        false_number = false_number + 1

print(number)