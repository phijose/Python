from os import system
import random
import re

class node:
    def __init__(self,data):
        self.d=data
        self.child=[]
        self.score=0

def chgmo(a):
    if a==1 or a==-1:
        print("!!! X wins !!!\n" if a==-1 else "!!! O wins !!!\n")
        exit()

def score(tt):
    if (tt[0]==tt[4]==tt[8] or tt[2]==tt[4]==tt[6]) and (tt[4]=='X' or tt[4]=='O'):
        return 1 if tt[4]=='O' else -1
    for i in range(3):
        if tt[i]==tt[i+3]==tt[i+6] and (tt[i]=='X' or tt[i]=='O'):
            return 1 if tt[i]=='O' else -1
        elif tt[i*3]==tt[i*3+1]==tt[i*3+2] and (tt[i*3]=='X' or tt[i*3]=='O'):
            return 1 if tt[i*3]=='O' else -1
    return 0

def adverserial(tt):
    player='O'
    opChange=''
    playerTree=node(tt)
    tpGen=[[playerTree]]
    for tpList in tpGen:
        spList=[]
        for tp in tpList:
            if tp.score==0:
                for i in [m.start() for m in re.finditer(' ', tp.d)]:
                    tpNode=node(tp.d[:i]+player+tp.d[i+1:])
                    tp.child.append(tpNode)
                    tpNode.score=score(tp.d[:i]+player+tp.d[i+1:])
            spList+=tp.child
        if spList:
            tpGen.append(spList)
        player='O' if player=='X' else 'X'
    player='O' if player=='X' else 'X'
    for i in tpGen[::-1]:
        for j in i:
            if j.child:
                tm = [k.score for k in j.child]
                opScore=max(tm) if player=='O' else min(tm)
                j.score=opScore
                opChange=j.child[tm.index(opScore)].d
        player='O' if player=='X' else 'X'
    return opChange

player=['X','O']
curPlayer=random.choice([0,1])
tictac='         '
while True:
    system('cls')
    print("\t Tic-Tac-Toe\n")
    for i in range(3):
        print(" {} | {} | {} ".format(tictac[i*3],tictac[i*3+1],tictac[i*3+2]))
        if i<2:
            print("---+---+---")
    print("")
    chgmo(score(tictac))
    if tictac.count(' ')==0:
        print("!!! Draw Match !!!\n")
        exit()
    if not curPlayer:
        mov=int(input("{} : ".format(player[curPlayer])))
        tictac=tictac[0:mov-1]+player[curPlayer]+tictac[mov:]
    else:
        tictac=adverserial(tictac)
    curPlayer=0 if curPlayer else 1