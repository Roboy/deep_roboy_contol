import os

import gym
import numpy as np
import pytest
from stable_baselines import PPO2
from stable_baselines.common import set_global_seeds
from stable_baselines.common.vec_env import DummyVecEnv


@pytest.fixture
def ppo_agent():
    return new_ppo_agent()


def new_ppo_agent():
    env = DummyVecEnv([lambda: gym.make("MountainCarContinuous-v0")])
    return PPO2("MlpPolicy", env)


def test_two_newly_created_agents_are_equal():
    set_global_seeds(0)
    agent1 = new_ppo_agent()
    set_global_seeds(0)
    agent2 = new_ppo_agent()

    assert agents_behave_equally(agent1, agent2)


def agents_behave_equally(agent1: PPO2, agent2: PPO2) -> bool:
    obs = agent1.get_env().observation_space.sample()
    assert isinstance(obs, np.ndarray)

    set_global_seeds(0)
    action1, _ = agent1.predict(obs, deterministic=True)
    set_global_seeds(0)
    action2, _ = agent2.predict(obs, deterministic=True)

    print(action1, action2)

    return np.allclose(action1, action2)


def test_agent_is_saved_as_a_pickle_file(ppo_agent: PPO2):
    pickle_fname = "delme_pickle_file"
    expected_pickle_fname = pickle_fname + ".pkl"
    try:
        assert not os.path.exists(expected_pickle_fname)
        ppo_agent.save(pickle_fname)
        assert os.path.exists(expected_pickle_fname)
    finally:
        os.remove(expected_pickle_fname)


def test_loaded_agent_is_equal():
    pickle_fname = "delme_pickle_file"
    full_pickle_fname = pickle_fname + ".pkl"
    try:
        assert not os.path.exists(full_pickle_fname)
        agent = new_ppo_agent()
        agent.save(pickle_fname)
        loaded_agent = PPO2.load(pickle_fname)
        assert agents_behave_equally(agent, loaded_agent)
    finally:
        os.remove(full_pickle_fname)
