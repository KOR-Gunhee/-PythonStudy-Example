#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()

