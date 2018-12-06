import gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2

# The algorithms require a vectorized environment to run
env = DummyVecEnv([lambda: gym.make("MountainCarContinuous-v0")])

agent = PPO2(MlpPolicy, env, verbose=1)

agent.learn(total_timesteps=10000)

obs = env.reset()
for _ in range(1000):
    # internal_state is only used with recurrent policies
    action, internal_state = agent.predict(obs)
    obs, reward, done, info = env.step(action)
    env.render()
