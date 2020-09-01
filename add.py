def add(v, w):
    assert len(v) == len(w), "Vector same lenght"
    return [v_i + w_i for v_i, w_i in zip (v,w)]
jjj = add([3,3,2],[3,3,2])
print((jjj))


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cl = pd.read_csv('tas_1991_2016_DOM.csv')
#print(cl)

cl2 = np.array(cl)

temprd = cl2[:,0]
years = cl2[:, 1]

#plt.plot(years, temprd)
#plt.show()
# print(cl2[:,0])



print(max(temprd))
print(min(temprd))


print((temprd))