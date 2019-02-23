
# coding: utf-8

# In[6]:


import pandas as pd
import re
from sqlalchemy import create_engine


 ##MOBILITY
mobility = pd.read_excel('Mobility-in.xlsx',
                       #skiprows=1,         
                       header=[0],                   
                       skipfooter=13,                   
                       na_values='(NA)',                
                       usecols=10,                      
                       index_col=[0,1,2,3,4])



mobility =mobility.stack().reset_index()

mobility.level_5.replace(['Unnamed: 5'],['Same County'], inplace=True)

mobility.level_5.replace(['Unnamed: 6'],['Diff. County_Total'], inplace=True)

mobility.level_5.replace(['Unnamed: 7'],['Diff. County_Same State'], inplace=True)

mobility.level_5.replace(['Unnamed: 8'],['Diff. County_Diff State'], inplace=True)

mobility.rename(columns={'level_5':'Residence in US'}, inplace=True)

 


mobility.to_excel('mobility_clean.xls')



##Unemployment
#Read in the document from excel, skip 5 rows at top, and 7 rows at bottom (meta data). Set first column as index. 

unemployment=pd.read_excel ('Unemployment rate by state 2000-2017.xlsx', skiprows=5, header=[1], index_col=0, usecols=[0,1,2,3,4]) 

  

unemployment.to_excel(excel_writer='Unemployment Clean.xlsx',           

                sheet_name='divorce',                             

                na_rep='null',                                  

                index=False)   


##Divorce
#Read in the document from excel, skip 5 rows at top, and 7 rows at bottom (meta data). Set first column as index. 

divorce=pd.read_excel ('Divorce_Rates_Dirty.xlsx', skiprows=5, skipfooter=7, header=[0], index_col=0) 

#Deletes all null rows in the data set. 

divorce.dropna(how='all', inplace=True)   

#Stacks the states column which converts the dataset to long form.  

divorce = divorce.stack([0]).reset_index() 

#Renames the column headers to the appropriate name. 

divorce=divorce.rename(columns={'level_0':'state','level_1':'year', 0:'divorce_rate'}) 


divorce.to_excel(excel_writer='DIVORCE_CLEAN_PY.xlsx',           

                sheet_name='divorce',                            

                na_rep='null', index=False)              

  

##Median Income
median=pd.read_excel ('Median Household.xls', skiprows=3, header=[0], skipfooter=13) 

median=median.stack([0]).reset_index() 

median.rename(columns={'level_0':'Location'}, inplace=True)

median.to_excel(excel_writer='Median_clean.xls',

                sheet_name='Median',                           

                na_rep='null',                                   

                index=True)

##Property



prop=pd.read_csv ('PropertyCrimeDirty.csv', skiprows=0, skipfooter=0, header=[0], index_col=0) 

 

prop.dropna(how='all', inplace=True) 

 

prop = prop.stack().reset_index() 



prop=prop.rename(columns={'level_0':'year','level_1':'state', 0:'property_crime_rate'}) 

 

prop.to_csv('property-out.csv')


##Violent

violent=pd.read_csv ('ViolentCrimeDirty.csv', skiprows=0, skipfooter=0, header=[0], index_col=0) 



violent.dropna(how='all', inplace=True) 

 

violent = violent.stack().reset_index() 



violent=violent.rename(columns={'level_0':'year','level_1':'state', 0:'violent_crime_rate'}) 



violent.to_csv('violent-out.csv')

##Marriage

states =pd.read_csv('States.csv', skiprows=4, header=[1], index_col=[0])

states=states.stack().reset_index()

states.rename(columns={'level_0':'State','level_1':'Year',0:'Marriage Rate'},inplace=True)

states.to_csv('marriage-out.csv')

##Health
health = pd.read_csv('Health-in.csv', 
                     skiprows=5, 
                     header=[0], 
                     index_col=[0])

health.to_csv('health-out.csv')


