import torch
import matplotlib.pyplot as plt
from IPython.display import clear_output
from IPython.display import display

class RewardTracker:
  def __init__(self):
    self.episode_rewards = []

  def plot_total_rewards(self):
    plt.figure(2)
    plt.clf()
    rewards_t = torch.tensor(self.episode_rewards, dtype=torch.float)
    plt.title('Training...')
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.plot(rewards_t.numpy())
    if len(rewards_t) > 50:
      means = rewards_t.unfold(0, 50, 1).mean(1).view(-1)
      means = torch.cat((torch.zeros(49), means))
      plt.plot(means.numpy())
      clear_output(wait=True)
      display(plt.gcf())

  def push(self, value):
    self.episode_rewards.append(value)

  def reset(self):
    self.episode_rewards = []