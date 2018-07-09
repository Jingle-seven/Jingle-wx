# coding=utf-8


from pylab import *


def showBar():
    n = 15
    X = np.arange(n)
    # Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
    Y1 = (1) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    bar(X, -Y2, facecolor='#ff9999', edgecolor='black')
    for x, y in zip(X, Y1):
        text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
    ylim(-1.25, +1.25)
    show()


def showSin():
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)
    # 画布大小
    # figure(figsize=(15,12), dpi=80)
    # 颜色和折线宽度
    plot(X, C, color="blue", linewidth=4, linestyle="-",label="cosine")
    plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")
    # plot(X,C)
    # plot(X,S)
    # 扩展边缘空白
    # xlim(X.min()*1.5, X.max()*1.5)
    # ylim(C.min()*1.1, C.max()*1.1)
    # 横纵坐标刻度
    xticks([i/2*np.pi for i in range(-2,3)],[ r'%s$\pi$'% (i/2) for i in range(-2,3)])
    yticks([-1, 0, +1])

    # ax = gca()
    # # 去除边框
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # # 设置底边的两个象限
    # ax.xaxis.set_ticks_position('bottom')
    # ax.spines['bottom'].set_position(('data',0))
    # # 设置左边的两个象限
    # ax.yaxis.set_ticks_position('left')
    # ax.spines['left'].set_position(('data',0))

    show()

def showMy():
    X = range(-20,21)
    plot(X,[i*i*i + 8*i*i -100*i for i in X])
    ax = gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    show()
if __name__ == "__main__":
    # showBar()
    # showSin()
    showMy()
