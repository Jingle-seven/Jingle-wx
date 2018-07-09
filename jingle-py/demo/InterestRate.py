# coding utf-8

sum = 0
payRate6 = 0.0
pay = 0.0
payRate3 = 0.0
# 每月六厘利息,年利率%7.2
yaerRate = 1.072
mouthRate1 = 1.003
mouthRate2 = 1.006
print("月利率三厘")
for i in range(1, 31):
    if i >= 4:
        sum += i
    if i <= 10:
        # pay = (pay * yaerRate) + 8.4
        for j in range(1, 13):
            payRate6 = (payRate6 * mouthRate1) + 0.7
        pay += 8.4
    else:
        for j in range(1, 13):
            payRate6 = (payRate6 * mouthRate1)

    print("第%d年累计收入 %d千元, 包括利息支出 %.3f千元 ,实际支出 %.2f 千元" % (i, sum, payRate6, pay))


def cacuMoney(money, rate=0.0, times=1):
    if times <= 0:
        return money
    return cacuMoney(money * (1 + rate), rate, times - 1)

# 按月计息和按年计息十年期差距大约为2.5%, 平均下来年利率差距大约为0.2%
print(cacuMoney(100.0, 0.006, 12 * 10))
print(cacuMoney(100.0, 0.072, 10))
