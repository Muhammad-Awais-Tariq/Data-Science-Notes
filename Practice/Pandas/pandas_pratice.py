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

sorted_df = covid_df.sort_values('new_cases')

sorted_df = covid_df.sort_values('new_cases', ascending=False)

top_10_cases = covid_df.sort_values('new_cases', ascending=False).head(10)

sorted_df = covid_df.sort_values(['new_cases', 'new_deaths'], ascending=False)

faulty_rows = covid_df[covid_df.new_cases < 0]

covid_df.at[172, 'new_cases'] = 0

column_average = covid_df.new_cases.mean()
covid_df.at[172, 'new_cases'] = column_average

covid_df.at[172, 'new_cases'] = (covid_df.at[171, 'new_cases'] + covid_df.at[173, 'new_cases']) / 2

covid_df.drop(172, inplace=True)

covid_df.sort_values('new_cases', ascending=False).head(10)

print(covid_df.date)         
print(covid_df.date.dtype)   

covid_df["date"] = pd.to_datetime(covid_df.date)

covid_df["year"]    = pd.DatetimeIndex(covid_df.date).year
covid_df["month"]   = pd.DatetimeIndex(covid_df.date).month
covid_df["day"]     = pd.DatetimeIndex(covid_df.date).day
covid_df["weekday"] = pd.DatetimeIndex(covid_df.date).weekday

covid_df_may = covid_df[covid_df.month == 5]

covid_df_2020 = covid_df[covid_df.year == 2020]

covid_df_sundays = covid_df[covid_df.weekday == 6]

covid_df_may_total = covid_df[covid_df.month == 5][['new_cases', 'new_deaths', 'new_tests']].sum()

overall_mean = covid_df.new_cases.mean()
sunday_mean  = covid_df[covid_df.weekday == 6].new_cases.mean()

covid_month_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()

covid_df["total_cases"] = covid_df.new_cases.cumsum()

covid_df["total_deaths"] = covid_df.new_deaths.cumsum()
covid_df["total_tests"]  = covid_df.new_tests.cumsum()

location_df = pd.read_csv("locations.csv")

location_df[location_df.location == "Italy"]

covid_df["location"] = "Italy"

merged_df = covid_df.merge(location_df, on="location")

merged_df["cases_per_million"]  = merged_df.total_cases  * 1e6 / merged_df.population
merged_df["deaths_per_million"] = merged_df.total_deaths * 1e6 / merged_df.population
merged_df["tests_per_million"]  = merged_df.total_tests  * 1e6 / merged_df.population

result_df = merged_df[['date', 'new_cases', 'total_cases', 'cases_per_million']]

print(result_df.head())
print(result_df.shape)

result_df.to_csv("results.csv", index=False)

result_df.to_excel("results.xlsx", index=False)   
result_df.to_json("results.json")                 
result_df.to_parquet("results.parquet", index=False)  

result_df.set_index('date', inplace=True)

result_df.new_cases.plot()

result_df.new_cases.plot()
result_df.new_deaths.plot()

death_rate = result_df.total_deaths / result_df.total_cases
death_rate.plot(title="Death Rate Over Time")

covid_month_df.new_cases.plot(kind="bar")

covid_month_df.new_deaths.plot(kind="bar")