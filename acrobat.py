# testing

import gym
env = gym.make('Acrobot-v0')
env.monitor.start('/tmp/Acrobot-v12')
for i_episode in range(13000):
    observation = env.reset()
    for t in range(1,1300,1) or range(1,1300,2) or range(1,1300,3) or range(1,1300,-1) or range(1,1300,-2) or range(1,1300,-3):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

env.monitor.close()

import gym
gym.upload('/tmp/Acrobot-v12', api_key='sk_3tDPxTVoRvmGd4nMwNtWlA')
