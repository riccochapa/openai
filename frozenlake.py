import gym

env = gym.make('FrozenLake-v0')
env.monitor.start('/tmp/FrozenLake-v33')
for i_episode in range(10000):
    observation = env.reset()
    for t in range(1000000001):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print(reward + "Episode finished after {} timesteps".format(t+1))
            break

env.monitor.close()

import gym
gym.upload('/tmp/FrozenLake-v33', api_key='sk_3tDPxTVoRvmGd4nMwNtWlA')
