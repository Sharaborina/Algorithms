#!/usr/bin/env python
# coding: utf-8

# In[165]:


def lines (a):
    deleted = 0
    same_color = 1
    first_ball = 0
    i = 0
    reverse = 0
    while i < (len(a)-1) and len(a)>=3:
        if reverse == 0:
            if a[i] != a[i+1]:
                first_ball += 1
                i += 1
                continue

            if a[i] == a[i+1]:
                i += 1
                same_color += 1
                

            if i == len(a)-1 and same_color >= 3:
                a[first_ball:first_ball+same_color] = []
                deleted+=same_color
                reverse = 1
                continue
                
            if i == len(a)-1 and same_color < 3:
                continue
                
            if a[i] != a[i+1] and same_color < 3:
                first_ball = i
                same_color = 1
                continue

            if a[i] != a[i+1] and same_color >= 3:
                a[first_ball:first_ball+same_color] = []
                deleted+=same_color
                first_ball = max(0,first_ball-1)
                i = first_ball
                same_color = 1
                reverse = 1             
            
        else:
            if i>=1 and a[i] == a[i-1]:
                i-=1
                first_ball -= 1
            else:
                reverse = 0
        
    return deleted


# In[ ]:





# In[ ]:





# In[ ]:




