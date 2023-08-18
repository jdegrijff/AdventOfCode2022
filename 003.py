import functions as f

def outcome(duplicate):
    if duplicate == 'a':
        return 1
       
def letter_to_position(letter):
    if letter.isalpha():
        if letter.islower():
            return ord(letter) - ord('a') + 1
        else:
            return ord(letter) - ord('A') + 27
    else:
        return None  # Return None for non-alphabetical characters

input = f.openFile('003_input.txt')

rucksacks = input.split("\n")

# print(rucksacks)

number = 0

for rucksack in rucksacks:
    length = len(rucksack)
    half_length = length // 2
    first_half = rucksack[:half_length]
    second_half = rucksack[half_length:]
    
    for char in first_half:
        if char in second_half:
            break

    number = number + letter_to_position(char)

print(number)