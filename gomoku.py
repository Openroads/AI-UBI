# coding: utf8
import copy
import random
import time
# ------------------------------------------------------------------



def showBoard(T):
	counter=0
	for x in T:
		if(counter %15 ==0):
			print("\n")

		counter +=1

		if(x == 0):
			print(".",end="\t")
		elif(x == 1):
			print("X",end="\t")
		else:
			print("O",end="\t")
	print("\n")

# ------------------------------------------------------------------
# given a state, returns the list of allowable actions
def allowableActions(T):
    possiblePosition=[]

    for x in range(0,len(T)):
        if(T[x]==0):
        	possiblePosition.append(x)
    return possiblePosition

# ------------------------------------------------------------------
# returns the new state after applying an action
def applyAction(T,a,jog):

	#mark=0 i dont know how it is possible
    aux = copy.copy(T)
    if(jog == 'MAX'):
        mark=1
    else:
        mark=-1
    aux[a] = mark
    return aux

# ------------------------------------------------------------------
# check the end game situations
# noinspection PyRedundantParentheses
def utility(T):
    boardsize = 15
    countX = 0
    countO = 0
    rightFrame  =   [x for x in range(14,225,15)]
    leftFrame   =   [x for x in range(0,210,15)]
#------------------Test for line-----------------
    x=0
    while(x < len(T)):
        #looking for X terminal state
        while(T[x] == 1):
            countX += 1
            if (x in rightFrame):
                break
            x += 1
        # looking for O terminal state
        while (T[x] == -1):
            countO += 1
            if (x in rightFrame):
                break
            x += 1
        if(countO == 5):
            return -1
        elif(countX==5):
            return 1

        countX = countO = 0

        x += 1
#----------------Test for column------------
    for i in range(boardsize):
        x = i
        while(x < len(T)):
            while (T[x] == 1):
                countX += 1
                if (x >= len(T)-15):
                    countX = 0
                    break
                x += 15
                # looking for O terminal state
            while (T[x] == -1):
                countO += 1
                if (x >= len(T)-15):
                    countO = 0
                    break
                x += 15
            if (countO == 5):
                return -1
            elif (countX == 5):
                return 1

            countX = countO = 0

            x += 15

#------------- Test for diagonal terminal state ------
    for x in range(4, boardsize):
        while(x not in rightFrame):
            #T[x]=-1
            #showBoard(T)
            #time.sleep(0.5)
            #T[x]=0
            while(T[x] == 1):
                countX += 1
                if(x in leftFrame):
                    break
                x += 14
            while (T[x] == -1):
                countO += 1
                if (x in leftFrame):
                    break
                x += 14


            if (countO == 5):
                return -1
            elif (countX == 5):
                return 1

            countX = countO = 0
            x += 14
    for x in range(210,221):
        while(x not in leftFrame):
            while (T[x] == 1):
                countX += 1
                if (x in rightFrame):
                    break
                x -= 14
            while (T[x] == -1):
                countO += 1
                if (x in rightFrame):
                    break
                x -= 14
            if (countO == 5):
                return -1
            elif (countX == 5):
                return 1

            countX = countO = 0
            x-=14

    rightFrameSpecial= [x +16 for x in rightFrame]
    for x in range(0,12):
        while(x not in rightFrameSpecial):
            while (T[x] == 1):
                countX += 1
                if (x in rightFrame):
                    break
                x += 16
            while (T[x] == -1):
                countO += 1
                if (x in rightFrame):
                    break
                x += 16
            if (countO == 5):
                return -1
            elif (countX == 5):
                return 1

            countX = countO = 0
            x+=16
    leftFrameSpecial=[x - 16 for x in leftFrame]
    for x in range(214,224):
        while(x not in leftFrameSpecial):
            while (T[x] == 1):
                countX += 1
                if (x in leftFrame):
                    break
                x -= 16
            while (T[x] == -1):
                countO += 1
                if (x in leftFrame):
                    break
                x -= 16
            if (countO == 5):
                return -1
            elif (countX == 5):
                return 1

            countX = countO = 0
            x -= 16


    return 0


# ------------------------------------------------------------------
# boolean function, true if we have reached a terminal state
def isTerminal(T):
    value = utility(T)
    if value == 1 or value == -1:
        return True
    else:
        for x in T:
            if (x == 0):
                return False
    return True


# ------------------------------------------------------------------
# see
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
#
def alfabeta(T, alfa, beta, player):
    if isTerminal(T):
        return utility(T), -1, -1
    if player:
        v = -10
        ba = -1
        for a in allowableActions(T):
            v1, ac, es = alfabeta(applyAction(T, a, 'MAX'), alfa, beta, False)
            if v1 > v:  # keep the best action
                v = v1
                ba = a
            alfa = max(alfa, v)
            if beta <= alfa:
                break

        return v, ba, applyAction(T, ba, 'MAX')
    else:
        v = 10
        ba = -1
        for a in allowableActions(T):
            v1, ac, es = alfabeta(applyAction(T, a, 'MIN'), alfa, beta, True)
            if v1 < v:
                v = v1
                ba = a
            beta = min(beta, v)
            if beta <= alfa:
                break
        return v,ba,applyAction(T,ba,'MIN')

# ------------------------------------------------------------------
def maxPlays(T):
    v,a,e = alfabeta(T,-10,10,True)
    print ('MAX joga para ',a)
    return e

# ------------------------------------------------------------------
def minPlays(T):
    v, a, e = alfabeta(T, -10, 10, False)
    print('MIN joga para ', a)
    return e

# ------------------------------------------------------------------
def Game(p1,p2):
    # empty board
    print("Chose size of board")
    s=15 #s=int(input("Type size:"))
    n=s**2
    T=[0]*n
    #T = [0,0,0,0,0,0,0,0,0]
    # we could have started from a latter state e.g.
    #T = [1,-1,0,0,-1,0,1,0,0]
    showBoard(T)
    print("e")
    while allowableActions(T) != [] and not isTerminal(T):
	    T=p1(T)
	    showBoard(T)
	    if allowableActions(T) != [] and not isTerminal(T):
		    T=p2(T)
		    showBoard(T)
    # end
    if utility(T) == 1:
        print ('Player1 wins!')
    elif utility(T) == -1:
        print ('Player1 wins!')
    else:
        print ('Draw!!!')

# ------------------------------------------------------------------
# random player
def randomPlayer(T):
    x = random.randint(0,8)
    while(T[x] != 0):
        x = random.randint(0, 8)
    e = applyAction(T,x,'RAND')
    print('RAND joga para ', x)
    return e
# ------------------------------------------------------------------

# noinspection PyRedundantParentheses
def human_player(T):
    print("You are O")
    x =int( input("Type position: "))
    while(x not in range(0, 9) or T[x] != 0):
        x = input("It was not correct. Type position again: ")
        x=int(x)
    e = applyAction(T, x, 'HUMAN')
    print('You have chosen ', x)
    return e

# ------------------------------------------------------------------

# main

# max always wins? :
#Game(maxPlays,randomPlayer)
# that's a draw:
Game(maxPlays,minPlays)

