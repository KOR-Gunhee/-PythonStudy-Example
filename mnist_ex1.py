#!/usr/bin/env python
# coding: utf-8

# In[25]:


import sys, os
sys.path.append(os.pardir)
from MNIST.mnist import load_mnist

(x_train, t_train), (x_test, t_test) =     load_mnist(flatten=True, normalize=False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)

