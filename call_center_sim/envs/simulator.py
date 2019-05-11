
from functools import reduce
from gym import spaces
import numpy as np

class CallCenterSimulator:
  def __init__(self, pod_count, pod_load_limit, step_limit):
    self.pod_count = pod_count
    self.pod_load_limit = pod_load_limit
    self.action_space = spaces.Discrete(pod_count)
    self.step_limit = step_limit
    self.reset()

  def reset(self):
    self.pods = [[] for i in range(self.pod_count)]
    self.timestep = 0
    self.next_lead = self.generate_lead()

  def generate_lead(self):
    estimated_lead_quality = round(np.random.randint(1, round(self.pod_load_limit * .10))/self.pod_load_limit * 1000)/1000
    fuzz = np.random.choice([0.8, 0.9, 1, 1.1, 1.2])
    ends = self.timestep + round(estimated_lead_quality * 1000 * fuzz)
    return { "lead_quality": estimated_lead_quality, "ends": ends }

  def get_current_state(self):
    load_levels = [reduce(lambda memo, x: memo + x["lead_quality"] if x["ends"] > self.timestep else memo, pod, 0) for pod in self.pods]
    return load_levels + [ self.next_lead["lead_quality"] ]


  def get_base_reward(self):
    current_state = self.get_current_state()[:-1]
    low = np.min(current_state)
    high = np.max(current_state)
    max_dist = high - low
    return 1/max_dist if max_dist > 0.01 else 100

  def take_action(self, action):
    self.pods[action].append(self.next_lead)
    self.timestep = self.timestep + 1
    self.next_lead = self.generate_lead()

  def get_observation(self):
    reward = self.get_base_reward()
    done = False if self.timestep < self.step_limit else True
    if self.timestep >= self.step_limit:
      reward = 100 + reward
    current_state = self.get_current_state()
    overload = False
    for pod in current_state[:-1]:
      if pod > 1:
        overload = True
      if pod > 1.1:
        done = True
        reward = -100
        break
    if reward > 0 and overload:
      reward = -reward
    return current_state, reward, done, { "pods": self.pods, "current_state": current_state, "next_lead": self.next_lead }