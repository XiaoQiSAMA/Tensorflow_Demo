import tensorflow as tf
import numpy as np 
import matplotlib.pyplot as plt


#y = 2x,加入了噪声
train_X = np.linspace(-1, 1, 100)
train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.3  

#显示模拟数据点
plt.plot(train_X, train_Y, 'ro', label = 'Original data')
plt.legend()
plt.show()