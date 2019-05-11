from gym.envs.registration import register

register(id="call-center-sim-v1", entry_point="call_center_sim.envs:BasicEnv")