#!/usr/bin/env python
# coding: utf-8

# ## Question 1 : Leader in the Array

# In[1]:


def find_leaders(arr):
    n = len(arr)
    leaders = [arr[n - 1]]
    max_right = arr[n - 1]

    for i in range(n - 2, -1, -1):
        if arr[i] > max_right:
            leaders.append(arr[i])
            max_right = arr[i]

    return leaders[::-1]

# Test Case
arr = [7, 10, 4, 10, 6, 5, 2]
result = find_leaders(arr)
print(result)


# In[ ]:





# ## Question 2 :Best Time to Buy and Sell Stock

# In[2]:


def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

# Test Cases
prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]

result1 = max_profit(prices1)
result2 = max_profit(prices2)

print(result1)  # Output: 5
print(result2)  # Output: 0


# ##  Question 3:Sum of All Subset XOR Totals
# 

# In[3]:


from itertools import combinations

def subset_xor_sum(nums):
    total_xor = 0

    for r in range(len(nums) + 1):
        subsets = combinations(nums, r)
        for subset in subsets:
            xor_result = 0 if not subset else subset[0]
            for num in subset[1:]:
                xor_result ^= num
            total_xor += xor_result

    return total_xor

# Test Cases
nums1 = [1, 3]
nums2 = [5, 1, 6]

result1 = subset_xor_sum(nums1)
result2 = subset_xor_sum(nums2)

print(result1)  # Output: 6
print(result2)  # Output: 28


# In[ ]:





# In[ ]:




