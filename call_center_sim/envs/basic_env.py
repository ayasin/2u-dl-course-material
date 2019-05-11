import gym
from gym import error, spaces, utils
from gym.utils import seeding
from call_center_sim.envs.simulator import CallCenterSimulator



class BasicEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.sim = CallCenterSimulator(5, 500, 2000)
    self.action_space = self.sim.action_space
  
  def step(self, action):
    self.sim.take_action(action)
    return self.sim.get_observation()
  
  def reset(self):
    self.sim.reset()
    return self.sim.get_current_state()
  
  def render(self, mode='human'):
    self.sim.get_current_state()[:-1]
  
  def close(self):
    pass
  