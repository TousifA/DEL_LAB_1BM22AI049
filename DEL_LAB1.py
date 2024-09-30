#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Demonstrate the following activation function
import matplotlib.pyplot as plt
import numpy as np
def sigmod(x):
  return 1/(1+np.exp(-x))
def stepfunction(x):
  if x>=0:
    return 1
  else:
    return 0
def relu(x):
  return max(0,x)
def tanh(x):
  return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

x1=int(input("Enter the value of x1:"))
x2=int(input("Enter the value of x2:"))

w1=1
w2=2

h1=x1*w1+x2*w2

y1=sigmod(h1)
print("Sigmoid activation pred=",y1)

y2=stepfunction(h1)
print("linear activation predection=",y2)

y3=relu(h1)
print("Relu activation pred=",y3)

y4=tanh(h1)
print("Tanh activation pred=",y4)

x_values = np.linspace(-10, 10, 100)
sig_values = sigmod(x_values)
step_values = np.array([stepfunction(x) for x in x_values])
relu_values = np.array([relu(x) for x in x_values])
tanh_values = np.array([tanh(x) for x in x_values])

plt.subplot(2,3,1)
plt.plot(x_values, sig_values, label='Sigmoid Function', color='blue')
plt.title('Sigmoid Activation Function')
plt.xlabel('Input')
plt.ylabel('Output')

plt.subplot(2,3,2)
plt.plot(x_values, relu_values, label='Relu Function', color='blue')
plt.title('Relu Activation Function')
plt.xlabel('Input')
plt.ylabel('Output')

plt.subplot(2,3,3)
plt.plot(x_values, tanh_values, label='Tanh Function', color='blue')
plt.title('Tanh Activation Function')
plt.xlabel('Input')
plt.ylabel('Output')

plt.subplot(2,3,4)
plt.plot(x_values, step_values, label='Step Function', color='blue')
plt.title('Step Activation Function')
plt.xlabel('Input')
plt.ylabel('Output')


plt.show()


# In[ ]:




