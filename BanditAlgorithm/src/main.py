from numpy.random import binomial,randint

# p: 成功確率
class Arm:
    def __init__(self, p):
        self._p = p
        self.success = 0
        self.fail = 0

    def play(self):
        result = binomial(n=1, p=self._p)
        if result == 1:
            self.success += 1
        else:
            self.fail += 1
        return result

def calc_success_ratio(arm):
    if arm.success + arm.fail == 0:
        return 0
    return arm.success / (arm.success + arm.fail)

def epsilon_greedy(arms, T, epsilon):
    reward = 0
    for i in range(T):
        if binomial(n=1, p=epsilon) == 1:
            # 探索ステップ : アームを一様ランダムに選ぶ
            index = randint(0, 99)
        else:
            # 活用ステップ : 今までで一番成功確率の高いアームを選ぶ
            avgs = [ calc_success_ratio(arm) for arm in arms]
            index = avgs.index(max(avgs))
        reward += arms[index].play()
    return reward

if __name__ == '__main__':
    pass
