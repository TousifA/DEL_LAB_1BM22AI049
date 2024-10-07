#!/usr/bin/env python
# coding: utf-8

# In[14]:


def accuracy(y,yp):
  a=0
  for i in range(len(y)):
    if y[i]==yp[i]:
      a=a+1
  return (a/4)*100


# In[15]:


def Xor(fn):
  inp=[[1,0],
    [0,1],
    [1,1],
    [0,0]]
  pred=[]
  out=[1,1,0,0]
  print(fn)
  for i in inp:
    w=np.matrix([1,1])
    i=np.matrix(i)
    h=(w*i.T)[0,0]
    z=fn(h)
    pred.append(int(bool(z)))
    print(f"Input={i},output={int(bool(z))}")
  acc=accuracy(out,pred)
  print(f"Accuracy={acc}% ")

Xor(sigmod)
print("")
Xor(relu)
print("")
Xor(stepfunction)
print("")
Xor(tanh)


# In[17]:


def nor(fn):
  inp=[[1,0],
    [0,1],
    [1,1],
    [0,0]]
  pred=[]
  out=[0,0,0,1]
  print(fn)
  for i in inp:
    w=np.matrix([0.5,-0.5])
    i=np.matrix(i)
    h=(w*i.T)[0,0]
    z=fn(h)
    pred.append(int(bool(z)))
    print(f"Input={i},output={int(bool(z))}")
  acc=accuracy(out,pred)
  print(f"Accuracy={acc}% ")

nor(sigmod)
print("")
nor(relu)
print("")
nor(stepfunction)
print("")
nor(tanh)

