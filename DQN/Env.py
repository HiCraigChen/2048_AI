import numpy as np
import random as rn
import math

'''
Set a 4x4 starting board containing two initial numbers.
The initial tile is either 2 or 4.
'''

def SetBoard():
    X = np.zeros((4,4))  
    A = (rn.randrange(4),rn.randrange(4))
    B = (rn.randrange(4),rn.randrange(4))
    while A == B:
        B = (rn.randrange(4),rn.randrange(4))
    if rn.random() > 0.5:
        X[A] = 4
    else:
        X[A] = 2

    if rn.random() > 0.5:
        X[B] = 4
    else:
        X[B] = 2
    return X

'''
Here defines the four possible moves in the game
moveR(matrix) : move tiles right
moveL(matrix) : move tiles left
moveU(matrix) : move tiles up
moveD(matrix) : move tiles down
'''
def moveR( Matrix ):
    reMatrix = np.zeros((4,4))
    for i in range(4):
        M = list(Matrix[i,:])
        Mplus=[]
        for j in range(M.count(0)):
            M.remove(0)
            j=j+1
        
        if len(M) == 0: 
            Mplus = [0,0,0,0]
        
        elif len(M) == 1:
            Mplus = [0,0,0]
            Mplus.append(M[0])

        
        elif len(M) == 2:
            if M[0]==M[1]:
                Mplus=[0,0,0]
                Mplus.append(M[0]+M[1])

            else:
                Mplus=[0,0]
                Mplus.append(M[0])
                Mplus.append(M[1])

        
        elif len(M) == 3:
            if M[1]==M[2]:
                Mplus = [0,0]
                Mplus.append(M[0])
                Mplus.append(M[1]+M[2])

            elif M[0] == M[1]:
                Mplus = [0,0]
                Mplus.append(M[0]+M[1])
                Mplus.append(M[2])

            else:        
                Mplus = [0]
                Mplus.append(M[0])
                Mplus.append(M[1])
                Mplus.append(M[2])
            
        elif len(M) == 4:
            if M[2]==M[3]:
                if M[0]==M[1]:
                    Mplus = [0,0]
                    Mplus.append(M[0]+M[1])
                    Mplus.append(M[2]+M[3])
                else:
                    Mplus = [0]
                    Mplus.append(M[0])
                    Mplus.append(M[1])
                    Mplus.append(M[2]+M[3])
            else: 
                if M[1]==M[2]:
                    Mplus = [0]
                    Mplus.append(M[0])
                    Mplus.append(M[1]+M[2])
                    Mplus.append(M[3])
                elif M[0] == M[1]:
                    Mplus = [0]
                    Mplus.append(M[0]+M[1])
                    Mplus.append(M[2])
                    Mplus.append(M[3])
                else:
                    Mplus = M
                
        for l in range(4):
            reMatrix[(i,l)] = Mplus[l]
            l = l+1
    return reMatrix


def moveL( Matrix ):
    reMatrix = np.zeros((4,4))
    for i in range(4):
        M = list(Matrix[i,:])
        Mplus=[]
        for j in range(M.count(0)):
            M.remove(0)
            j=j+1
        
        if len(M) == 0: 
            Mplus = [0,0,0,0]
        
        elif len(M) == 1:
            Mplus = [0,0,0]
            Mplus.insert(0,M[0])
        
        elif len(M) == 2:
            if M[0]==M[1]:
                Mplus=[0,0,0]
                Mplus.insert(0,M[0]+M[1])
                
            else:
                Mplus=[0,0]
                Mplus.insert(0,M[0])
                Mplus.insert(1,M[1])
        
        elif len(M) == 3:
            if M[0]==M[1]:
                Mplus = [0,0]
                Mplus.insert(0,M[0]+M[1])
                Mplus.insert(1,M[2])

            elif M[1] == M[2]:
                Mplus = [0,0]
                Mplus.insert(0,M[0])
                Mplus.insert(1,M[1]+M[2])

            else:        
                Mplus = M
                Mplus.append(0)
            
        elif len(M) == 4:
            if M[0]==M[1]:
                if M[2]==M[3]:
                    Mplus = [0,0]
                    Mplus.insert(0,M[0]+M[1])
                    Mplus.insert(1,M[2]+M[3])
                    
                else:
                    Mplus.append(M[0]+M[1])
                    Mplus.append(M[2])
                    Mplus.append(M[3])
                    Mplus.append(0)
                    
            else: 
                if M[1]==M[2]:
                    Mplus.append(M[0])
                    Mplus.append(M[1]+M[2])
                    Mplus.append(M[3])
                    Mplus.append(0)

                elif M[2] == M[3]:
                    Mplus.append(M[0])
                    Mplus.append(M[1])
                    Mplus.append(M[2]+M[3])
                    Mplus.append(0)
                else:
                    Mplus = M
                
        for l in range(4):
            reMatrix[(i,l)] = Mplus[l]
            l = l+1

    return reMatrix


def moveU( Matrix ):
    reMatrix = np.zeros((4,4))
    for i in range(4):
        M = list(Matrix[:,i])
        Mplus=[]
        for j in range(M.count(0)):
            M.remove(0)
            j=j+1
        
        if len(M) == 0: 
            Mplus = [0,0,0,0]
        
        elif len(M) == 1:
            Mplus = [0,0,0]
            Mplus.insert(0,M[0])
        
        elif len(M) == 2:
            if M[0]==M[1]:
                Mplus=[0,0,0]
                Mplus.insert(0,M[0]+M[1])
                
            else:
                Mplus=[0,0]
                Mplus.insert(0,M[0])
                Mplus.insert(1,M[1])
        
        elif len(M) == 3:
            if M[0]==M[1]:
                Mplus = [0,0]
                Mplus.insert(0,M[0]+M[1])
                Mplus.insert(1,M[2])

            elif M[1] == M[2]:
                Mplus = [0,0]
                Mplus.insert(0,M[0])
                Mplus.insert(1,M[1]+M[2])

            else:        
                Mplus = M
                Mplus.append(0)
            
        elif len(M) == 4:
            if M[0]==M[1]:
                if M[2]==M[3]:
                    Mplus = [0,0]
                    Mplus.insert(0,M[0]+M[1])
                    Mplus.insert(1,M[2]+M[3])
                    
                else:
                    Mplus.append(M[0]+M[1])
                    Mplus.append(M[2])
                    Mplus.append(M[3])
                    Mplus.append(0)
                    
            else: 
                if M[1]==M[2]:
                    Mplus.append(M[0])
                    Mplus.append(M[1]+M[2])
                    Mplus.append(M[3])
                    Mplus.append(0)

                elif M[2] == M[3]:
                    Mplus.append(M[0])
                    Mplus.append(M[1])
                    Mplus.append(M[2]+M[3])
                    Mplus.append(0)
                else:
                    Mplus = M
                
        for l in range(4):
            reMatrix[(l,i)] = Mplus[l]
            l = l+1

    return reMatrix


def moveD( Matrix ):
    reMatrix = np.zeros((4,4))
    for i in range(4):
        M = list(Matrix[:,i])
        Mplus=[]
        for j in range(M.count(0)):
            M.remove(0)
            j=j+1
        
        if len(M) == 0: 
            Mplus = [0,0,0,0]
        
        elif len(M) == 1:
            Mplus = [0,0,0]
            Mplus.append(M[0])

        
        elif len(M) == 2:
            if M[0]==M[1]:
                Mplus=[0,0,0]
                Mplus.append(M[0]+M[1])

            else:
                Mplus=[0,0]
                Mplus.append(M[0])
                Mplus.append(M[1])

        
        elif len(M) == 3:
            if M[1]==M[2]:
                Mplus = [0,0]
                Mplus.append(M[0])
                Mplus.append(M[1]+M[2])

            elif M[0] == M[1]:
                Mplus = [0,0]
                Mplus.append(M[0]+M[1])
                Mplus.append(M[2])

            else:        
                Mplus = [0]
                Mplus.append(M[0])
                Mplus.append(M[1])
                Mplus.append(M[2])
            
        elif len(M) == 4:
            if M[2]==M[3]:
                if M[0]==M[1]:
                    Mplus = [0,0]
                    Mplus.append(M[0]+M[1])
                    Mplus.append(M[2]+M[3])
                else:
                    Mplus = [0]
                    Mplus.append(M[0])
                    Mplus.append(M[1])
                    Mplus.append(M[2]+M[3])
            else: 
                if M[1]==M[2]:
                    Mplus = [0]
                    Mplus.append(M[0])
                    Mplus.append(M[1]+M[2])
                    Mplus.append(M[3])
                elif M[0] == M[1]:
                    Mplus = [0]
                    Mplus.append(M[0]+M[1])
                    Mplus.append(M[2])
                    Mplus.append(M[3])
                else:
                    Mplus = M
                
        for l in range(4):
            reMatrix[(l,i)] = Mplus[l]
            l = l+1
    return reMatrix




'''
Rate the Matrix for generating the reward. 

Function Rate_With_Human_Decision is based on the strategy of 2048 game.
Put the largest tile in the corner is more likely to get higher score.
Thus, I let the weight in the top-right corner higher.
The decision that AI makes will lead larger tiles more likely toward to top-right corner.

Function Rate is based on the number on the tiles.
It's like the original game scoring method. 
'''
def Rate_With_Human_Decision(matrice):
    r = 0.0025
    score = 0
    for i in range(4):
        for j in range(4):
            score += matrice[(i,j)]* (r**(3-j))*(4-i)*(4-i)
    return score

def Rate(matrice):
    score = 0
    for i in range(4):
        for j in range(4):
            x = matrice[(i,j)]
            if x > 0:
                k = math.log2(x)
                #score += (k-1)*2**(2*k)
                score += x*(k-1)
            else:
                pass            
    return score

def normalRate(matrice):
    return np.sum(matrice)    



'''
Add a new number in the matrix.
After each move, the game generates a new tile with 50% 2 and 50% 4.
If there is no empty space to add a new tile (i.e. game over), return 'Done'.
'''
def AddNew(Matrix):
    zeroPos = []
    for i in range(4):
        for j in range(4):
            if Matrix[i,j] == 0:
                zeroPos.append([i,j])
    try:
        q = rn.randrange(len(zeroPos))
        P = tuple(zeroPos[q])

        if rn.random() > 0.1:
            Matrix[P] = 2
        else : 
            Matrix[P] = 4
        return Matrix
    except ValueError:
        return 'Done'


'''
Check whelther the move is legal or not. 

Legal move : The move changes the broad condition.

Illegal move : After each move, the broad remains the same.
'''
def State_Check(Matrix):
    Ways_can_go = []
    R = moveR(Matrix)
    L = moveL(Matrix)
    U = moveU(Matrix)
    D = moveD(Matrix)
    Ways_can_go.append(0 if (R == Matrix).all() else 1)
    Ways_can_go.append(0 if (L == Matrix).all() else 1)
    Ways_can_go.append(0 if (U == Matrix).all() else 1)
    Ways_can_go.append(0 if (D == Matrix).all() else 1)
    return Ways_can_go

'''
Plot a graph to see the distribution.
'''
def Plot(Counter):
    print(Counter)
    Max_reach = [0,0,0,0,0,0,0,0,0,0,0,0]
    Num = []
    Num_N = []
    for i in range(0,12):
        Tag = 2**(i+3)
        Num.append(i)
        Num_N.append(str(Tag))
        #Max_reach.append(Counter[str(Tag)+'.0'])
        try:
            Max_reach[i] = Counter[str(Tag)+'.0']
        except KeyError:
            pass

    import matplotlib.pyplot as plt
    plt.bar(Num, Max_reach, tick_label=Num_N)
    plt.ylabel('Reach(times)')
    plt.xlabel('Number')
    plt.show()





