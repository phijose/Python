import gym
import numpy as np
import random

# pelman's equation
env = gym.make("CartPole-v0")
learning_rate = 0.1
discount_factor = 0.99
exploration_rate = 1
max_exploration_rate = 1
min_exploration_rate =  0.01
exploration_decay_rate = 0.001

num_epochs = 10000
max_steps = 200
done = False
s = env.reset()
discrete_size = [20]*len(env.observation_space.high)
win_size = (env.observation_space.high-env.observation_space.low)/discrete_size
q_table=np.random.uniform(low=-1,high=0,size=(discrete_size+[env.action_space.n]))
print(discrete_size,win_size)
print(discrete_size+[env.action_space.n])
print(q_table.shape)
print([10,10]+[2])
def discretize(state):
    s=(state-env.observation_space.low)/win_size
    return tuple(s.astype(np.int0))
s=discretize(s)
print(discretize(s))
print(q_table[s+(0,)])

print("Before training\n\n")
for epoch in range(num_epochs):
    state = env.reset()
    state=discretize(state)
    done = False
    print(epoch)
    for step in range(max_steps):
        exploration_threshold = random.uniform(0,1)
        if exploration_threshold > exploration_rate:
            action = np.argmax(q_table[state])
        else:
            action = random.randint(0,env.action_space.n-1)
        next_state, reward, done ,info = env.step(action)
        next_state=discretize(next_state)
        q_table[state][action] = (1-learning_rate)*q_table[state][action] + learning_rate*(reward + discount_factor*np.max(q_table[next_state]))
        # env.render()
        state = next_state
        if done == True:
            break
    exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate)*np.exp(-exploration_decay_rate*epoch)
print("After training\n\n")
print(q_table)
for epoch in range(100):
    state = env.reset()
    state=discretize(state)
    done = False
    for steps in range(max_steps):
        action = np.argmax(q_table[state])
        new_state, reward, done, info = env.step(action)
        new_state=discretize(new_state)
        env.render()
        state = new_state
        if done == True:
            break