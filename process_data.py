#%% 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
%matplotlib inline 

#%%
!ls

#%%
house_of_wines_df = pd.read_csv('house_of_wines2.csv')
majestic_wines_df = pd.read_csv('majestic_wines2.csv')


#%%
house_of_wines_df.head()

#%%
majestic_wines_df.head()

#%%
majestic_wines_df.info()

#%%
house_of_wines_df.info()

#%%
wines_df = pd.concat([house_of_wines_df,majestic_wines_df])

#%%
wines_df.head()

#%%
wines_df.info()

#%%
wines_df.alcohol_percent = wines_df.alcohol_percent.map(lambda x: str(x).replace(',','.')).astype('float64')

#%%
wines_df.alcohol_percent.fillna(wines_df.alcohol_percent.mean(),inplace=True)

#%%
wines_df.producer.fillna('Unkwon Producer',inplace=True)

#%%
wines_df.producer


#%%
wines_df.wine_color.value_counts()

#%%
wines_df.wine_color.fillna('Red',inplace=True)


#%%
wines_df.year = wines_df.year.astype(str).map(lambda x :x.replace('.0',''))

#%%
wines_df.to_csv('wines_final.csv')

#%%
