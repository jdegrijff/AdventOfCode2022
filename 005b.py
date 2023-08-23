import functions as f

# input_start = f.openFile('005_input_start.txt')
# stacks = input_start.split("\n")
# startingstack = [[stacks[j][i] for j in range(len(stacks))] for i in range(len(stacks[0]))]

input_moves = f.openFile('005_input_moves.txt')
moves = input_moves.split("\n")
stacks = [['H','R','B','D','Z','F','L','S'],
          ['T','B','M','Z','R'],
          ['Z','L','C','H','N','S'],
          ['S','C','F','J'],
          ['P','G','H','W','R','Z','B'],
          ['V','J','Z','G','D','N','M','T'],
          ['G','L','N','W','F','S','P','Q'],
          ['M','Z','R'],
          ['M','C','L','G','V','R','T']]

for move in moves:
    fromlocation = move.find("from")
    tolocation = move.find("to")
    numbertomove = int(move[5:7])
    movefrom = int(move[fromlocation+5])-1
    moveto = int(move[tolocation+3])-1

    stack_from = stacks[movefrom]
    stack_to = stacks[moveto]
    move_start_position = len(stack_from)-numbertomove
    digitstomove = stack_from[move_start_position:]
    
    stacks[movefrom] = stacks[movefrom][:-numbertomove]
    stacks[moveto] = stacks[moveto] + digitstomove

answer = ""
for stack in stacks:
    answer = answer + stack[-1]

print(answer)