
# coding: utf-8

# In[7]:

import numpy as np
import matplotlib.pyplot as plt

x=[0,20,20,50,50,70]
a=20
b=50

def funh(x,a,b):
    if (x<a):
        y=1
    if (x>=a)&(x<b):
         y=1-(x-a)/(b-a);
    if (x>=b):
        y=0
    return y

funhombro = np.vectorize(funh)
plt.axis([x[0], x[-1], -0.1, 1.5])
plt.plot(x,funhombro(x,a,b))
plt.xlabel('Grado de pertenencia')
plt.title('Funcion de pertenencia hombro izquierdo')


# In[ ]:



