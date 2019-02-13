from imports import *

def check_my_system():
  if (torch.cuda.is_available()):
    print("You have a CUDA capable machine")
    print("Available GPU(s):")
    for i in range(torch.cuda.device_count()):
      name = torch.cuda.get_device_name(i)
      major, minor = torch.cuda.get_device_capability(i)
      print(f"\tcuda:{i} {name} (CUDA version {major}.{minor})")
  else:
    print("You do not have a CUDA capable machine")
  env = gym.make('CartPole-v1').unwrapped
  if (env.action_space.n == 2):
    print("\nYour AI Gym enviornment is correctly set up.")
  else:
    print("\nThere may be a problem with your Gym environment")