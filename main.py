import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')
np.random.seed(10)
class FuncOptimizer:
    def __init__(self, A):
        self.A = A
        self.a = 1
        self.b = -1
        self.c = 0
        self.loss = []
        self.find_best_abc()

    def func_y(self):
        return np.where(self.A[:, 0] < self.c, self.a, self.b)

    def std(self):
        func_y = self.func_y()
        mse = np.mean(np.power((self.A[:, 1] - func_y), 2))
        return np.sqrt(mse)

    def find_best_abc(self):
        abc = []
        for x in self.A[:, 0]:
            self.c = x
            a_points = self.A[np.where(self.A[:, 0] < self.c)]
            self.a = np.mean(a_points[:, 1])
            b_points = self.A[np.where(self.A[:, 0] >= self.c)]
            self.b = np.mean(b_points[:, 1])

            self.loss.append(self.std())
            abc.append((self.a, self.b, self.c))
        min_idx = self.loss.index(min(self.loss))
        self.a, self.b, self.c = abc[min_idx]

    def plot(self):
        plt.figure(figsize=(8, 8))

        plt.subplot(2, 1, 1)
        plt.title('Distribution of A')
        plt.ylabel("Y-values")
        plt.xlabel("X-values")
        xs, ys, func_ys = self.A[:, 0], self.A[:, 1], self.func_y()
        plt.scatter(xs, ys, label='Y')
        plt.scatter(xs, func_ys, label='func(x)')
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.title('Relationship between Standard Deviation and the value of C')
        plt.ylabel('STD')
        plt.xlabel(f'Value of C')
        plt.scatter(self.A[:, 0], self.loss, marker='o')

        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    data = np.asarray([(i, 8) for i in range(-10, 5)] + [(i, -2) for i in range(5, 20)])
    opt = FuncOptimizer(data)
    print(opt.a, opt.b, opt.c)
    print(np.sort(opt.A[:, 0]), opt.loss)
    opt.plot()