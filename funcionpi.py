
# coding: utf-8

# In[14]:

import numpy as np
import matplotlib.pyplot as plt

x=[0,10,10,50,150,190,190,200]
a=10
b=50
c=150
d=180

def funcionp(x,a,b,c,d):
    if ((x<a) | (x>=c)):
        y=0
    if (x>=a)&(x<b):
         y=(x-a)/(b-a)
    if (x>=b)&(x<d):
        y=1
    if (x>=d)&(x<c):
        y=1-(x-d)/(c-d)
    return y

funpi = np.vectorize(funcionp)
plt.axis([x[0], x[-1], -0.1, 1.5])
plt.plot(x,funpi(x,a,b,c,d))
plt.xlabel('Eje de X')
plt.title('Funcion de pertenencia forma pi')
plt.ylabel('Grado de pertenencia')


# In[ ]:



