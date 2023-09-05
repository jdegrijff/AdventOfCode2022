import functions as f

input = f.openFile('010_input.txt')
instructions = input.split("\n")
cycles = []
value = []
x = 1
cycle = 0
x_times_cycle = []
answer = "#"

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

cycle = -1
for v in value:
    if cycle > 39:
        cycle = 1
    else:
        cycle = cycle + 1
    c1 = cycle 
    c2 = cycle + 1
    c3 = cycle + 2
    if v == c1 or v == c2 or v == c3:
        answer = answer + "#"
    else:
        answer = answer + " "    
    
line1 = answer[:40]
line2 = "#" + answer[41:80]
line3 = "#" + answer[81:120]
line4 = "#" + answer[121:160]
line5 = "#" + answer[161:200]
line6 = "#" + answer[201:240]

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)