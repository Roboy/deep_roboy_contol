import gym

from stable_baselines.common.vec_env import SubprocVecEnv
from stable_baselines.common import set_global_seeds
from stable_baselines import PPO2


def setup_constructor(rank, seed=0):

    def our_env_constructor() -> gym.Env:
        environment = gym.make("MountainCarContinuous-v0")
        environment.seed(seed + rank)
        return environment

    set_global_seeds(seed)
    return our_env_constructor


num_cpu = 2
env = SubprocVecEnv([setup_constructor(i) for i in range(num_cpu)])

model = PPO2("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=25000)

obs_batch = env.reset()
for i in range(1000):
    actions_batch, _ = model.predict(obs_batch)
    obs_batch, rewards_batch, _, _ = env.step(actions_batch)
    env.render()

    # Notice how the environment and the agent operate both in batches
    assert obs_batch.shape[0] == num_cpu
    assert actions_batch.shape[0] == num_cpu
    assert rewards_batch.shape[0] == num_cpu
