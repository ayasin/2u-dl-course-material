from imports import *

def display_frames_as_gif(frames):
    patch = plt.imshow(frames[0])
    plt.axis('off')
    def animate(i):
        patch.set_data(frames[i])
    anim = animation.FuncAnimation(plt.gcf(), animate, frames = len(frames), interval=50)
    display(display_animation(anim, default_mode='once'))

def make_movie(device, env_name, agent):
    env = gym.make(env_name)
    fig = plt.figure()
    state = env.reset()
    state = torch.tensor(state, dtype=torch.float).unsqueeze(0).to(device)
    frames = []
    done = False
    total_reward = 0
    while not done:
        frames.append(env.render(mode='rgb_array'))
        action = agent.choose_next_action(state, explore=False)
        state, reward, done, _ = env.step(action.item())
        state = torch.tensor(state, dtype=torch.float).unsqueeze(0).to(device)
        total_reward += reward
    display_frames_as_gif(frames)
    print(f"Total reward: {total_reward}")
    env.close()