#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
from urllib.request import urlopen


# In[2]:


df = pd.read_csv(r"E:\Property\property.csv")
df


# In[3]:


df.info()


# In[4]:


df.describe()


# In[5]:


df.isna().sum()


# In[6]:


df.isna().sum().plot(kind='bar')


# In[7]:


# Finding out the percent of missing values
percent_missing = df.isnull().sum() * 100 / len(df)
print(percent_missing)


# In[8]:


#Filter Altona Data set
Altona_df = df[(df['Suburb'] == 'Altona')]
Altona_df


# In[9]:


(df['Suburb'] == 'Altona').value_counts()


# In[10]:


Altona_df.info()


# In[11]:


Altona_df.isna().sum()


# In[12]:


# Finding out the percent of missing values
percent_missing = Altona_df.isnull().sum() * 100 / len(df)
print(percent_missing)


# In[13]:


Altona_df.isna().sum().plot(kind='bar')


# In[14]:


# Catagorical Columns
list_cate = []

for i in list(Altona_df.columns):
    if Altona_df[i].dtype == 'O': # O reffers to object
        print(i)
        list_cate.append(i)


# In[15]:


#Numerical columns
set(list_cate) ^ set(list(Altona_df.columns))


# In[16]:


import matplotlib.pyplot as plt

Altona_df.hist(figsize=(20,14))
plt.show()


# #### Inputing numerical values

# In[17]:


#missing values in Item_weight and Outlet_size needs to be imputed
Altona_df['BuildingArea'].fillna('BuildingArea', inplace=True)

Altona_df['CouncilArea'].fillna('CouncilArea', inplace=True)

Altona_df['YearBuilt'].fillna(method='ffill', inplace=True)

Altona_df['Car'].fillna(method='bfill', inplace=True)


# In[18]:


print(Altona_df)


# In[19]:


Altona_df


# In[20]:


Altona_df.info()


# In[21]:


import matplotlib.pyplot as plt

Altona_df.hist(figsize=(20,14))
plt.show()


# In[22]:


plt.figure(figsize=(18,18))

plt.subplot(2,2,4)
Altona_df['YearBuilt'].value_counts().plot(kind='bar')


# In[23]:


# 1.For the suburb Altona, it is postulated that a typical property sells for $800,000. Use the data at hand to test this assumption. 
#Is the typical property price really $800,000 or has it increased? Use a significance level of 5%. 


# ### Set up the hypothesis:
# #### Null hypothesis ((H_0)): The mean property price is 800,000.
# #### Alternative hypothesis ((H_1)): The mean property price is greater than 800,000.

# In[24]:


import numpy as np
from scipy import stats


# In[25]:


Altona_df['Price']


# In[26]:


# Hypothesized mean price
mu = 800000


# In[27]:


# Perform one-sample t-test
t_statistic, p_value = stats.ttest_1samp(Altona_df['Price'], mu)


# In[28]:


# Print the results
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")


# In[29]:


# Determine if we reject the null hypothesis
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. The mean property price is significantly greater than $800,000.")
else:
    print("Fail to reject the null hypothesis. There is not enough evidence to say the mean property price is greater than $800,000.")


# In[30]:


#2. For the year 2016, is there any difference in prices of properties sold in the summer months vs winter months?
#Consider months from October till March as winter months and the rest as summer months. Use a significance level of 5%. 


# In[31]:


#Extracting month from date

import datetime as dt


# In[32]:


Altona_df['Date']=pd.to_datetime(Altona_df['Date'])


# In[33]:


Altona_df['Month']=Altona_df['Date'].dt.month


# In[34]:


Altona_df.head()


# In[35]:


# Define summer and winter months
summer_months = [4, 5, 6, 7, 8, 9]
winter_months = [10, 11, 12, 1, 2, 3]


# In[36]:


# Split the data into summer and winter groups
summer_prices = Altona_df[Altona_df['Date'].dt.month.isin(summer_months)]['Price']
winter_prices = Altona_df[Altona_df['Date'].dt.month.isin(winter_months)]['Price']


# In[37]:


# Perform independent two-sample t-test
t_statistic, p_value = stats.ttest_ind(summer_prices, winter_prices, equal_var=False)


# In[38]:


# Print the results
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")


# In[39]:


# Determine if we reject the null hypothesis
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference in property prices between summer and winter months.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in property prices between summer and winter months.")


# #### Abbotsford Data set

# In[40]:


#Filter Abbotsford Data set
Abbotsford_df = df[(df['Suburb'] == 'Abbotsford')]
Abbotsford_df


# In[41]:


(df['Suburb'] == 'Abbotsford').value_counts()


# In[43]:


Abbotsford_df.info()


# In[44]:


Abbotsford_df.isna().sum()


# In[46]:


# Finding out the percent of missing values
percent_missing2 = Abbotsford_df.isnull().sum() * 100 / len(df)
print(percent_missing2)


# In[47]:


Abbotsford_df.isna().sum().plot(kind='bar')


# In[48]:


# Catagorical Columns
list_cate = []

for i in list(Abbotsford_df.columns):
    if Abbotsford_df[i].dtype == 'O': # O reffers to object
        print(i)
        list_cate.append(i)


# In[49]:


#Numerical columns
set(list_cate) ^ set(list(Abbotsford_df.columns))


# In[50]:


import matplotlib.pyplot as plt

Abbotsford_df.hist(figsize=(20,14))
plt.show()


# #### Inputing numerical values

# In[51]:


#missing values in Item_weight and Outlet_size needs to be imputed
Abbotsford_df['BuildingArea'].fillna('BuildingArea', inplace=True)

Abbotsford_df['CouncilArea'].fillna('CouncilArea', inplace=True)

Abbotsford_df['YearBuilt'].fillna(method='ffill', inplace=True)


# In[53]:


print(Abbotsford_df)


# In[54]:


Abbotsford_df


# In[55]:


Abbotsford_df.info()


# In[56]:


import matplotlib.pyplot as plt

Abbotsford_df.hist(figsize=(20,14))
plt.show()


# In[58]:


plt.figure(figsize=(18,18))

plt.subplot(2,2,4)
Abbotsford_df['YearBuilt'].value_counts().plot(kind='bar')


# In[ ]:


## 3. For the suburb Abbotsford, what is the probability that out of 10 properties sold, 3 will not have car parking? 
## Use the column car in the dataset. Round off your answer to 3 decimal places. 


# In[60]:


# Calculate the probability of a property not having car parking
p = 1 - (Abbotsford_df['Car'].sum() / len(Abbotsford_df))


# In[62]:


p


# In[64]:


from scipy.stats import binom


# In[65]:


# Number of trials (properties sold)
n = 10

# Number of successes (properties without car parking)
k = 3

# Calculate the binomial probability
probability = binom.pmf(k, n, p)

# Round off the result to 3 decimal places
rounded_probability = round(probability, 3)

print(f"The probability that out of 10 properties sold, 3 will not have car parking is {rounded_probability}")


# In[ ]:


#4. In the suburb Abbotsford, what are the chances of finding a property with 3 rooms?
# Round your answer to 3 decimal places. 


# In[68]:


# Calculate the number of properties with 3 rooms
num_properties_with_3_rooms = Abbotsford_df[Abbotsford_df['Rooms'] == 3].shape[0]
num_properties_with_3_rooms


# In[70]:


# Calculate the total number of properties in Abbotsford
total_properties = Abbotsford_df.shape[0]
total_properties


# In[72]:


# Calculate the probability
probability = num_properties_with_3_rooms / total_properties
probability


# In[73]:


# Round off the result to 3 decimal places
rounded_probability = round(probability, 3)

print(f"The probability of finding a property with 3 rooms in Abbotsford is {rounded_probability}")


# In[ ]:


## 5. In the suburb Abbotsford, what are the chances of finding a property with 2 bathrooms? 
#Round your answer to 3 decimal places.


# In[77]:


# Calculate the number of properties with 2 bathrooms
num_properties_with_2_bathrooms = Abbotsford_df[Abbotsford_df['Bathroom'] == 2].shape[0]
num_properties_with_2_bathrooms


# In[78]:


# Calculate the total number of properties in Abbotsford
total_properties = Abbotsford_df.shape[0]
total_properties


# In[79]:


# Calculate the probability
probability = num_properties_with_2_bathrooms / total_properties
probability


# In[80]:


# Round off the result to 3 decimal places
rounded_probability = round(probability, 3)

print(f"The probability of finding a property with 2 bathrooms in Abbotsford is {rounded_probability}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




