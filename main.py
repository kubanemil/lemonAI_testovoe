import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

class ParameterOptimizer:
    def __init__(self, data):
        self.data = data
        self.a = 1
        self.b = -1
        self.c = 0
        self.loss = []

    def func_y(self):
        return np.where(self.data[:, 0] < self.c, self.a, self.b)

    def std(self):
        func_y = self.func_y()
        mse = np.mean(np.power((self.data[:, 1] - func_y), 2))
        return np.sqrt(mse)

    def find_best_abc(self):
        abc = []
        for x in self.data[:, 0]:
            self.c = x
            a_points = self.data[np.where(self.data[:, 0] < self.c)]
            self.a = np.mean(a_points[:, 1])
            b_points = self.data[np.where(self.data[:, 0] >= self.c)]
            self.b = np.mean(b_points[:, 1])

            self.loss.append(self.std())
            abc.append((self.a, self.b, self.c))
        min_idx = self.loss.index(min(self.loss))
        self.a, self.b, self.c = abc[min_idx]

    def plot(self):
        plt.legend()
        xs = self.data[:, 0]
        ys = self.data[:, 1]
        func_ys = self.func_y()
        plt.scatter(xs, ys)
        plt.scatter(xs, func_ys)
        plt.show()

    def plot_loss(self):
        plt.plot([i for i in range(len(self.loss))], self.loss)
        plt.show()


if __name__=='__main__':
    data = np.random.randint(-10, 10, (10, 2))
    opt = ParameterOptimizer(data)
    opt.find_best_abc()
    print(opt.a, opt.b, opt.c)
    opt.plot()
    opt.plot_loss()