from ThompsonSampling import thompson_sampling
from EpsilonGreedy import epsilon_greedy
from UCB import ucb
from Arm import Arm
import numpy as np


def __out_benchmark(array):
    print('\t Avg: {}, Std: {}, Max: {}, Min: {}'.format(np.average(array), np.std(array), np.max(array), np.min(array)))


if __name__ == "__main__":
    loop_cnt = 100
    T = 1_000
    arms = [Arm(0.3) for _ in range(5)] + [Arm(0.1) for _ in range(4)] + [Arm(0.5)]

    eg_3_reward_hist = []
    eg_5_reward_hist = []
    eg_7_reward_hist = []
    ucb_reward_hist = []
    ts_reward_hist = []

    for i in range(loop_cnt):
        eg_3_reward_hist.append(epsilon_greedy(arms=arms,T=T,epsilon=0.3))
        eg_5_reward_hist.append(epsilon_greedy(arms=arms,T=T,epsilon=0.5))
        eg_7_reward_hist.append(epsilon_greedy(arms=arms,T=T,epsilon=0.5))
        ucb_reward_hist.append(ucb(arms=arms,T=T))
        ts_reward_hist.append(thompson_sampling(arms=arms,T=T))

    print('Epsilon-greedy_0.3')
    __out_benchmark(eg_3_reward_hist)
    print('Epsilon-greedy_0.5')
    __out_benchmark(eg_5_reward_hist)
    print('Epsilon-greedy_0.7')
    __out_benchmark(eg_7_reward_hist)
    print('UCB')
    __out_benchmark(ucb_reward_hist)
    print('Thompson sampling')
    __out_benchmark(ts_reward_hist)
