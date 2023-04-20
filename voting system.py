print("Your votes matters")
print("There are two candidates, Mr'X', Mr'Y' and if you want to quit 'E'")
Xcnt=0
Ycnt=0
c=1
while c<5:
    print("VOTER:",c)
    vote=input("cast your vote:")
    if vote=='X' or vote=='x':
        Xcnt=Xcnt+1
        print("thanks for voting")
    elif vote=='Y' or vote=='y':
        Ycnt=Ycnt+1
        print("thanks for voting")
    else:
        vote=='E' or vote=='e'
        print("Quit")
    c=c+1
print("Votings are closed now")
print(" Mr'X' has recieved",Xcnt,"votes")
print(" Mr'Y' has recieved",Ycnt, "votes")

if Xcnt<Ycnt:
         print("Mr'Y' wins by",Ycnt,"votes")
elif Xcnt>Ycnt:
         print("Mr'X' wins by",Xcnt,"votes")
else:
         Xcnt==Ycnt
         print("It's a draw")
