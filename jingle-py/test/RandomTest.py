# coding=utf-8

import random


def testRand():

    # 在[a, b]之间产生随机整数 random.randint(a, b)
    for i in range(5):
        ret = random.randint(100, 999)
        print("random.randint(100, 999) = {0}".format(ret,))

    # 在[a, b]之间产生随机浮点数 random.uniform(a, b)
    for i in range(5):
        ret = random.uniform(1.0, 100.0)
        print("random.uniform(1.0, 100.0) = {0}".format(ret,))

    # 在[0.0, 1.0)之间产生随机浮点数 random.random()
    for i in range(5):
        ret = random.random()
        print("random.random() = {0}".format(ret,))

    # 在样本population中随机选择k个 random.sample(population, k)
    population = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" }
    for i in range(5):
        ret = random.sample(population, 3)
        print("random.sample(population, 3) = {0}".format(ret,))

    # 在序列seq中随机选择1个 random.choice(seq)
    seq = ("to", "be", "or", "not", 'tobe', 'is', 'a', 'question')
    for i in range(5):
        ret = random.choice(seq)
        print("random.choice(seq) = {0}".format(ret,))

    # 从序列中随机获取指定长度的片断。不修改原有序列。
    # random.sample(sequence, k)
    sentence = "to be or not to be is a question"
    for i in range(5):
        ret = random.sample(sentence, 5)
        print("random.sample(sentence, 5) = {0}".format(ret,))

    # 三角分布的随机数 random.triangular(low, high, mode)
    for i in range(5):
        ret = random.triangular(0, 100, 10)
        print(" random.triangular(0, 100, 10) = {0}".format(ret,))

    print("=================================")
    # 高斯分布的随机数（稍快） random.gauss(mu, sigma)
    for i in range(20):
        # ret = random.gauss(0, 1)
        # print(" random.gauss(0, 1) = {0}".format(ret,))

        # beta β分布的随机数 random.betavariate(alpha, beta)

        # 指数分布的随机数 random.expovariate(lambd)

        # 伽马分布的随机数 random.gammavariate(alpha, beta)

        print(int(10*random.gammavariate(8, 0.5)))

        # 对数正态分布的随机数 random.lognormvariate(mu, sigma)

        # 正态分布的随机数 random.normalvariate(mu, sigma)

        # 冯米塞斯分布的随机数 random.vonmisesvariate(mu, kappa)

        # 帕累托分布的随机数 random.paretovariate(alpha)

        # 韦伯分布的随机数 random.weibullvariate(alpha, beta)


if __name__ == "__main__" :
    testRand()