from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)
mean = 10
sd = 2

X = range(20)
Ypdf = [norm(mean, sd).pdf(x) for x in X]
Ycdf = [norm(mean, sd).cdf(x) for x in X]

ax.plot(X, Ypdf)
ax.plot(X, Ycdf)

ax.grid(True)

ax.xaxis.set_ticks(range((20)+1))
ax.yaxis.set_ticks(np.arange(0, 1+0.1, 0.1))

plt.show()