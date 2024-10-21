#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
import numpy as np
def step_fun(x):
  return np.where(x >= 0, 1, 0)

inp=[[1,0],
    [0,1],
    [1,1],
    [0,0]]
w1=np.matrix([1, 1])
w2=np.matrix([1, 1])
w3=np.matrix([0.5, -0.5])
threshold=1
i=np.matrix(inp)
n1=w1*i.T
n2=w2*i.T
n1=step_fun(n1)
n2=step_fun(n2)
print(n1)
print(n2)

h = []
for a in range(len(n1)):
  h.append(step_fun(n1[a]*w3[0,0] + n2[a]*w3[0,1]))

print(h)


# In[2]:


import numpy as np

def softmax(logits):
    # Subtract the max logit for numerical stability
    exp_logits = np.exp(logits - np.max(logits))
    return exp_logits / np.sum(exp_logits)

import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
data=pd.DataFrame(iris.data)
w=np.matrix([0.5,0.5,0.5]*4).reshape(3,4)
df=np.matrix(data)
h=df*w.T
y1=tan_h(h)
o=[]
for i in y1:
  o.append(softmax(i))
display(o)

