from gym.envs.registration import register

register(
    id='baccarat-v0',
    entry_point='gym_baccarat.envs:BaccaratEnv',
    timestep_limit=1000,
)
