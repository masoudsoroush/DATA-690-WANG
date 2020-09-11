#!/usr/bin/env python
# coding: utf-8

# # Homework 3

# ## Useful Functions for the Main Task

# In[1]:


import random


# In[2]:


# This function generates 10 random integers between 0 and 9 in a list.

def RandFunc():
    a=[];
    for i in range(10):
        a.append(random.randint(0,9))
    return a


# In[3]:


# This function finds the sum of the entries of a list.

def Sum(L):
    a=0;
    for k in range(len(L)):
        a += L[k]
    return a


# ## Tasks of Homework 3

# ### Print a 10x10 Matrix of Random Integers between 0 and 9

# In[4]:


# This block generates and prints the 10x10 matrix.

for l in range(10):
    b=RandFunc();
    for k in range(10):
        print(b[k],end=' ')
        
    print(' ')


# ### Print a 10x10 Matrix of Random Integers with @ in Place of All Odd Entries

# In[5]:


# This block generates and prints the 10x10 matrix of integers with @ in position of all odd entries.

for l in range(10):
    b=RandFunc();
    for k in range(10):
        if b[k]%2==0:
            print(b[k],end=' ')
        else:
            print('@',end=' ')
    print(' ')


# ### Print a 10x10 Matrix of Integers with the Sum of Each Row at the End

# In[6]:


# This block prints a 10x10 matrix of random integers with the sum of each row at the end of the row after *.

for l in range(10):
    b=RandFunc();
    for k in range(10):
        print(b[k],end=' ')
        
    print(' * ',Sum(b))


# ### Print a 10x10 Matrix of Random Integers and Surround by *

# In[7]:


# This block generates a 10x10 matrix of random integers surrounded by *.

print('***********************')
for l in range(10):
    b=RandFunc();
    print('*',end=' ')
    for k in range(10):
        print(b[k],end=' ')
    
    print('* ')
    
print('***********************')


# ### Print a 10x10 Matrix of Random Integers with the Sum of Each Row and Column

# In[8]:


# This block creates a 10x10 matrix of random integers with the sum of each row and column. The basic idea we used 
# here is the notion of the transposed matrix to take care of the sum of the columns.

Mat=[RandFunc() for v in range(10)];
MatTran=[[0 for u in range(10)] for v in range(10)]

for l in range(10):
    for k in range(10):
        MatTran[k][l]=Mat[l][k]
        print(Mat[l][k],end='  ')
        
    print(' * ',Sum(Mat[l]))
    
print('*  *  *  *  *  *  *  *  *  *')

for m in range(10):
    print(Sum(MatTran[m]),end=' ')


# In[ ]:




