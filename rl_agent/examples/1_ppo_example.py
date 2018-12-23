import gym
import time
import gym_roboy
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO1


def our_env_constructor() -> gym.Env:
    return gym.make("msj-control-v0")

def main():

	# The algorithms require a vectorized environment to run
	env = DummyVecEnv([our_env_constructor])

	agent = PPO1(MlpPolicy, env, verbose=1)

	agent.learn(total_timesteps=10000)

	obs = env.reset()
	for _ in range(100):
	    # internal_state is only used with recurrent policies
	    obs = env.reset()
	    done = False
	    while not done:
		    action, _ = agent.predict(obs)
		    obs, reward, done, info = env.step(action)
		    print("step reward:", reward)
		    time.sleep(0.01)
	    print('reached goal')
if __name__ == '__main__':
	main()
