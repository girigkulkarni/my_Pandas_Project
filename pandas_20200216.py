# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 17:47:35 2020

@author: girig
"""
import pandas as pd
import csv
#2 main datatypes
#1 - Series
series=pd.Series(['BMW','Toyota','Honda'])
series
#Series = 1-dimensional
colours=pd.Series(['Red', 'Blue', 'Whilte'])
colours
#DataFrame=2 Dimensional
car_data=pd.DataFrame({'Car name':series,'Colour':colours})
car_data
#importing data
car_sales = pd.read_csv("car-sales.csv")
car_sales
car_sales.to_csv('exported-car-sales.csv')


## Describe data -m

car_sales.dtypes

car_sales.columns

car_sales.index

car_sales.describe()

car_sales.info()

car_sales.mean()

len(car_sales)

##Viewing and selecting data m


animals=pd.Series(['cat','dog','panda','bird','snake'],index=[0,3,2,1,3])
animals
animals.loc[3]
animals.iloc[3]

car_sales

car_sales['Price']=car_sales['Price'].str.replace('[\$\,]','').astype(float)

car_sales['Price'].plot()

pd.crosstab(car_sales['Make'],car_sales['Doors'])

car_sales.groupby(['Make']).mean()

car_sales['Odometer (KM)'].hist()

giri=pd.read_excel('test_xl.xlsx',None)
giri
temp1=giri['Sheet1']
temp1
temp2=giri['Sheet2']
temp2



