import numpy as np
import random as rn
#from Brian_NN import DeepQNetwork
from Env import *
from DQN_CNN import DeepQNetwork

def run():
    step = 0
    #reward_step = 2
    counter = {}
    for episode in range(300):
        # initial observation
        observation = SetBoard() 
        while True:
            #Actions = ['R','L','U','D']
            Max_reach = observation.max()
            ways = State_Check(observation)
            # RL choose action based on observation
            # Normalize the observation
            #action,action_value = RL.choose_action(observation)
            action,action_value = RL.choose_action(observation/Max_reach)
            #action,action_value = RL.choose_action_mix(observation/Max_reach)
            # action,action_value = RL.choose_action_remove_state_check(observation/Max_reach)
            # loop = 0
            # while ways[action] == 0 and ways != [0,0,0,0]:
            #     reward = -(loop+1)*Rate(observation)
            #     RL.store_transition(observation/Max_reach, action, reward, observation/Max_reach)
            #     #print('loooooop')
            #     loop = loop+1
            #     if loop > 5 and step>64:
            #         RL.learn()
            #         #print('learned')
            #     action,action_value = RL.choose_action_remove_state_check(observation/Max_reach)

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
                #reward = normalRate(observation/Max_reach)
                #RL.store_transition(observation, action, reward, observation)
                RL.store_transition(observation/Max_reach, action, reward, observation/Max_reach)


                # Print the Game over broad
                # Every 100 episode
                # Every time reach 512
                if episode%100 ==0:
                    print(episode)
                    print(observation)

                if (observation > 511).any():
                    print('----------\n',episode,'\n',observation,'\n----------')
                    print(-reward)
                break
            # if Max_reach >= 2**reward_step:
            #     reward = 1
            
            reward = Rate(observation_)
            #reward = normalRate(observation_/Max_reach)            
            #RL.store_transition(observation, action, reward, observation_)
            RL.store_transition(observation/Max_reach, action, reward, observation_/Max_reach)
            if (step > 200) and (step % 5 == 0):
                RL.learn()

            # swap observation
            observation = observation_
            step += 1
        
        if str(Max_reach) in counter:
            counter[str(Max_reach)] += 1
        
        else:
            counter[str(Max_reach)] = 1
    
    
    
    # end of game
    #RL.Save()
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
                      learning_rate=0.00001,
                      reward_decay=0.8,
                      e_greedy=1,
                      replace_target_iter=100,
                      memory_size=1000,
                      # output_graph=True
                      )

    # Load the model, countinue the previous training.
    #RL.Load() 
    
    run()

    # Plot the result.
    RL.plot_acc()