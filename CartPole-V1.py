import numpy as np
import gym

class Environment:
    TYPE_CART_POLE='CartPole-v0'

    def __init__(self, env_type, render=False, monitor=False):
        self.env = gym.make(env_type)
        self.must_be_reset = True
        self.render = render
        self.monitor = monitor

        if self.monitor:
            self.env.monitor.start('monitor', force=True)

    def close(self):
        if self.monitor:
            self.env.monitor.close()

    def reset(self):
        self.must_be_reset = False
        return self.env.reset()

    def executeAction(self, action):
        if self.must_be_reset:
            self.reset()

        observation, reward, terminal, info = self.env.step(action)

        if self.render:
            self.env.render()

        if terminal:
            self.must_be_reset = True

        return observation, reward, terminal, info
