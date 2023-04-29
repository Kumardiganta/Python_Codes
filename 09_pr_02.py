
def game():
    return 5699

score=game()
with open ('highscore.txt') as f:
    hiScoreStr=(f.read())

if hiScoreStr=='':
    with open ('highscore.txt','w') as f:
        f.write(str(score))
elif int(hiScoreStr)<score:
    with open ('highscore.txt','w') as f:
        f.write(str(score))