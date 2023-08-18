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

def compare(string1,string2):
    output=""
    for char in string1:
        if char in string2:
            output = output + char
    return "".join(set(output))


input = f.openFile('003_input.txt')

rucksacks = input.split("\n")

rucksackset = range(0,len(rucksacks), 3)

# print(rucksacks)

number = 0

for rucksack in rucksackset:
    rucksack_1 = rucksacks[rucksack]
    rucksack_2 = rucksacks[rucksack+1]
    rucksack_3 = rucksacks[rucksack+2]
    
    r12 = compare(rucksack_1,rucksack_2)
    r123 = compare(r12,rucksack_3)

    number = number + letter_to_position(r123)

print(number)