#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program to calculate the sum of all even numbers between 1 and a given positive integer n


# In[2]:


def sum_of_even_numbers(n):
    total_sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total_sum += i
    return total_sum
n = int(input(''))
print(f"The sum of all even numbers between 1 and {n} is: {sum_of_even_numbers(n)}")


# In[ ]:




