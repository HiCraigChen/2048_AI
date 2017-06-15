import numpy as np
import random as rn
from Brian_Keras import DeepQNetwork
from Env import *

def run():
    step = 0
    counter = {}
    for episode in range(150000):
        # initial observation
        observation = SetBoard() 
        while True:
            Actions = ['R','L','U','D']
            
            # RL choose action based on observation
            action,action_value = RL.choose_action(observation)

            if action == 0:
                observation_ = moveR(observation)
            elif action == 1:
                observation_ = moveL(observation)
            elif action == 2:
                observation_ = moveU(observation)
            elif action == 3:
                observation_ = moveD(observation)


            observation_ = AddNew(observation_)

            if observation_ == 'Done':
                reward = -Rate(observation)
                RL.store_transition(observation, action, reward, observation)


                # Print the Game over broad
                # Every 100 episode
                # Every time reach 512
                if episode%100 ==0:
                    print(episode)
                    print(observation)

                if (observation > 511).any():
                    print('----------\n',episode,'\n',observation,'\n----------')
                break
            
            reward = Rate(observation_)
            RL.store_transition(observation, action, reward, observation_)
            if (step > 200) and (step % 5 == 0):
                RL.learn()

            # swap observation
            observation = observation_
            step += 1
            Max_reach = observation.max()
        
        if str(Max_reach) in counter:
            counter[str(Max_reach)] += 1
        
        else:
            counter[str(Max_reach)] = 1
    
    
    
    # end of game
    RL.Save()
    print('game over')
    Plot(counter)
    
'''
Build the Neural Network.
n_actions = 4
In the 2048 game, we have four actions : Up, Down, Left, Right.

n_features = 16
In the game, a braod observation contains 16 tiles.
'''

if __name__ == "__main__":
    RL = DeepQNetwork(n_actions=4, 
                      n_features=16,
                      learning_rate=0.001,
                      reward_decay=0.7,
                      e_greedy=0.99,
                      replace_target_iter=100,
                      memory_size=100000,
                      # output_graph=True
                      )

    # Load the model, countinue the previous training.
    #RL.Load() 
    
    run()

    # Plot the result.
    RL.plot_acc()