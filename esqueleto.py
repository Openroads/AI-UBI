# coding: utf8
import copy
import random

# ------------------------------------------------------------------
def mostra_tabuleiro(T):
	# IMPLEMENTAR - wyrzuca tablice na screeen
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
# devolve a lista de ações que se podem executar partido de um estado
def acoes(T):
#IMPLEMENTAR - zwrocenie listy z mozliwymi pozycjami na tablicy
    possiblePosition=[]

    for x in range(0,len(T)):
        if(T[x]==0):
            possiblePosition.append(x)
    return possiblePosition
# ------------------------------------------------------------------
# devolve o estado que resulta de partir de um estado e executar uma ação
# a - action, jog - player
def resultado(T,a,jog):
    #mark=0 i dont know how it is possible
    aux = copy.copy(T)
    if(jog == 'MAX'):
        mark=1
    else:
        mark=-1
    aux[a] = mark
    return aux

# ------------------------------------------------------------------
# existem 8 possíveis alinhamentos vencedores, para cada jogador
def utilidade(T):
    # COMPLETAR

    # testa as colunas
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
# devolve True se T é terminal, senão devolve False
def estado_terminal(T):
    # IMPLEMENTAR
    value = utilidade(T)
    if( value == 1 or value == -1):
        return True
    else:
        for x in T:
            if (x == 0):
                return False
    return True
# ------------------------------------------------------------------
# algoritmo da wikipedia
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
# ignoramos a profundidade e devolvemos o valor, a ação e o estado resultante
def alfabeta(T,alfa,beta,jog):
    if estado_terminal(T):
        return utilidade(T),-1,-1
    if jog:
        v = -10
        ba=-1
        for a in acoes(T):
            v1,ac,es = alfabeta(resultado(T,a,'MAX'),alfa,beta,False)
            if v1 > v: # guardo a ação que corresponde ao melhor
                v = v1
                ba=a
            alfa = max(alfa,v)
            if beta <= alfa:
                break
        return v,ba,resultado(T,ba,'MAX')
    else:
        v = 10
        ba = -1
        for a in acoes(T):
            v1,ac,es = alfabeta(resultado(T,a,'MIN'),alfa,beta,True)
            if v1 < v:
                v = v1
                ba = a
            beta = min(beta,v)
            if beta <= alfa:
                break
        return v,ba,resultado(T,ba,'MIN')

# ------------------------------------------------------------------
def joga_max(T):
    v,a,e = alfabeta(T,-10,10,True)
    print ('MAX joga para ',a)
    return e

# ------------------------------------------------------------------
def joga_min(T):
# IMPLEMENTAR
    v, a, e = alfabeta(T, -10, 10, False)
    print('MIN joga para ', a)
    return e

# ------------------------------------------------------------------
def jogo(p1,p2):
# cria tabuleiro vazio
    T = [0,0,0,0,0,0,0,0,0]
    # podemos partir de um estado mais "avançado"
	#T = [1,-1,0,0,-1,0,1,0,0]
    mostra_tabuleiro(T)
    while acoes(T) != [] and not estado_terminal(T):
        T=p1(T)
        mostra_tabuleiro(T)
        if acoes(T) != [] and not estado_terminal(T):
            T=p2(T)
            mostra_tabuleiro(T)
    # fim
    if utilidade(T) == 1:
        print ('Venceu o jog1 - MAX')
        return 1
    elif utilidade(T) == -1:
        print ('Venceu o jog2')
        return -1
    else:
        print ('Empate')
        return 0

#------------------------------------------------------------------
# jogador aleatório
def joga_rand(T):
    x = random.randint(0,8)
	# COMPLETAR
    while(T[x] != 0):
        x = random.randint(0, 8)
    e = resultado(T,x,'RAND')
    print('RAND joga para ', x)
    return e

def human_player(T):
    print("You are O")
    x =int( input("Type position: "))
    while(x not in range(0,9) or T[x]!=0):
        x = input("It was not correct. Type position again: ")
        x=int(x)
    e = resultado(T, x, 'HUMAN')
    print('You have chosen ', x)
    return e

# ------------------------------------------------------------------
# main

# deve ganhar sempre o max:
jogo(joga_max,human_player)
#jogo(joga_max,joga_rand)
# devem empatar sempre:
#jogo(joga_max,joga_min)


