import pandas as pd

covid_df = pd.read_csv("F:\Data-Science-Notes\Practice\Pandas\italy-covid-daywise.csv")

print(covid_df)
print(covid_df.info())
print(covid_df.describe())
print(covid_df.columns)
print(covid_df.shape)

print(covid_df['new_cases']) 

print(type(covid_df['new_cases'])) 

print(covid_df['new_cases'][246])  

print(covid_df.at[241, 'new_cases'])  

print(covid_df.new_cases) 

print(covid_df[['new_cases', 'date']])  

subset = covid_df[['new_cases', 'date']].copy()

print(covid_df.loc[243])  

print(covid_df.head(5))  
print(covid_df.tail(5))  

print(covid_df.loc[108:113])  

print(covid_df.new_tests.first_valid_index())  

print(covid_df.sample(10)) 