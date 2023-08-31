import functions as f

input = f.openFile('007_input.txt')
actions = input.split("\n")

path = ""
list = []
size = []
totalsize = []
closest_to_zero = []
dir = 0
last_folder_start = 0

for action in actions:
    steps = action.split(" ")
    if steps[0] == "$":
      if steps[1] == "cd":
        if steps[2] == "..":
          last_folder_start = path.rfind("-")
          path = path[:last_folder_start]             
        if steps[2] != "..":
          try:
             index_value = list.index(steps[2])
          except ValueError or IndexError:
              index_value = -1
          if index_value < 0:
            path = path + "-" + steps[2]
          else:
            path = list[index_value]

      if steps[1] == "ls":
          list.append(path)
          size.append(0)
          totalsize.append(0)
          closest_to_zero.append(0)
    
    elif steps[0] == "dir":
      path = path

    else:
      position = list.index(path)
      increase = int(steps[0])
      size[position] = size[position] + increase

for l1 in list:
  ts = 0
  n1 = l1
  index1 = list.index(n1)
  for l2 in list:
    n2 = l2
    index2 = list.index(n2)
    if n1 == n2:
      ts = ts + size[index2]
    if n1 + "-" in n2:
      ts = ts + size[index2]

    totalsize[index1] = ts

answer = 0
for totalsiz in totalsize:
  if totalsiz <= 100000:
     answer = answer + totalsiz
  else:
     answer = answer

full_disk = 70000000
space = full_disk - totalsize[0]
space_needed = 30000000 - space
for l3 in list:
  index3 = list.index(l3)
  ctz = totalsize[index3] - space_needed
  if ctz < 0:
    closest_to_zero[index3] = full_disk
  else:
    closest_to_zero[index3] = ctz

low = min(closest_to_zero)
answer = low + space_needed

print(answer)