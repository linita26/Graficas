
# coding: utf-8

# In[5]:

import math
import numpy as np
import matplotlib.pyplot as plt

def sigmoidal(x):
    a = []
    for item in x:
        a.append(1/(1+math.exp(-item)))
    return a
x = np.arange(-10., 15,0.2)
sig = sigmoidal(x)
plt.plot(x,sig)

plt.xlabel('Eje X')
plt.title('Funcion de pertenencia Sigmoidal');
plt.ylabel('Grado de pertenencia');


# In[ ]:



