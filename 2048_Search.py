import numpy as np
from Env import *
import math 
'''
Choice the action that reaches the highest score from the results in movecheck plus n times 1-step move results.
The reason why I add n times 1-step move results is to put more emphasis on the score we can get in the next move.
Do the action and add a new tile on the broad.
'''
def move(Matrix, depth):

    Choice = movecheck(Matrix, depth)
    Ways  = State_Check(Matrix)
    matrix_list=[moveR(Matrix),moveL(Matrix),moveU(Matrix),moveD(Matrix)]
    for i in range(len(Choice)):
        if Ways[i] == 0:
            Choice[i] = -math.inf
    Choice[1] *= 0.5   # Want to make the biggest tile on the top-right
    child = np.zeros((4,4))
    way = np.argmax(Choice)
    child = AddNew(matrix_list[way])
    return child


'''
Search every possible steps and record the max scores in certain depth.
Return a list with length 4 which stores the scores from first 4 different steps.
'''
def movecheck(Matrix, depth):
    if depth == 0:
        return Rate_With_Human_Decision(Matrix) if AddNew(Matrix) != 'Done' else 0
    else:
        matrix_score_list = [0,0,0,0]        
        matrix_list=[moveR(Matrix),moveL(Matrix),moveU(Matrix),moveD(Matrix)]
        
        for i, elements in enumerate(matrix_list):
            matrix_list[i] = AddNew(matrix_list[i])
            if elements == "Done":
                matrix_score_list[i] = 0
                continue
            matrix_score_list[i] = Rate(elements) + np.max(movecheck(elements,depth-1))
        
        return matrix_score_list


'''
Play the game!
Give the time you want to play (epoch) and the depth you want to search.
It will print out every moved broad on your terminal.
'''
def play(epoch, depth):
    # Info
    print('epoch:',epoch)
    print('depth:',depth)

    counter = {}
    for i in range(epoch):
        print(i)
        X = SetBoard()
        step = 0
        while True:
            child = move(X,depth)

            if child == 'Done':
                break
            
            Max_reach = child.max()
            X = child
        
        if str(Max_reach) in counter:
            counter[str(Max_reach)] += 1
        else:
            counter[str(Max_reach)] = 1
    Plot(counter)
if __name__ == '__main__':
    play(10000,1)



