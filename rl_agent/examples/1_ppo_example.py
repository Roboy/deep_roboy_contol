import gym
import gym_roboy

import time



from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO1

#for plot
import os
from stable_baselines.bench import Monitor
from stable_baselines.results_plotter import load_results, ts2xy
import numpy as np
import matplotlib.pyplot as plt

best_mean_reward, n_steps = -np.inf, 0

def our_env_constructor() -> gym.Env:
    return gym.make("msj-control-v0")


def callback(_locals, _globals):
  """
  Callback called at each step (for DQN an others) or after n steps (see ACER or PPO2)
  :param _locals: (dict)
  :param _globals: (dict)
  """
  global n_steps, best_mean_reward
  # Print stats every 1000 calls
  if (n_steps + 1) % 10 == 0:
      # Evaluate policy performance
      x, y = ts2xy(load_results(log_dir), 'timesteps')
      if len(x) > 0:
          mean_reward = np.mean(y[-100:])
          print(x[-1], 'timesteps')
          print("Best mean reward: {:.2f} - Last mean reward per episode: {:.2f}".format(best_mean_reward, mean_reward))

          # New best model, you could save the agent here
          if mean_reward > best_mean_reward:
              best_mean_reward = mean_reward
              # Example for saving best model
              print("Saving new best model")
              _locals['self'].save(log_dir + 'best_model.pkl')
  n_steps += 1
  return True


# Create log dir
log_dir = "/tmp/gym/"
os.makedirs(log_dir, exist_ok=True)



env = gym.make('msj-control-v0')
#for plotting
env = Monitor(env, log_dir, allow_early_resets= True)
# The algorithms require a vectorized environment to run
#env = DummyVecEnv([our_env_constructor])
env = DummyVecEnv([lambda:env])

agent = PPO1(MlpPolicy, env, verbose=1)

agent.learn(total_timesteps=10, callback= callback)

obs = env.reset()
for _ in range(100):
    # internal_state is only used with recurrent policies
    obs = env.reset()
    done = False
    i = 0
    while not done and i < 10:
	    self.node.get_logger().info("number of it: %i" % i)
        
	    action, _ = agent.predict(obs)
	    obs, reward, done, info = env.step(action)
	    print("step reward:", reward)
	    self.node.get_logger().info("reward: %f" % reward)
	    time.sleep(0.01)
	    i += 1
    print('reached goal')

