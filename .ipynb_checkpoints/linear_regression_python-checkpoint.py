#!/usr/bin/env python
# coding: utf-8

# This notebook demonstrates a simple linear regression analysis using Python to model Salary based on Years of Experience.

# In[2]:


import pandas as pd
dataset = pd.read_csv("regression_data.csv")


# In[3]:


import matplotlib.pyplot as plt
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")


# In[4]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# In[5]:


plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# In[6]:


model.score(dataset[["YearsExperience"]], dataset[["Salary"]])  # R-squared


# In[ ]:




