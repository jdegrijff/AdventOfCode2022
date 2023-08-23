import functions as f
input = f.openFile('006_input.txt')

letters = list(input)

used_letters = ""
attempt = 0

for letter in letters:
    used_letters = used_letters + letter
    last_fourteen = used_letters[-14:]
    last_fourteen_length = len(last_fourteen)
    last_fourteen_set = set(last_fourteen)
    last_fourteen_set_length = len(last_fourteen_set)
    attempt = attempt + 1

    if last_fourteen_length == 14 and last_fourteen_length == last_fourteen_set_length:
        answer = attempt
        break

print(answer)