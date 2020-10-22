import random
def takeplayer():
    player=""
    while not(player.lower()=='r' or player.lower()=='p' or player.lower()=='s'):
        player=input("Enter player choice :- R | P | S ")
    return player.lower()

def getbot():
    lst=['r','p','s']
    return random.choice(lst)

def checkwinner(player,bot):
    if player=='r'and bot=='r':
        return "draw"
    elif player=='r'and bot =='p':
        return "bot"
    elif player=='r'and bot =='s':
        return "player"
    elif player=='p'and bot =='s':
        return "player"
    elif player=='p'and bot =='r':
        return "player"
    elif player=='p'and bot =='p':
        return "draw"
    elif player=='s'and bot =='r':
        return "bot"
    elif player=='s'and bot =='p':
        return "player"
    elif player=='s'and bot =='s':
        return "draw"
    else :
        return 'draw'


def rockpaperscissor():
    endgame='n'
    player_score=0
    bot_score=0
    while endgame.lower() != 'y':
        ply=takeplayer()
        bt=getbot()
        print("Bot entered: ",bt)
        winner=checkwinner(player=ply,bot=bt)
        if winner=='player':
            player_score+=2;
        elif winner=='bot':
            bot_score+=2
        else:
            player_score+=1;
            bot_score+=1
        print("------Score Board-------")
        print("-----Player-------::",player_score)
        print("-----Bot-------::", bot_score)
        endgame=input("Do you wont Exit game:(y/n)")


rockpaperscissor()