# testing

import gym
env = gym.make('MountainCar-v0')
env.monitor.start('/tmp/MountainCar-v2')
for i_episode in range(1313):
    observation = env.reset()
    for t in range(-5,-15,1):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

env.monitor.close()

import gym
gym.upload('/tmp/MountainCar-v2', api_key='sk_3tDPxTVoRvmGd4nMwNtWlA')
