f = open('001_input.txt','r')
input = f.read()
f.close()

foodbags = input.split("\n\n")

dwarfes = range(len(foodbags))

for d in dwarfes:
    equation = foodbags[d].replace('\n', '+')
    foodbags[d] = eval(equation)

print(max(foodbags))