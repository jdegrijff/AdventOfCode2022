import functions as f

def outcome(game):
    if game == 'A X':
        return 3+0
    if game == 'A Y':
        return 1+3
    if game == 'A Z':
        return 2+6
    if game == 'B X':
        return 1+0
    if game == 'B Y':
        return 2+3
    if game == 'B Z':
        return 3+6
    if game == 'C X':
        return 2+0
    if game == 'C Y':
        return 3+3
    if game == 'C Z':
        return 1+6
    
input = f.openFile('002_input.txt')

games = input.split("\n")
print(games[0])

result = 0
for game in games:
    result=result+outcome(game)

print(result)