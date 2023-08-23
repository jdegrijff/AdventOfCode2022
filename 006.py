import functions as f

input = f.openFile('006_input.txt')

letters = list(input)

used_letters = ""
attempt = 0
answer = 0

for letter in letters:
    used_letters = used_letters + letter
    last_four = used_letters[-4:]
    last_four_length = len(last_four)
    one = last_four[0:1]
    two = last_four[1:2]
    three = last_four[2:3]
    four = last_four[3:4]
    one_count = last_four.count(one)
    two_count = last_four.count(two)
    three_count = last_four.count(three)
    four_count = last_four.count(four)
    total = one_count + two_count + three_count + four_count
    attempt = attempt + 1

    if last_four_length == 4 and total == 4:
        answer = attempt
        break

print(answer)