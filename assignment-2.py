#!/usr/bin/env python
# coding: utf-8

# In[2]:


# second assignment
#*
#**
#***
#****
#*****
#****
#***
#**
#*
# create the above pattern using nested for loop
    


# In[13]:


for i in range(1,6):
    for j in range(i):
        print('*',end='')
    print(end = '\n')

for i in range(4,0,-1):
    for j in range(i):
        print('*',end='')
    print(end='\n')


# In[14]:


# second question
# write a python program to reverse a word after accepting the input from the user


# In[15]:


word = input('enter the word: ')
print(word[::-1])


# In[ ]:




