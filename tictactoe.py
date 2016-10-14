# coding: utf8
import copy
import random

# ------------------------------------------------------------------
def showBoard(T):
	counter=0
	for x in T:
		if(counter %3 ==0):
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
    countX = countO = 0
    for i in (0,3,6):
        if(T[i] == 1):
            countX +=1
        elif(T[i] == -1):
            countO +=1
        if(countX == 3):
            return 1
        elif(countO == 3):
            return -1
    countO=countX=0
    for i in (1, 4, 7):
        if (T[i] == 1):
            countX += 1
        elif (T[i] == -1):
            countO += 1
        if (countX == 3):
            return 1
        elif (countO == 3):
            return -1
    countO = countX = 0
    for i in (2, 5, 8):
        if (T[i] == 1):
            countX += 1
        elif (T[i] == -1):
            countO += 1
        if (countX == 3):
            return 1
        elif (countO == 3):
            return -1
    countO = countX = 0

    # COMPLETAR
    # testa as linhas
    for i in (0, 1, 2):
        # noinspection PyRedundantParentheses
        if (T[i] == 1):
            countX += 1
        elif (T[i] == -1):
            countO += 1
        if (countX == 3):
            return 1
        elif (countO == 3):
            return -1
    countO = countX = 0
    for i in (3, 4, 5):
        if (T[i] == 1):
            countX += 1
        elif (T[i] == -1):
            countO += 1
        if (countX == 3):
            return 1
        elif (countO == 3):
            return -1
    countO = countX = 0
    for i in (6, 7, 8):
        if (T[i] == 1):
            countX += 1
        elif (T[i] == -1):
            countO += 1
        if (countX == 3):
            return 1
        elif (countO == 3):
            return -1
    countO = countX = 0
    # COMPLETAR
	# testa as diagonais
    for i in (0, 4, 8):
        if (T[i] == 1):
            countX += 1
        elif (T[i] == -1):
            countO += 1
        if (countX == 3):
            return 1
        elif (countO == 3):
            return -1
    countO = countX = 0
    for i in (2, 4, 6):
        if (T[i] == 1):
            countX += 1
        elif (T[i] == -1):
            countO += 1
        if (countX == 3):
            return 1
        elif (countO == 3):
            return -1

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
def checkIfBlank(T):
    for x in T:
        if(x!=0):
            return False
    return True
# ------------------------------------------------------------------
def maxPlays(T):
    if(checkIfBlank(T)):
        a=random.randint(0,8)
        e=applyAction(T,a,'MAX')
        print('MAX joga para ', a)
    else:
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
	#T = [0,0,0,0,0,0,0,0,0]
	# we could have started from a latter state e.g.
	T = [1,-1,1,0,1,-1,0,0,-1]
	showBoard(T)
	while allowableActions(T) != [] and not isTerminal(T):
		T=p1(T)
		showBoard(T)
		if allowableActions(T) != [] and not isTerminal(T):
			T=p2(T)
			showBoard(T)
	# end
	if utility(T) == 1:
		print ('Player MAX wins!')
	elif utility(T) == -1:
		print ('Player MIN wins!')
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
        x = int(x)
    e = applyAction(T, x, 'HUMAN')
    print('You have chosen ', x)
    return e

# ------------------------------------------------------------------

# main

# max always wins? :
#Game(maxPlays,human_player)
# that's a draw:
Game(maxPlays,minPlays)
#Game(maxPlays,randomPlayer)


