import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,80,0.25)
y = [f(t) for t in x]
y_norm = [t/sum(y) for t in y]
y_cumul = [sum(y[t+1:])/sum(y) for t in range(len(y))]