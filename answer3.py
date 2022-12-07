#!/usr/bin/env python
# coding: utf-8

# In[2]:


num = int(input("enter your numbers :"))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print(str(reversed_num))


# In[ ]:




