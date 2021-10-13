print("\U0001F929 \U0001F929 \U0001F929 Welcome to Rock,Paper,Scissors game\U0001F929 \U0001F929 \U0001F929 ")
def game(comp,player):
    if comp==player:
        return None
    elif comp=='r' or comp=='R':
        if player=='p' or player=='P':
            return True
        elif player=='s' or player=='S':
            return False
    elif comp=='p' or comp=='P':
        if player=='s' or player=='S':
            return True
        elif player=='r' or player=='R':
            return False
    elif comp=='s' or comp=='S':
        if player=='r' or player=='R':
            return True
        elif player=='p' or player=='P':
            return False
import random
randno=random.randint(1,3)
begin="Game is started"
print(begin.center(len(begin)+6,"*"))
if randno==1:
    comp='r' or comp=='R'
elif randno==2:
    comp='p' or comp=='P'
else:
    comp='s' or comp=='S'
player=input("Enter your choice rock(r) or paper(p) or scissors(s):-")
a=game(comp,player)
print(f"Comp choice {comp}")
print(f"Your's choice {player}")
if a==None:
    print("Game is Tie")
elif a:
    print("You Win \U0001F973")
else:
    print("You Lost \U0001F62D")