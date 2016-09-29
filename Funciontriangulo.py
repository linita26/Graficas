
# coding: utf-8

# In[ ]:




# In[5]:

import numpy as np
import matplotlib.pyplot as plt

x=[0,10,10,50,50,90,90,100]
a=10
b=50
c=90
def func(x,a,b,c):
    if ((x<a) | (x>=c)):
        y=0
    if ((a<=x) & (x<b)):
         y=(x-a)/(b-a);
    if ((b<=x) & (x<=c)):
        y=1-(x-b)/(c-b);
    return y

ftriangulo = np.vectorize(func)
plt.plot(x,ftriangulo(x,a,b,c))
plt.xlabel('Eje  X')
plt.title('Funcion de pertenencia triangular');
plt.ylabel('Grado de pertenencia');


# In[ ]:




# In[ ]:



