import functions as f

input = f.openFile('010_input.txt')
instructions = input.split("\n")
cycles = []
value = []
x = 1
cycle = 0
x_times_cycle = []

for i in instructions:
    split = i.split(" ")
    if len(split) == 2:
        cycles.append(split[0])
        cycles.append(split[1])
    elif len(split) == 1:
        cycles.append(split[0])

for c in cycles:
    cycle = cycle + 1
    x_times_cycle.append(x * cycle)
    if c == "noop":
        x = x + 0
    elif c == "addx":
        x = x + 0    
    else:
        x = x + int(c)
    value.append(x)

answer = (x_times_cycle[20-1] + 
          x_times_cycle[60-1] + 
          x_times_cycle[100-1] + 
          x_times_cycle[140-1] + 
          x_times_cycle[180-1] + 
          x_times_cycle[220-1])

print(answer)