import functions as f
import math

input = f.openFile('012_input.txt')
rows = input.split("\n")

columns = list(rows[0])
position = -1
moves = range(0,300)
attempts = range(0,10000000)
routes = []
visited = []
steps = []
number = 0
to_visit = []
to_visit_with_num = []

for row in rows:
    for column in columns:
        position = position + 1
        letter_to_move = row[position-1:position]
        columns[position-1] = columns[position-1] + letter_to_move
    position = -1
    columns[position] = columns[position] + row[-1:]

for column in columns:
    column_f = column[1:]
    position = position + 1
    columns[position] = column_f

for c2 in columns:
    if c2.find("") > -1:
        y_end = c2.find("")
    if c2.find("E") > -1:
        y_start = c2.find("E")        
for r2 in rows:
    if r2.find("") > -1:
        x_end = r2.find("")    
    if r2.find("E") > -1:
        x_start = r2.find("E")           
goal = str(x_end) + ":" + str(y_end)
to_visit_with_num.append(str(x_start) + ":" + str(y_start) + "," + str(0))
to_visit.append(str(x_start) + ":" + str(y_start))

for a in attempts:
    for tv in to_visit_with_num:
        coor_now = tv.split(",")[0]
        if coor_now not in visited:
            number = tv.split(",")[1]
            visited.append(coor_now)
            steps.append(number)
            location_r = int(coor_now.split(":")[0])
            location_u = int(coor_now.split(":")[1])
            location = rows[location_u][location_r:location_r + 1]

            if location_u != 0:
                dir_up = rows[location_u - 1][location_r:location_r + 1]
            else:
                dir_up = ''

            if location_u + 1 != len(rows):
                dir_down = rows[location_u + 1][location_r:location_r + 1]
            else:
                dir_down = ''

            if location_r != 0:
                dir_left = rows[location_u][location_r - 1:location_r]
            else:
                dir_left = ''

            if location_r + 1 != len(columns):
                dir_right = rows[location_u][location_r + 1:location_r + 2]
            else:
                dir_right = ''

            location_num = ord(location) - ord('a') + 1
            if location == 'E':
                location_num = 27

            if dir_up.isalpha():
                num_up = ord(dir_up) - ord('a') + 1
            if dir_up != '' and location_u != 0:
                if num_up < 0:
                    num_up = 26
                if num_up > location_num - 2:
                    coor_up = str(location_r) + ":" + str(location_u - 1)                 
                    if coor_up not in to_visit and coor_up not in visited:
                        to_visit_with_num.append(coor_up + "," + str(int(number) + 1))
                        to_visit.append(coor_up)

            if dir_down.isalpha():
                num_down = ord(dir_down) - ord('a') + 1
            if dir_down != '' and location_u != len(rows):
                if num_down < 0:
                    num_down = 26
                if num_down > location_num - 2:
                    coor_down = str(location_r) + ":" + str(location_u + 1)                  
                    if coor_down not in to_visit and coor_down not in visited:
                        to_visit_with_num.append(coor_down + "," + str(int(number) + 1))
                        to_visit.append(coor_down)

            if dir_left.isalpha():
                num_left = ord(dir_left) - ord('a') + 1
            if dir_left != '' and location_r != 0:
                if num_left < 0:
                    num_left = 26
                if num_left > location_num - 2:
                    coor_left = str(location_r - 1) + ":" + str(location_u)            
                    if coor_left not in to_visit and coor_left not in visited:
                        to_visit_with_num.append(coor_left + "," + str(int(number) + 1))
                        to_visit.append(coor_left)

            if dir_right.isalpha():
                num_right = ord(dir_right) - ord('a') + 1
            if dir_right != '' and location_r != len(columns):
                if num_right < 0:
                    num_right = 26
                if num_right > location_num - 2:
                    coor_right = str(location_r + 1) + ":" + str(location_u)
                    if coor_right not in to_visit and coor_right not in visited:
                        to_visit_with_num.append(coor_right + "," + str(int(number) + 1))
                        to_visit.append(coor_right)

        to_visit_with_num.remove(tv)
        to_visit.remove(coor_now)
        break
    if location == 'a' or location == 'S':
        break

print(number)