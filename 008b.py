import functions as f

input = f.openFile('008_input.txt')
rows = input.split("\n")
columns = list(rows[0])
position = -1

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

index = []
visible = []
for row in rows:
    row_num = rows.index(row)
    for column in columns:
        column_num = columns.index(column)
        coordinate = ''.join(str(row_num)) + ":" + ''.join(str(column_num))
        index.append(coordinate)
        visible.append(0)

total_visible = 0
for i in index:
    index_num = index.index(i)
    split = i.split(":")
    row = int(split[0])
    column = int(split[1])
    string = columns[column][row:row+1]
    stringup = columns[column][:row]
    stringdown = columns[column][row+1:]
    stringleft = rows[row][:column]
    stringright = rows[row][column+1:]
    stringup_list = list(stringup)
    stringdown_list = list(stringdown)
    stringleft_list = list(stringleft)
    stringright_list = list(stringright)
    stringup_list.reverse()
    stringleft_list.reverse()
    max_down = 0
    max_up = 0
    max_left = 0
    max_right = 0
    number = 0 

    for d in stringdown_list:
        if int(d) >= int(string):
            number = number + 1
            break
        else:
            number = number + 1
    visible[index_num] = number

    number = 0 
    for u in stringup_list:
        if int(u) >= int(string):
            number = number + 1
            break
        else:
            number = number + 1
    visible[index_num] = visible[index_num] * number

    number = 0 
    for l in stringleft_list:
        if int(l) >= int(string):
            number = number + 1
            break
        else:
            number = number + 1
    visible[index_num] = visible[index_num] * number

    number = 0 
    for r in stringright_list:
        if int(r) >= int(string):
            number = number + 1
            break
        else:
            number = number + 1
    visible[index_num] = visible[index_num] * number
        
answer = max(visible)
print(answer)