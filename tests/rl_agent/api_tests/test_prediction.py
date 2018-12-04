import numpy as np
from stable_baselines import PPO2
from .test_save_and_load import ppo_agent


def test_agent_predict_can_operate_in_batches(ppo_agent: PPO2):
    batch_size = 10
    obs_batch = np.array([ppo_agent.observation_space.sample()
                          for _ in range(batch_size)])
    actions_batch, internal_state = ppo_agent.predict(obs_batch)

    assert internal_state is None  # Only used for recurrent policies
    assert actions_batch.shape[0] == batch_size
    for action in actions_batch:
        assert isinstance(action, np.ndarray)


def test_agent_can_operate_with_a_single_observation(ppo_agent: PPO2):
    env = ppo_agent.get_env()
    obs = env.reset()
    assert isinstance(obs, np.ndarray)

    action, _ = ppo_agent.predict(obs)
    assert isinstance(action, np.ndarray)
