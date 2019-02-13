from collections import namedtuple
import random

Transition = namedtuple('Transition', {'state', 'action', 'reward', 'next_state'})

class MemoryRing(object):
  def __init__(self, max_size):
    self.ring_size = max_size
    self.ring = [None for i in range(self.ring_size)]
    self.next_insert = 0;
    self.full = False
    
  def push(self, state, action, reward, next_state):
    self.ring[self.next_insert] = Transition(state=state, action=action, next_state=next_state, reward=reward)
    next_pos = (self.next_insert + 1) % self.ring_size
    if (not self.full and (next_pos < self.next_insert)):
        self.full = True
    self.next_insert = next_pos

  def sample(self, batch_size):
    if (self.full):
        return random.sample(self.ring, batch_size)
    return random.sample(self.ring[:self.next_insert], batch_size)

  def can_sample(self, size):
    if (size > self.ring_size):
        return False
    if (self.full or size < self.next_insert):
        return True
    return False