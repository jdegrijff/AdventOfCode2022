import functions as f

input = f.openFile('009_input.txt')
actions = input.split("\n")

coordinates_touched_h= ['0:0']
coordinates_touched_t= ['0:0']
direction = []
coordinate_h_x = 0
coordinate_h_y = 0
coordinate_t_x = 0
coordinate_t_y = 0

for action in actions:
    mov = action[2:]
    dir = action[0:1] * int(mov)
    direction.append(dir)
    
for d in direction:
    moves = list(d)
    for m in moves:
        if m == "R":
            coordinate_h_x = coordinate_h_x + 1
        elif m == "L":
            coordinate_h_x = coordinate_h_x - 1
        elif m == "U":
            coordinate_h_y = coordinate_h_y + 1
        elif m == "D":
            coordinate_h_y = coordinate_h_y - 1            
        coordinates_h = str(coordinate_h_x) + ":" + str(coordinate_h_y)
        coordinates_touched_h.append(coordinates_h)

        if coordinate_h_x - coordinate_t_x > 1 and coordinate_h_y - coordinate_t_y > 1:
            coordinate_t_x = coordinate_t_x + 1
            coordinate_t_y = coordinate_t_y + 1
        if coordinate_h_x - coordinate_t_x > 1 and coordinate_h_y - coordinate_t_y == 1:
            coordinate_t_x = coordinate_t_x + 1
            coordinate_t_y = coordinate_t_y + 1
        if coordinate_h_x - coordinate_t_x > 1 and coordinate_h_y - coordinate_t_y == 0:
            coordinate_t_x = coordinate_t_x + 1
            coordinate_t_y = coordinate_t_y            
        if coordinate_h_x - coordinate_t_x > 1 and coordinate_h_y - coordinate_t_y == -1:
            coordinate_t_x = coordinate_t_x + 1
            coordinate_t_y = coordinate_t_y - 1
        if coordinate_h_x - coordinate_t_x > 1 and coordinate_h_y - coordinate_t_y < -1:
            coordinate_t_x = coordinate_t_x + 1
            coordinate_t_y = coordinate_t_y - 1

        if coordinate_h_x - coordinate_t_x == 1 and coordinate_h_y - coordinate_t_y > 1:
            coordinate_t_x = coordinate_t_x + 1
            coordinate_t_y = coordinate_t_y + 1
        if coordinate_h_x - coordinate_t_x == 1 and coordinate_h_y - coordinate_t_y == 1:
            coordinate_t_x = coordinate_t_x
            coordinate_t_y = coordinate_t_y
        if coordinate_h_x - coordinate_t_x == 1 and coordinate_h_y - coordinate_t_y == 0:
            coordinate_t_x = coordinate_t_x
            coordinate_t_y = coordinate_t_y            
        if coordinate_h_x - coordinate_t_x == 1 and coordinate_h_y - coordinate_t_y == -1:
            coordinate_t_x = coordinate_t_x
            coordinate_t_y = coordinate_t_y
        if coordinate_h_x - coordinate_t_x == 1 and coordinate_h_y - coordinate_t_y < -1:
            coordinate_t_x = coordinate_t_x + 1
            coordinate_t_y = coordinate_t_y - 1

        if coordinate_h_x - coordinate_t_x == 0 and coordinate_h_y - coordinate_t_y > 1:
            coordinate_t_x = coordinate_t_x
            coordinate_t_y = coordinate_t_y + 1
        if coordinate_h_x - coordinate_t_x == 0 and coordinate_h_y - coordinate_t_y == 1:
            coordinate_t_x = coordinate_t_x
            coordinate_t_y = coordinate_t_y
        if coordinate_h_x - coordinate_t_x == 0 and coordinate_h_y - coordinate_t_y == 0:
            coordinate_t_x = coordinate_t_x
            coordinate_t_y = coordinate_t_y            
        if coordinate_h_x - coordinate_t_x == 0 and coordinate_h_y - coordinate_t_y == -1:
            coordinate_t_x = coordinate_t_x
            coordinate_t_y = coordinate_t_y
        if coordinate_h_x - coordinate_t_x == 0 and coordinate_h_y - coordinate_t_y < -1:
            coordinate_t_x = coordinate_t_x
            coordinate_t_y = coordinate_t_y - 1

        if coordinate_h_x - coordinate_t_x == -1 and coordinate_h_y - coordinate_t_y > 1:
            coordinate_t_x = coordinate_t_x - 1
            coordinate_t_y = coordinate_t_y + 1
        if coordinate_h_x - coordinate_t_x == -1 and coordinate_h_y - coordinate_t_y == 1:
            coordinate_t_x = coordinate_t_x
            coordinate_t_y = coordinate_t_y
        if coordinate_h_x - coordinate_t_x == -1 and coordinate_h_y - coordinate_t_y == 0:
            coordinate_t_x = coordinate_t_x
            coordinate_t_y = coordinate_t_y            
        if coordinate_h_x - coordinate_t_x == -1 and coordinate_h_y - coordinate_t_y == -1:
            coordinate_t_x = coordinate_t_x
            coordinate_t_y = coordinate_t_y
        if coordinate_h_x - coordinate_t_x == -1 and coordinate_h_y - coordinate_t_y < -1:
            coordinate_t_x = coordinate_t_x - 1
            coordinate_t_y = coordinate_t_y - 1

        if coordinate_h_x - coordinate_t_x < -1 and coordinate_h_y - coordinate_t_y > 1:
            coordinate_t_x = coordinate_t_x - 1
            coordinate_t_y = coordinate_t_y + 1
        if coordinate_h_x - coordinate_t_x < -1 and coordinate_h_y - coordinate_t_y == 1:
            coordinate_t_x = coordinate_t_x - 1
            coordinate_t_y = coordinate_t_y + 1
        if coordinate_h_x - coordinate_t_x < -1 and coordinate_h_y - coordinate_t_y == 0:
            coordinate_t_x = coordinate_t_x - 1
            coordinate_t_y = coordinate_t_y            
        if coordinate_h_x - coordinate_t_x < -1 and coordinate_h_y - coordinate_t_y == -1:
            coordinate_t_x = coordinate_t_x - 1
            coordinate_t_y = coordinate_t_y - 1
        if coordinate_h_x - coordinate_t_x < -1 and coordinate_h_y - coordinate_t_y < -1:
            coordinate_t_x = coordinate_t_x - 1
            coordinate_t_y = coordinate_t_y - 1

        coordinates_t = str(coordinate_t_x) + ":" + str(coordinate_t_y)
        try:
            index_value = coordinates_touched_t.index(coordinates_t)
        except ValueError or IndexError:
            index_value = -1
        if index_value < 0:
            coordinates_touched_t.append(coordinates_t)

answer = len(coordinates_touched_t)
print(answer)