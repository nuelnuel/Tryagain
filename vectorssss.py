v = (1, 2, 3)
c = (3, 2, 1)

print(v + c)

import numpy as np
import pandas as pd

a = np.array([1, 2, 3])

print(a)
print(a.shape)

print(a[1])

temp = pd.read_csv('tas_1991_2016_DOM.csv')
print(temp.shape)

h = np.array([[1,2,3], [4,5,6,], [7,8,9]])
print(h)
print(h[0,2])
print(h[2,2])




zeer = np.zeros((5,9))
print(zeer)