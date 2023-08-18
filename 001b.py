import functions as f

def calories(foodbags):
    dwarfes = range(len(foodbags))
    for d in dwarfes:
        equation = foodbags[d].replace('\n', '+')
        foodbags[d] = eval(equation)


input = f.openFile('001_input.txt')
# print(input)
foodbags = input.split("\n\n")

# print(foodbags[0])

calories(foodbags)

print(max(foodbags))

foodbags.sort(reverse=True)
print(foodbags[0:3])
print(sum(foodbags[0:3]))


# numberone = max(foodbags)
# foodbags.remove(numberone)

# print(max(foodbags))

# numbertwo = max(foodbags)
# foodbags.remove(numbertwo)

# print(max(foodbags)+numbertwo+numberone)

