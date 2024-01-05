#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing pandas and numpy 
import pandas as pd
import numpy as np


# In[2]:


#reading your csv file
df = pd.read_csv(r'F:\PA1_Tirmanwar\Input\raw_2004car.csv')


# In[3]:


#checking data types
df.dtypes


# In[4]:


#last 5 values 
df.tail()


# In[5]:


df


# In[6]:


df.dtypes


# In[7]:


# Dropping[*]
drop_idx = []
for col in df.columns:
    for idx in df.index:
        if df[col][idx] == "*":
            print(idx)
            drop_idx.append(idx)


# In[8]:


df = df.drop(drop_idx, 0)


# In[9]:


#Save the nation where a manufacturer's headquarter is located
GER = ['Porsche','Audi','BMW','Mercedes-Benz','Mini', 'Volkswagen']
JPN = ['Acura', 'Honda','Infiniti','Isuzu','Lexus','Mazda','Mitsubishi','Nissan','Scion','Subaru','Suzuki','Toyota']
KOR = ['Hyundai','Kia']
SWD = ['Saab', 'Volvo']
UK = ['Jaguar', 'Land']
USA = ['Buick','Cadillac','Chevrolet','Chrysler','Dodge','Ford','GMC','Hummer' ,'Jeep','Lincoln' ,'Mercury' ,'Oldsmobile' ,'Pontiac' ,'Saturn']


# In[10]:


#creating empty list of country and continent
country = []
continent = []


# In[11]:


country 


# In[12]:


continent


# In[13]:


#Inserting column
for idx in df.index:
    manu = df['Vehicle Name'][idx].split(" ")[0]
    if manu in GER:
        country.append("GER")
        continent.append("Europe")
    elif manu in JPN:
        country.append("JPN")
        continent.append("Asia")
    elif manu in KOR:
        country.append("KOR")
        continent.append("Asia")
    elif manu in SWD:
        country.append("SWD")
        continent.append("Europe")
    elif manu in UK:
        country.append("UK")
        continent.append("Europe")
    elif manu in USA:
        country.append("USA")
        continent.append("North America")
    else:
        print("Something wrong")
        


# In[14]:


print(country)


# In[15]:


print(continent)


# In[16]:


#inserting your nationality column
df.insert(0, 'Nationality',country)


# In[17]:


#inserting your continent column
df.insert(1, 'Continent',continent)


# In[18]:


df


# In[19]:


df.head()


# In[20]:


#rename to Sedan
df=df.rename(columns={"Small/Sporty/ Compact/Large Sedan":"Sedan"})


# df3

# In[21]:


#creating a new list car_type
car_type=[]
#inserting column 
for index,rows in enumerate(df.iterrows()):
    if df.iloc[index][3]==1:
        car_type.append(df.columns[3])
    elif df.iloc[index][4]==1:
        car_type.append(df.columns[4])
    elif df.iloc[index][5]==1:
        car_type.append(df.columns[5])
    elif df.iloc[index][6]==1:
        car_type.append(df.columns[6])
    elif df.iloc[index][7]==1:
        car_type.append(df.columns[7])
    elif df.iloc[index][8]==1:
        car_type.append(df.columns[8])


# In[22]:


#lenghth of car type
len(car_type)


# In[23]:


#inserting vehicle type column
df.insert(3, 'Vehicle Type',car_type)


# In[24]:


df.info()


# ### 

# In[25]:


#creating a  empty list wheel drive type
Wheel_drive_type=[]
#inserting column
for index,rows in enumerate(df.iterrows()):
    if df.iloc[index][10]==1:
        Wheel_drive_type.append(df.columns[10])
    elif df.iloc[index][11]==1:
        Wheel_drive_type.append(df.columns[11])
    else:
         Wheel_drive_type.append('NA')


# In[26]:


#inserting wheel drive type column
df.insert(4, 'Wheel drive type',Wheel_drive_type)


# In[27]:


df.head()


# In[28]:


df['City MPG']=df['City MPG'].astype(str).astype(int)
df['Hwy MPG']=df['City MPG'].astype(str).astype(int)
#weighted average of City MPG*0.55 + Hwy MPG*0.45
df['Combined MPG']=df['City MPG']*0.55+df['Hwy MPG']*0.45


# In[29]:


#average
df['Combined MPG']


# In[30]:


df.head()


# In[31]:


drop_idx = []
for col in df.columns:
    for idx in df.index:
        if df[col][idx] == "*":
            print(idx)
            drop_idx.append(idx)


# In[32]:


df.iloc[72]


# In[33]:


#dropping columns 
df=df.drop(['Sedan','Sports Car','SUV','Wagon','Minivan','Pickup','AWD','RWD',], axis=1)


# In[34]:


df.columns


# In[35]:


df.head()


# In[36]:


df.shape


# In[37]:


df.head()


# In[38]:


df.shape


# In[39]:


df.columns


# In[41]:


#exporting to output folder
df.to_csv('F:/PA1_Tirmanwar/Output/refined_2004car.csv')


# In[ ]:




