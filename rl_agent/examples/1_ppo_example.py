import gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2


def our_env_constructor() -> gym.Env:
    return gym.make("MountainCarContinuous-v0")


# The algorithms require a vectorized environment to run
env = DummyVecEnv([our_env_constructor])

agent = PPO2(MlpPolicy, env, verbose=1)

agent.learn(total_timesteps=10000)

obs = env.reset()
for _ in range(1000):
    # internal_state is only used with recurrent policies
    action, internal_state = agent.predict(obs)
    obs, reward, done, info = env.step(action)
    env.render()
