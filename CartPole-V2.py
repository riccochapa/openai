# testing

import gym
env = gym.make('CartPole-v0')
env.monitor.start('/tmp/cartpole-experiment-60')

for i_episode in range(13000):
    observation = env.reset()
    for t in range(1,100,1) and range(100,300,1) and range(300,600,1) or range(1,100,-1) and range(100,300,-1) and range(300,600,-1):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            print reward
            print info
            break

env.monitor.close()

import gym
gym.upload('/tmp/cartpole-experiment-60', api_key='sk_3tDPxTVoRvmGd4nMwNtWlA')
