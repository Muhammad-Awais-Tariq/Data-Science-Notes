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

total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()

print(total_cases)
print(total_deaths)

death_rate = total_deaths / total_cases
print(death_rate)

initial_tests = 935310
total_tests_complete = initial_tests + covid_df.new_tests.sum()
print(total_tests_complete)

positive_rate = total_cases / total_tests_complete
print(positive_rate)

high_new_cases = covid_df.new_cases > 1000
print(high_new_cases) 

filtered_df = covid_df[high_new_cases]
print(filtered_df)  

high_new_cases_df = covid_df[covid_df.new_cases > 1000]

# from ipython.display import display
 
# with pd.option_context('display.max_rows', 100):
#     display(covid_df[covid_df.new_cases > 1000])

positive_rate_avg = covid_df.new_cases.sum() / covid_df.new_tests.sum()
high_ratio_df = covid_df[covid_df.new_cases / covid_df.new_tests > positive_rate_avg]

covid_df['positive_rate'] = covid_df.new_cases / covid_df.new_tests

covid_df.drop(columns=['positive_rate'], inplace=True)

covid_df[(covid_df.new_cases > 1000) & (covid_df.new_deaths > 50)]

covid_df[(covid_df.new_cases > 1000) | (covid_df.new_deaths > 50)]