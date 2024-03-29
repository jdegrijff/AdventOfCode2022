import functions as f
import math

input = f.openFile('011_input.txt')
list = input.split("\n")
monkey_list = []
inventory_list = []
check_list = []
to_if_true_list = []
to_if_wrong_list = []
operation_list = []
counter = []
worry_level = 1 
rounds = range(0,10000)

for l in list:
    # if l.find("Starting items") > -1:
    if "Starting items" in l:
        inventory_list.append(l[18:])
    if l.find("Monkey") > -1:
        monkey_list.append(l[-2:-1])
        counter.append(0)
    if l.find("divisible") > -1:
        check_list.append(int(l[21:]))
    if l.find("true") > -1:
        to_if_true_list.append(l[29:])
    if l.find("false") > -1:
        to_if_wrong_list.append(l[29:])
    if l.find("Operation") > -1:  
        operation_list.append(l)
prime_number = math.prod(check_list)

for r in rounds:
    for m in monkey_list:
        index = monkey_list.index(m)
        items = inventory_list[index]
        item_list = items.split(", ")
        actions = operation_list[index].split(" ")
        monkey = monkey_list[index]
        check = check_list[index]
        true = to_if_true_list[index]
        wrong = to_if_wrong_list[index]
        for item in item_list:
            if items == '':
                break
            else:
                if actions[7] == "old":
                    new = math.floor((int(item) * int(item)) / worry_level)
                else:
                    if actions[6] == "*":
                        new = math.floor((int(item) * int(actions[7])) / worry_level)
                    if actions[6] == "+":
                        new = math.floor((int(item) + int(actions[7])) / worry_level)
                new = new % prime_number
                sum = new / int(check)
                counter[index] = counter[index] + 1
                if sum.is_integer():
                    inventory_list[int(true)] = inventory_list[int(true)] + ", " + str(new)
                else:
                    inventory_list[int(wrong)] = inventory_list[int(wrong)] + ", " + str(new)

        inventory_list[index] = ""

        for inv in inventory_list:
            index = inventory_list.index(inv)
            if inv.find(",") == 0:
                inventory_list[index] = inv[2:]

counter.sort()
answer = counter[int(m)-1] * counter[int(m)]
print(answer)