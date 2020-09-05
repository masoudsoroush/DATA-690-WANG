#!/usr/bin/env python
# coding: utf-8

# # DATA-690-Homework 02

# ## Necessary Functions Defined for Homework 02

# In[1]:


# This function calculates the maximum of a list of real numbers.

def Max(L):
    if len(L)==0:
        a='The list is empty!'
    else:
        a=L[0];
        for k in range(len(L)):
            if L[k]>a:
                a=L[k]
    return a


# In[2]:


# This function calculates the minimum of a list of real numbers.

def Min(L):
    if len(L)==0:
        a='The list is empty!'
    else:
        a=L[0];
        for k in range(len(L)):
            if L[k]<a:
                a=L[k]          
    return a


# In[3]:


# This function calculates the range of a list of real numbers.

def Range(L):
    if len(L)==0:
        a='The list is empty!'
    else:
        a=Max(L)-Min(L)
    return a


# In[4]:


# This function calculates the average of a list of real numbers.

def Average(L):
    if len(L)==0:
        a='The list is empty!'
    else:
        a=0
        for k in range(len(L)):
            a += L[k]
        a /=len(L)
    return a


# In[5]:


# This function calculates the variance of a list of real numbers. The variable Type specifies 
# whether the data belongs to a population or a sample. 

def Variance(L,Type):
    if len(L)==0:
        a='The list is empty!'
    else:
        a=0
        for k in range(len(L)):
            a += (L[k]-Average(L))**2
        if Type=='P':
            a /= len(L)
        else:
            a /= len(L)-1
    return a


# In[6]:


# This function calculates the standard deviation of a list of real numbers. The variable Type specifies 
# whether the data belongs to a population or a sample. 

def StanDev(L,Type):
    if len(L)==0:
        a='The list is empty!'
    else:
        a=Variance(L,Type)**(1/2)
    return a


# In[7]:


# This function checks whether a string L is merely composed of digits.

def IntCheck(L):
    S={'0','1','2','3','4','5','6','7','8','9'}
    if L=='':
        a=False
    else:
        for m in range(len(L)):
            if L[m] not in S:
                a=False
                break 
            else:
                a=True
    return a


# In[8]:


# This function checks whether string L is merely composed of digits and the minus sign.

def IntCheckPM(L):
    S={'-','0','1','2','3','4','5','6','7','8','9'}
    if L=='':
        a=False
    else:
        for m in range(len(L)):
            if L[m] not in S:
                a=False
                break 
            else:
                a=True
    return a


# # Constructing the Data Set

# In[9]:


import time


# In[10]:


# The code first asks whether the data belongs to a population or to a sample. 

Type=input('Sample or Population? Please enter either S or P: ')
while Type not in {'S','P'}:
    print('Please enter either S for sample or P for population!')
    Type=input('Sample or Population? Please enter either S or P: ')

# The code asks the total number of integer in the data set.

xstr=input('What is the total number of integers in your data set?')
while IntCheck(xstr)==False:
    print('Please enter a positive integer!')
    xstr=input('What is the total number of integers in your data set? ')    

# The code asks the user to enter the integers one by one.
    
NN=int(xstr); Y=[];
for n in range(1,NN+1):
    Gstr=input('What is the number {} integer of your data set? '.format(n))
    while IntCheckPM(Gstr)==False:
        print('please enter an integer!')
        Gstr=input('What is the number {} integer in your data set? '.format(n))
    Y.append(int(Gstr))
    
# The code constructs a list of integers (i.e. Y). Using the functions defined earlier, the code 
# calculates and spits out the minimum, maximum, range, mean, variance, and the standard deviation of the data set.
    
print('Your list of integers are',Y)
time.sleep(1)
print('Minimum of your data set is: ',Min(Y))
time.sleep(1)
print('Maximum of your data set is: ',Max(Y))
time.sleep(1)
print('Range of your data set is: ',Range(Y))
time.sleep(1)
print('Mean of your data set is: ',Average(Y))
time.sleep(1)
print('Variance of your data set is: ',Variance(Y,Type))
time.sleep(1)
print('Standard deviation of your data set is: ',StanDev(Y,Type))

