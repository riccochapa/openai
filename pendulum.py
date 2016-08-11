# testing

import gym
env = gym.make('Pendulum-v0')
env.monitor.start('/tmp/Pendulum-v19')
for i_episode in range(13130):
    observation = env.reset()
    for t in range(1, 13, 1) and range(13000,33000,5):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

env.monitor.close()

import gym
gym.upload('/tmp/Pendulum-v19', api_key='sk_3tDPxTVoRvmGd4nMwNtWlA')
