#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv(r'C:\Users\MahmoudMohamedHel202\Desktop\Visualzation  ملف عمل\Orders (1).csv')


# In[3]:


df


# In[4]:


df.plot(x='Category',y='Total Cost')  


# In[5]:


Country_ordrs=df['Category'].value_counts()
Country_ordrs


# In[6]:


Country_ordrs.plot(kind='bar',title ="ordrs & Country")


# In[7]:


df


# In[9]:


cat_totalcost=df.groupby('Category')['Total Cost'].sum()


# In[11]:


cat_totalcost.plot(kind='barh',color='r',xlabel='Total Cost (Millions)',title='Total Cost by Category')


# In[15]:


cat_Quan_TotCost=df.groupby('Category')[['Quantity','Total Cost']].sum()
cat_Quan_TotCost


# In[19]:


cat_Quan_TotCost.plot(subplots=True)


# In[32]:


s_axis= cat_Quan_TotCost.plot(y='Total Cost',kind='bar',color='g',ylabel='Total Cost (Millions)')
cat_Quan_TotCost.plot(y='Quantity',kind='line',secondary_y=True,ax=s_axis,color='r',ylabel='Quantity',rot=45)


# In[ ]:




