# 2048_AI
Build an AI to win 2048 game

# Build a simple environment.
The most important thing about 2048 is to reach the highest score by moving tiles and merging the same tile.	  
We have to define how to move tiles in a game and how to generate new tile after every move.		    
The codes is in the `Env.py`

# Search method 
My first attempt is to use search method to win the game.  I tried to go through all the possible moves in the given search depth, and then compared the scores in the result to choose the best decision in the specific situation.    
The codes is in the `2048_Search.py`

In this method, I set the depth from 2 to 5 and ran 100 times in each depth.  
Here is some result.

In Depth:2,

| Max Reach | Count | Accumulate %  | Reverse Accumulate % |
|-------|---------|----------|----------|
| 256   |  4  |   4% |  100% |
| 512   |  19 |  23% |  96%|
| 1024  |  47 |  70% |  77%|
| 2048  |  29 |  99% |  30%|
| 4096  |  1  | 100% |  1%|
| 8192  |  0  | 100% |  0%|

In Depth:3,

| Max Reach | Count | Accumulate %  |  Reverse Accumulate % |
|-------|---------|----------|----------|
| 256   |  1  |   1% | 100%|
| 512   |  9 |  10% |  99%|
| 1024  |  36 |  46% | 90%|
| 2048  |  48 |  94% | 54%|
| 4096  |  6  | 100% | 6%|
| 8192  |  0  | 100% | 0%|

In Depth:4,

| Max Reach | Count | Accumulate %  |  Reverse Accumulate % |
|-------|---------|----------|----------|
| 256   |  0  |   0% | 100%|
| 512   |  3|  3% |   100%|
| 1024  |  19 |  22% | 97%|
| 2048  |  58 |  80% | 78%|
| 4096  |  20  | 100% | 20%|
| 8192  |  0  | 100% |  0%|

In Depth:5,

| Max Reach | Count | Accumulate %  |  Reverse Accumulate % |
|-------|---------|----------|----------|
| 256   |  0  |   0% | 100%|
| 512   |  2 |  2% |  100%|
| 1024  |  20 |  22% | 98%|
| 2048  |  48 |  70% | 78%|
| 4096  |  29  | 99% | 30%|
| 8192  |  1  | 100% | 1%|



# Deep Q Network method (DQN)
After I implemented the search method, I studied some Reinforcement Learning (RL) method. In order to understand more comprehensively about RL, I implement DQN which is one main branch of RL in 2048 game.	    
DQN is using Q-value as reward to evaluate the decision that machine make.	    
The codes is in DQN folder.

# Deep Sarsa Network method (Sarsa)
Sarsa is also a kind of RL.  Sarsa is slightly different from DQN.    
In short, the difference is that Sarsa policy chooses the safest way to avoid the failure (Game over) in the game.     
On the other hand, DQN policy always chooses the way to reach the highest scores and sometimes get failure in the early game.	    
The codes is in Sarsa folder.   
