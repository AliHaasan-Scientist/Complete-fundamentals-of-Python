def game():
    return 10000


score = game()
# read score:
with open('09.File Input & Output\score.txt', 'r') as r:
    a = int(r.read())

if a < score:
    with open('09.File Input & Output\score.txt', 'w') as w:
        w.write(str(score))
