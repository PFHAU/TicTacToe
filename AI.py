
#this is the global variable that will count the number of nodes that the algorithm will calculate
total=0

#Generic Functions

def printGame(game, isAiX):
    print(printCase(game[0], isAiX)+printCase(game[1], isAiX)+printCase(game[2], isAiX))
    print(printCase(game[3], isAiX)+printCase(game[4], isAiX)+printCase(game[5], isAiX))
    print(printCase(game[6], isAiX)+printCase(game[7], isAiX)+printCase(game[8], isAiX))

#isAiX is True if AI plays the X      
def printCase(case, isAiX):
    if case == 0 :
        return(".")
    if case == 1 and isAiX :
        return("X")
    if case == 1 and isAiX == False:
        return("O")
    if case == -1 and isAiX:
        return("O")
    if case == -1 and isAiX == False:
        return("X")


#p is a state of the board 
# return the value of the winner if the board is an end board, otherwise it returns False
def final(p):

    #lines check
    for i in range(0,9,3):
        if p[i]!=0 and (p[i]==p[i+1] and p[i+1]==p[i+2]):
            return p[i]
    #columns check
    for i in range(0,3):
        if p[i]!=0 and (p[i]==p[i+3] and p[i+3]==p[i+6]) :
            return p[i]
    #diagonals check
    if ((p[2]!=0 and p[2]==p[4] and p[4]==p[6]) or (p[0]!=0 and p[0]== p[4] and p[4]==p[8])):
        #if it's a diagonal win , p[4] is always the right symbol
        return p[4]
    
    #if it's a draw
    if 0 not in p :
        #if we return 0, when we will verify if it's equal to False in minMaxStart/alphaBetaStart, that will be true (in python 0==False)
        return 2
    return False

#Xturn is True if it's the turn of X
def suiv(state, Xturn):
    res=list()
    value=-1
    if Xturn :
        value=1

    for i in range(0,9):
        stateTmp=state.copy()
        if state[i]==0:
            stateTmp[i]=value
            res.append(stateTmp)
    return res

def endGame(x):
    if x==2:
        print("It's a Draw!")
    elif x==1:
        print("X win!")
    elif x==-1:
        print("O win!")

################################################

#MiniMax algorithms:

#The Game
def minMaxStart():
    global total
    player=input("Choose X or O (X begin)")
    while player!='X' and player!='O':
        player= input('Wrong enter, please enter X or O')
    print('You choose ' + player)
    state=[0,0,0,0,0,0,0,0,0]
    

    if player=='O':
        while(final(state)==False):
            #minimax turn:
            print("minmax play:")
            newState=decisionMinMax(state)[1]
            print("number of node: "+ str(total))
            total=0
            state=newState.copy()
            printGame(state, True)
            print(state)
            #if the AI doesn't win on his turn, player can play
            if final(state)==False:
                print("Your Turn:")
                while(True):
                    p=int(input("enter a case number (1 to 9) that is not taken"))
                    if p>0 and p<10 and state[p-1]==0:
                        #The player is O so we add -1 on his play
                        state[p-1]=-1
                        #The player played, we can finish his turn
                        break
                printGame(state, True)
                print(state)
            else:
                endGame(final(state))
                return True
        #end of this while mean end of player turn
        endGame(final(state))
        return True

    if player=='X':
        while(final(state)==False):
            printGame(state, False)
            print(state)
            print("Your Turn:")
            while(True):
                p=int(input("enter a case number (1 to 9) that is not taken"))
                if p>0 and p<10 and state[p-1]==0:
                    #The player is X so we add 1 on his play
                    state[p-1]=-1
                    #The player played, we can finish his turn
                    break
            #if the player doesn't win on this turn, the AI can play
            if final(state)==False:
                #minimax turn:
                print("minmax play:")
                newState=decisionMinMax(state)[1]
                print("number of node: "+ str(total))
                total=0
                state=newState.copy()   
            else:
                endGame(final(state))
                return True
        #end of this while mean end of minimax turn
        endGame(final(state))
        return True   

def decisionMinMax(state):
    v=valeurMax(state)
    return v

def valeurMax(state):
    global total
    fin=final(state)
    if fin!=False:
        return (fin,state)
    v=-99999
    bestPlay2=[0,0,0,0,0,0,0,0,0]
    child=[0,0,0,0,0,0,0,0,0]
    for child in suiv(state, True):
        total=total+1
        (VMC,bestPlay)=valeurMin(child)
        if v<VMC:
            v=VMC
            bestPlay2=child
    return (v,bestPlay2)

def valeurMin(state):
    global total
    fin=final(state)
    if fin:
        return (fin,state)
    v=99999
    bestPlay2=[0,0,0,0,0,0,0,0,0]
    child=[0,0,0,0,0,0,0,0,0]
    for child in suiv(state, False):
        total=total+1
        (VMC,bestPlay)=valeurMax(child)
        if v>VMC:
            v=VMC
            bestPlay2=child
    return (v,bestPlay2)

#################################################

#Algorithme alpha-beta


#the Game
def alphaBetaStart():
    global total
    player=input("Choose X or O (X begin)")
    while player!='X' and player!='O':
        player= input('Wrong enter, please enter X or O')
    print('You choose ' + player)
    state=[0,0,0,0,0,0,0,0,0]
    

    if player=='O':
        while(final(state)==False):
            #alpha-beta Turn:
            print("alpha-beta play:")
            newState=decisionAlphaBeta(state)[1]
            print("number of node: "+ str(total))
            total=0
            state=newState.copy()
            printGame(state, True)
            #if the AI doesn't win on this turn, the player can play
            if final(state)==False:
                print("Your Turn:")
                while(True):
                    p=int(input("enter a case number (1 to 9) that is not taken"))
                    if p>0 and p<10 and state[p-1]==0:
                        #The player is O so we add -1 on his play
                        state[p-1]=-1
                        #The player played, we can finish his turn
                        break
                printGame(state, True)
            else:
                endGame(final(state))
                return True
        #end of this while mean end of player turn
        endGame(final(state))
        return True

    if player=='X':
        while(final(state)==False):
            printGame(state, False)
            print("Your Turn:")
            while(True):
                p=int(input("enter a case number (1 to 9) that is not taken"))
                if p>0 and p<10 and state[p-1]==0:
                    #The player is X so we add 1 on his play
                    state[p-1]=-1
                    #The player played, we can finish his turn
                    break
            #if the player doesn't win on this turn, the AI can play
            if final(state)==False:
                #alpha-beta turn:
                print("alpha-beta play:")
                newState=decisionAlphaBeta(state)[1]
                print("number of node: "+ str(total))
                total=0
                state=newState.copy()   
            else:
                endGame(final(state))
                return True
        #end of this while mean end of alpha-beta turn
        endGame(final(state))
        return True

def decisionAlphaBeta(state):
    v=valeurMaxAB(state, -99999, 99999)
    return v

def valeurMaxAB(state, alpha, beta):
    global total
    fin=final(state)
    if fin!=False:
        return (fin,state)
    v=-99999
    bestPlay2=[0,0,0,0,0,0,0,0,0]
    child=[0,0,0,0,0,0,0,0,0]
    for child in suiv(state, True):
        total=total+1
        (VMC,bestPlay)=valeurMinAB(child, alpha, beta)
        if v<VMC:
            v=VMC
            bestPlay2=child
        alpha=max(alpha, VMC)
        if beta<=alpha:
            break
    return (v,bestPlay2)

def valeurMinAB(state, alpha, beta):
    global total
    fin=final(state)
    if fin:
        return (fin,state)
    v=99999
    bestPlay2=[0,0,0,0,0,0,0,0,0]
    child=[0,0,0,0,0,0,0,0,0]
    for child in suiv(state, False):
        total=total+1
        (VMC,bestPlay)=valeurMaxAB(child, alpha, beta)
        if v>VMC:
            v=VMC
            bestPlay2=child
        beta = min(beta, VMC)
        if beta <= alpha:
            break
    return (v,bestPlay2)

#############################################

def demarre(choix):
    if choix==1:
        minMaxStart()
        return True
    elif choix==0:
        alphaBetaStart()
        return True
    else:
        print("Wrong enter. Must be 1 (minimax) or 0 (alpha-beta)")
        return False
    

def Main():
    print(" Welcome! This is Tic-Tac-Toe VS AI")
    print(" Please select an algorithm that you want to play against")
    print("1. MiniMax")
    print("0. Alpha-Beta")
    choix=int(input("Your choice: "))
    demarre(choix)

Main()
    