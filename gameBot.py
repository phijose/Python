import gym
import numpy as np
import random

# pelman's equation
env = gym.make("FrozenLake-v1",map_name="8x8",is_slippery=False)
learning_rate = 0.1
discount_factor = 0.99
exploration_rate = 1
min_exploration_rate =  0.01
max_exploration_rate = 1
exploration_decay_rate = 0.0001
q_table = np.zeros((env.observation_space.n,env.action_space.n))
num_epochs = 50000
max_steps = 1000
done = False
print("Before training\n\n")
for epoch in range(num_epochs):
    state = env.reset()
    done = False
    for step in range(max_steps):
        exploration_threshold = random.uniform(0,1)
        if exploration_threshold > exploration_rate:
            action = np.argmax(q_table[state,:])
        else:
            action = random.randint(0,3)
        next_state, reward, done ,info = env.step(action)
        q_table[state][action] = (1-learning_rate)*q_table[state][action] + learning_rate*(reward + discount_factor*np.max(q_table[next_state,:]))
        state = next_state
        if done == True:
            break
    exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate)*np.exp(-exploration_decay_rate*epoch)
print("After training\n\n")
print(q_table)
for epoch in range(10):
    state = env.reset()
    done = False
    for steps in range(max_steps):
        action = np.argmax(q_table[state,:])
        new_state, reward, done, info = env.step(action)
        env.render()
        state = new_state
        if done == True:
            break