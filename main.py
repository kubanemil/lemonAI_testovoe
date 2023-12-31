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

    def F(self):
        """
        Кусочно-постоянная функция F(x)
        """
        return np.where(self.A[:, 0] < self.c, self.a, self.b)

    def std(self):
        """Среднеквадратическое отклонение функции от точек из A"""
        func_y = self.F()
        mse = np.mean(np.power((self.A[:, 1] - func_y), 2))
        return np.sqrt(mse)

    def find_best_abc(self):
        """
        Находит оптимальные значения для a, b, c
        """

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

    def plot(self, show=True):
        """
        Делает 2 графика:
        1. Распределение массива А на плоскости
        2. Зависимость среднеквадратического отклонение от значения С
        """
        plt.figure(figsize=(8, 8))

        plt.subplot(2, 1, 1)
        plt.title('Distribution of A')
        plt.ylabel("Y-values")
        plt.xlabel("X-values")
        xs, ys, func_ys = self.A[:, 0], self.A[:, 1], self.F()
        plt.scatter(xs, ys, label='Y')
        plt.scatter(xs, func_ys, label='func(x)')
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.title('Relationship between Standard Deviation and the value of C')
        plt.ylabel('STD')
        plt.xlabel(f'Value of C')
        plt.scatter(self.A[:, 0], self.loss, marker='o')

        plt.tight_layout()
        if show: plt.show()


if __name__ == '__main__':
    data = np.asarray([(i, 8) for i in range(-10, 5)] + [(i, -2) for i in range(5, 20)])
    opt = FuncOptimizer(data)
    print(opt.a, opt.b, opt.c)
    opt.plot()