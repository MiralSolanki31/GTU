#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
sales_data=pd.read_csv('sales.csv')
sales_data


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
sales_data=pd.read_csv('sales.csv')
sales_data


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('sales.csv')

monthly_profit = sales_data.groupby('month_name')['total_profit'].sum()

plt.plot(monthly_profit.index, monthly_profit.values)

plt.title('Total Profit of All Months')
plt.xlabel('Month_name')
plt.ylabel('Total Profit')
plt.show()


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('sales.csv')

monthly_profit = sales_data.groupby('month_name')['total_profit'].sum()

plt.plot(monthly_profit.index, monthly_profit.values,linestyle='dotted', color='blue')

plt.title('Total Profit of All Months')
plt.xlabel('Month_name')
plt.ylabel('Total Profit')
plt.show()


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('sales.csv')

monthly_profit = sales_data.groupby('month_name')['total_profit'].sum()

plt.plot(monthly_profit.index, monthly_profit.values, linestyle='dotted', color='blue', label='Total Profit')

plt.title('Total Profit of All Months')
plt.xlabel('Month Name')
plt.ylabel('Total Profit')
plt.legend(loc='upper right')
plt.show()


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('sales.csv')

monthly_profit = sales_data.groupby('month_name')['total_profit'].sum()

plt.plot(monthly_profit.index, monthly_profit.values,linestyle='dotted', color='blue')

plt.title('Total Profit of All Months')
plt.xlabel('Month number')
plt.ylabel('Total Profit')
plt.show()


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('sales.csv')

monthly_profit = sales_data.groupby('month_name')['total_profit'].sum()

plt.plot(monthly_profit.index, monthly_profit.values,linestyle='dotted', color='blue')

plt.title('Total Profit of All Months')
plt.xlabel('Month number')
plt.ylabel('Item Sold units number')
plt.show()


# In[9]:


import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('sales.csv')

monthly_profit = sales_data.groupby('month_name')['total_profit'].sum()

plt.plot(monthly_profit.index, monthly_profit.values, linestyle='dotted', color='blue', marker='o',label='Total Profit')

plt.title('Total Profit of All Months')
plt.xlabel('Month Name')
plt.ylabel('Total Profit')
plt.legend(loc='upper right')
plt.show()


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('sales.csv')

monthly_profit = sales_data.groupby('month_name')['total_profit'].sum()

plt.plot(monthly_profit.index, monthly_profit.values, linestyle='dotted', color='blue', marker='o',markeredgecolor='yellow',label='Total Profit')

plt.title('Total Profit of All Months')
plt.xlabel('Month Name')
plt.ylabel('Total Profit')
plt.legend(loc='upper right')
plt.show()


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('sales.csv')

monthly_profit = sales_data.groupby('month_name')['total_profit'].sum()

plt.plot(monthly_profit.index, monthly_profit.values, linestyle='dotted', linewidth=5,color='blue', marker='o',markeredgecolor='yellow',label='Total Profit')

plt.title('Total Profit of All Months')
plt.xlabel('Month Name')
plt.ylabel('Total Profit')
plt.legend(loc='upper right')
plt.show()


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('sales.csv')

sales_data['year'] = pd.to_datetime(sales_data['date']).dt.year

last_year_sales = sales_data[sales_data['year'] == 2022]
product_sales = last_year_sales.groupby('product')['units_sold'].sum()

plt.pie(product_sales.values, labels=product_sales.index, autopct='%1.1f%%')
plt.title('Total Unit Sales by Product in 2022')
plt.show()


# In[13]:


import matplotlib.pyplot as plt
import numpy as np

# create an array of x values
x = np.linspace(-10, 10, 100)

# calculate y values for the parabola
y = x ** 2

# plot the parabola
plt.plot(x, y)

# add text to the plot
plt.text(0, 50, "Parabola $Y = x^2$",
         fontsize=14, ha='center')

# set axis labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Parabola $Y = x^2$")

# display the plot
plt.show()


# In[14]:


import matplotlib.pyplot as plt

# Data
a = [12, 3, 4, 5,6]  # added an extra element
b = [16, 234, 25, 90, 32]

# Create bar plot
plt.bar(a, b)

# Set labels for x and y axis
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Set title of the plot
plt.title('Bar Plot')

# Show the plot
plt.show()


# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("sales.csv")
total_profit=df['total_profit'].tolist()
Month=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
total_profit=[239600,240500,204600,271100,174700,236300,212000,265000,202600,237800,294200,336800]
plt.axis("equal")
plt.axis()
plt.pie(total_profit, labels=Month)
plt.show()


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("sales.csv")
total_profit=df['total_profit'].tolist()
Month=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
total_profit=[239600,240500,204600,271100,174700,236300,212000,265000,202600,237800,294200,336800]
plt.axis("equal")
plt.axis()
plt.pie(total_profit, labels=Month)
plt.show()


# In[ ]:





# In[ ]:




