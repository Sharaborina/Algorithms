#!/usr/bin/env python
# coding: utf-8

# # Scraping Yahoo Finance

# In this assignment you are required to look at historical data for 30 companies from [Dow Jones Index](https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average). Tickers for companies from the index can be found in *dow_jones_tickers.txt*. For each company you should get historical daily stock prices for 2019 from https://finance.yahoo.com/, and then use the data to answer the questions you will find below. 

# In[106]:


dow_jones_companies = []

with open('dow_jones_tickers.txt') as f:
    for ticker in f:
        dow_jones_companies.append(ticker.strip())
N = len(dow_jones_companies)  


# In[168]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
data = {}
for ticker in dow_jones_companies:
    url = 'https://query1.finance.yahoo.com/v7/finance/download/' + ticker + '?period1=1546300800&period2=1577750400&interval=1d&events=history&includeAdjustedClose=true'
    tab = pd.read_csv(url)
    tab['Date']= pd.to_datetime(tab['Date'])
    data[ticker] = {'table':tab}
    print(ticker)
    display(data[ticker]['table'].head(-1))


# In[109]:


data['DOW']['table'].info()


# <br><br>
# 
# ### Questions
# 
# <br><br>
# 
# **Question 1.** What is the average change of price over the year (in %)?
# 
# *Note 1*. The opening price is the price at which a stock first trades upon the opening of an exchange on a trading day.
# 
# *Note 2*. The closing price for any stock is the final price at which it trades during regular market hours on any given day.
# 
# *Note 3*. Here by the price change we going to mean a ratio of a closing price in the last day of the period to an opening price in the first day of that period, subtracted one and multiplied by 100.
# 
# Example: if a price of a stock in day 1 opened at \\$100, and its close price in the last day was \\$120, then the price change during the period is: $$\left(\dfrac{120}{100}-1\right) * 100 = (1.2 - 1) * 100=20.$$
# 
# The price grew by 20%.

# In[166]:


avg = 0
avg0 = 0
for ticker in dow_jones_companies:
    df = data[ticker]['table']
    df['Change'] = df.apply(lambda row: 100*(row.Close/row.Open - 1), axis=1) # Create new column with 100*(Close/Open - 1)
    data[ticker]['VolumeProgress'] = df.Change.sum()
    avg0 += data[ticker]['VolumeProgress']

    mindate = min(df.Date) # Min date
    maxdate = max(df.Date) # Max date
    opn = df[df.Date == mindate].Open.values[0]
    cls = df[df.Date == maxdate].Close.values[0]
    data[ticker]['Open' ] = opn
    data[ticker]['Close'] = cls
#     display(df[df.Date == mindate])
#     display(df[df.Date == maxdate])
    data[ticker]['Progress'] = (cls/opn - 1)*100

    print('Ticker:',ticker,'Date:', mindate,'Open:',opn,'Date:', maxdate,', Close:',cls, 'Progress:', data[ticker]['Progress'])    
    avg += data[ticker]['Progress']*(maxdate-mindate)/( pd.to_datetime('2019-12-30') - pd.to_datetime('2019-01-02'))
    
answer_part_1 = avg/N
print('AVG:',answer_part_1)

# I've calculated % change between close at 31st of December and open in 1st day of Jan, this worked


# In[ ]:


# Ticker:
#     Date: 2019-01-02 00:00:00 Open: 93.910004 
#     Date: 2019-12-30 00:00:00 Close: 124.300003 
#     Progress: 32.36076850768743


# <br>
# 
# **Question 2.** What company's stock price grew the most (in %)? Enter ticker of the company as an answer)

# In[123]:


maxGrew = -100000
maxGrewCompany = ''
for ticker in dow_jones_companies:
    progress = data[ticker]['Progress']
    print('Ticker:', ticker, 'progress:', progress)
    if maxGrew < progress:
        maxGrew = progress
        maxGrewCompany = ticker
answer_part_2 = maxGrewCompany
print(answer_part_2)


# <br>
# 
# **Question 3.** What company's stock lost in price the most (in %)? Enter ticker of the company as an answer

# In[125]:


minGrew = 100000
minGrewCompany = ''
for ticker in dow_jones_companies:
    progress = data[ticker]['Progress']
    print('Ticker:', ticker, 'progress:', progress)
    if minGrew > progress:
        minGrew = progress
        minGrewCompany = ticker
answer_part_3 = minGrewCompany
print(answer_part_3)


# <br>
# 
# **Question 4.** What company had the largest summary volume over the year? Enter ticker of the company as an answer

# In[143]:


maxVolume = -100000
maxVolumeCompany = ''
for ticker in dow_jones_companies:
    df = data[ticker]['table']
    data[ticker]['SummaryVolume'] = df.Volume.sum()
    if data[ticker]['SummaryVolume'] >maxVolume:
        maxVolume = data[ticker]['SummaryVolume']
        maxVolumeCompany = ticker
answer_part_4 = maxVolumeCompany
print('Max Volume company:',answer_part_4)


# <br>
# 
# **Question 5.** What is the biggest stock price daily increase (in %)? Enter the number 

# In[177]:


maxVol = np.zeros(N)
maxTick = ''
for i,ticker in enumerate(dow_jones_companies):
    df = data[ticker]['table']
    df['Change'] = df.apply(lambda row: 100*(row.Close/row.Open - 1), axis=1) # Create new column with 100*(Close/Open - 1)
    
    maxVol[i] = df['Change'].max()
arg = np.argmax(maxVol)
    
print(maxVol)        
answer_part_5 = maxVol.max()


# <br><br>
# 
# **Question 6.** What is the company that had the biggest stock price daily increase? Enter ticker of the company as an answer

# In[180]:


print(dow_jones_companies[arg]) 
answer_part_6 = dow_jones_companies[arg]


# <br>
# 
# **Question 7.** What is the biggest stock price daily decrease (in %)? Enter the number

# In[196]:


minVol = np.zeros(N)

for i,ticker in enumerate(dow_jones_companies):
    df = data[ticker]['table']
    df['Change'] = df.apply(lambda row: 100*(row.Close/row.Open - 1), axis=1) # Create new column with 100*(Close/Open - 1)
    
    minVol[i] = df['Change'].min()
arg_min = np.argmin(minVol)
    
print(minVol)        
answer_part_7 = minVol.min()


# <br>
# 
# **Question 8.** What is the company that had the biggest stock price daily decrese (in %)? Enter ticker of the company as an answer

# In[199]:


answer_part_8 = dow_jones_companies[arg_min]

