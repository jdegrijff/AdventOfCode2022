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

    if stringup == "":
        stringup_list_max = -1
    else:
        stringup_list_max = max(stringup_list)

    if stringdown == "":
        stringdown_list_max = -1
    else:
        stringdown_list_max = max(stringdown_list)    

    if stringleft == "":
        stringleft_list_max = -1
    else:
        stringleft_list_max = max(stringleft_list)

    if stringright == "":
        stringright_list_max = -1
    else:
        stringright_list_max = max(stringright_list)

    if (int(string) > int(stringup_list_max) or 
        int(string) > int(stringdown_list_max) or 
        int(string) > int(stringleft_list_max) or 
        int(string) > int(stringright_list_max)):
            visible[index_num] = 1
            total_visible = total_visible + 1

print(total_visible)