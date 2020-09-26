import numpy as np
from numpy.random import beta
from Arm import Arm

def thompson_sampling(arms, T):
    reward = 0
    for i in range(T):
        # 事後分布から乱数を生成。これをpの推定値として扱う
        rand_gened_params = [beta(a=arm.success+1, b=arm.fail+1) for arm in arms]
        # 推定値が一番高いアームを選択
        max_index = np.argmax(rand_gened_params)
        reward += arms[max_index].play()
    return reward
