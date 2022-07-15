
engine = [["_","_","_"],["_","_","_"],["_","_","_"]]
possiblecall = ["A1","B1","C1","A2","B2","C2","A3","B3","C3"]
player1 = ""
player2 = ""
roundcount = 0

gamewon = False

def startgame():
    print("Let's play tic-tac-toe")
    a = input("What is player 1 name ? ")
    b = input("What is player 2 name ? ")
    for s in engine: print(s)
    print(f"""Ok {a} and {b}, the rule is simple, just announce the case you want to play by typing the coordinate, the lines are named A,B and C, the column are named 1,2 and 3. 
For exemple, if I want to play the middle case, i'll type B2, if I want to play the top right case, I'll type A3, first to align tree cases win """)
    return a, b


def playgame1():
    currentplayer = ""
    mk = roundcount % 2
    if mk == 0 : currentplayer = player1
    else : currentplayer = player2
    marks = ["X","O"]
    x = input(f"{currentplayer}, what do you play ? ").upper()
    a = x[0]
    b = int(x[1])-1
    w = 5

    if a == "A" : w = 0
    elif a == "B" : w = 1
    elif a == "C" : w = 2
    if x not in possiblecall: 
        print ("Not a valid case, try again")
        playgame1()
    else:
        possiblecall.remove(x)
        engine[w][b] = marks[mk]
        for s in engine: print(s)
    return currentplayer
        
def checkwin():  
    global gamewon
    for x in engine :
        if x == ["X","X","X"] or x == ["O","O","O"]: gamewon = True
    for x in range(3):
        if engine[0][x] == engine[1][x] and engine[0][x] == engine[2][x] and engine[0][x] != "_": gamewon = True
    if engine[0][0] == engine[1][1] and engine[0][0] == engine[2][2] and engine[2][2] != "_" : gamewon = True
    if engine[0][2] == engine[1][1] and engine[0][2] == engine[2][0] and engine[2][0] != "_" : gamewon = True



    
player1, player2 = startgame()

while roundcount <= 9:
    if gamewon == False:
        currentplayer =playgame1()
        checkwin()
    else : print (f"Congratulation {currentplayer}, you win the game !!") ; break
    roundcount +=1
if gamewon == False : print("Oh no ! It's a draw...")   

