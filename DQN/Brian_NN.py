import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam
from keras.models import load_model
from Env import State_Check

class DeepQNetwork:
    def __init__(
            self,
            n_actions,
            n_features,
            learning_rate=0.001,
            reward_decay=0.7,
            e_greedy=0.99,
            replace_target_iter=100,
            memory_size=100000,
            batch_size=64,
            e_greedy_increment=0.01,
            output_graph=False
):
        self.n_actions = n_actions
        self.n_features = n_features
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon_max = e_greedy
        self.replace_target_iter = replace_target_iter
        self.memory_size = memory_size
        self.batch_size = batch_size
        self.epsilon_increment = e_greedy_increment
        self.epsilon = 0.3 if e_greedy_increment is not None else self.epsilon_max

        # total learning step
        self.learn_step_counter = 0

        # initialize zero memory [s, a, r, s_]
        self.memory = np.zeros((self.memory_size, n_features * 2 + 2))  #+2 ==> action & reward
        self._build_net()
        self.acc = []


    def _build_net(self):
        self.model = Sequential()
        self.model.add(Dense(input_dim=self.n_features,output_dim=512))
        self.model.add(Activation('relu'))
        self.model.add(Dense(4096))
        self.model.add(Activation('relu'))
        self.model.add(Dense(256))
        self.model.add(Activation('relu'))
        self.model.add(Dense(4))
        self.model.add(Activation('softmax'))
        self.model.summary()
        self.model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
        #self.model.compile(loss='mean_squared_error',optimizer='adam',metrics=['accuracy'])


    def store_transition(self, s, a, r, s_):
        if not hasattr(self, 'memory_counter'):
            self.memory_counter = 0
        s = np.reshape(s,16).tolist()
        s_= np.reshape(s_,16).tolist()
        transition = s+[a]+[r]+s_
        
        # replace the old memory with new memory
        index = self.memory_counter % self.memory_size
        self.memory[index, :] = transition
        self.memory_counter += 1

    def choose_action(self, observation):

        ways = State_Check(observation)
        
        observation = np.reshape(observation,(16))
        observation = observation[np.newaxis, :]
        if np.random.uniform() < self.epsilon:
            # forward feed the observation and get q value for every actions
            actions_value = self.model.predict(observation)
            actions_value = actions_value.tolist()

        
            actions_value = list(actions_value[0])
            for i in range(len(ways)):
                if ways[i] == 0:
                    actions_value[i] = -100


            action = np.argmax(actions_value)
        else:
            actions_value = []
            action = np.random.randint(0, self.n_actions)
        return action, actions_value




    def learn(self):
        if self.memory_counter > self.memory_size:
            sample_index = np.random.choice(self.memory_size, size=self.batch_size)
        else:
            sample_index = np.random.choice(self.memory_counter, size=self.batch_size)
        batch_memory = self.memory[sample_index, :]

        batch_memory_this = batch_memory[:,:16]
        batch_memory_after = batch_memory[:,-16:]

        # check to ,replace target parameters
        if self.learn_step_counter % self.replace_target_iter == 0:
            batch_memory_this = batch_memory[:,:16]
            batch_memory_after = batch_memory[:,-16:]

            this_q = self.model.predict(batch_memory_this)
            next_q = self.model.predict(batch_memory_after)
            reward = batch_memory[:, self.n_features + 1]

            batch_index = np.arange(self.batch_size, dtype=np.int32)
            eval_act_index = batch_memory[:, self.n_features].astype(int)
            this_q[batch_index,eval_act_index] = reward + self.gamma * np.max(next_q, axis = 1)
            his = self.model.fit(batch_memory_this,this_q,nb_epoch=1,batch_size=self.batch_size, verbose = 0)
            self.acc.append(his.history['acc'])


        # increasing epsilon
        self.epsilon = self.epsilon + self.epsilon_increment if self.epsilon < self.epsilon_max else self.epsilon_max
        self.learn_step_counter += 1

    def plot_acc(self):
        import matplotlib.pyplot as plt
        plt.plot(np.arange(len(self.acc)), self.acc)
        plt.ylabel('Acc')
        plt.xlabel('training steps')
        plt.show()

    def Save(self):
        self.model.save('ModelwithNN.h5')

    def Load(self):
        self.model = load_model('ModelwithNN.h5')




        



