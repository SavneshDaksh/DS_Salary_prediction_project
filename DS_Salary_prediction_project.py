#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Libraries

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as  plt
import seaborn as sbn
import warnings
warnings.filterwarnings("ignore")


# In[3]:


df = pd.read_csv("C:\\Users\\PCC\\Downloads\\archive.csv\\ds_salaries.csv")


# In[4]:


df


# # Exploratory Data Analysis

# In[ ]:


# Unlike .describe(), .info() gives us a shorter summary of our dataset. It returns us information about the data type, 
# non-null values and memory usage.


# In[5]:


# Data Information

df.info()


# In[22]:


# The describe function does exactly this: it provides purely descriptive information about the dataset. This information 
# includes statistics that summarize the central tendency of the variable, their dispersion, the presence of empty values and their shape.

df.describe()


# In[23]:


# Data Correletion

df.corr()


# In[9]:


# Top values

df.head()


# In[10]:


# Lower values

df.tail()


# In[11]:


# If we apply .shape on the dataset, Pandas returns us a pair of numbers that represent the dimensionality of our dataset. 
# This property is very useful for understanding the number of columns and the length of the dataset.

df.shape


# In[14]:


# Count of value

df.count()


# In[15]:


# Mean values

df.mean()


# In[17]:


# std values

df.std()


# In[18]:


# Minimum values

df.min()


# In[19]:


# maximum values

df.max()


# In[24]:


# To check for duplicate rows we can use .isduplicated().sum()— this will print us the number of duplicated rows in our 
# dataset


df.duplicated()


# In[25]:


# Sum of Duplicate values

df.duplicated().sum()


# In[26]:


# In this context, .value_counts() is one of the most important functions to understand how many values of a given variable 
# there are in our dataset. Let’s take the target variable for example.

df.salary.value_counts()


# In[28]:


# You can also express the data as a percentage by passing normalize = True

df.salary.value_counts(normalize = True)


# In[29]:


# Numeric variables in salary column

df.salary.describe()


# # Missing Value Analysis

# In[30]:


# Checking for missing values using isnull()


df.isnull()


# In[31]:


# Checking for missing values using notnull()

df.notnull()


# In[33]:


# Filling missing values using fillna(), replace() and interpolate()

# filling missing value using fillna()  

df.fillna(0)


# In[35]:


# filling a missing value with
# previous ones

df.fillna(method="pad")


# In[36]:


# filling  null value using fillna() function  

df.fillna(method="bfill")


# In[42]:


# Printing the first 51 to 101 rows of
# the data frame for visualization 

df[51:102]


# In[49]:


# using dropna() function  

df.dropna()


# In[50]:


# using dropna() function with axis = 1 

df.dropna(axis = 1)


# # Data Visualization with Graph

# In[59]:


sbn.heatmap(df.corr())
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# In[64]:


plt.plot(df.salary.head(50),color='orange',marker='*',markeredgecolor='red')
plt.title('DS_Salary')
plt.xlabel('Salary')
plt.ylabel('Y')


# In[68]:


plt.boxplot(df['work_year'])
plt.title('Work_year Column')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# In[78]:


plt.figure(figsize=(16,6))
plt.subplot(1,2,1)
plt.plot(df.work_year,marker='*',markeredgecolor='orange',alpha=0.9,linestyle='solid',color='red')
plt.title('work_year')
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(1,2,2)
plt.plot(df.salary,marker='*',markeredgecolor='orange',alpha=0.9,linestyle='solid',color='red')
plt.title('salary')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[84]:


plt.hist(df.work_year,color='orange')
plt.title('work_year')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()


# In[88]:


plt.boxplot(df['salary_in_usd'])
plt.title("salary_in_usd")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# In[ ]:




