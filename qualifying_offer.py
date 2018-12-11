# importing necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# I followed the link below to learn how to read in the table of data from the website
# https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059
url = 'https://questionnaire-148920.appspot.com/swe/data.html'
tables = pd.read_html(url)
data = tables[0]
if (data.empty):
    raise Exception("Table was not read in correctly.")

# removes null values and players with "no salary data" from dataframe
num_players = len(data)
data = data.dropna()
data = data[data['Salary'] != "no salary data"]
num_valid = len(data)
# extracts corrected salary column from dataframe
salary = data['Salary']

# I followed the answers at the link below to learn how to parse the salary data from strings with $ and , to floats
# https://stackoverflow.com/questions/31521526/convert-currency-to-float-and-parentheses-indicate-negative-amounts/31521773

# converts currency values to floats
salary = salary.replace('[\$,]','', regex=True).astype(float)
# sorts salary values in descending order and selects the 125 largest values
salary = salary.sort_values(ascending = False)
top_125 = salary[0:125]
offer = round(top_125.mean(), 2)
print("\nQUALIFYING OFFER")
print("The value of the qualifying offer is ${:,}".format(offer))

# head of the dataset and number of elements
print("\nHEAD OF DATASET (CORRECTED FOR MISSING VALUES)")
print(data.head(n = 5))
print("\nOf the {} players in the data, {} had valid salary data.".format(num_players, num_valid))

# five number summary and mean of the salaries
print("\nFIVE NUMBER SUMMARY AND MEAN OF SALARY")
print("Minimum Salary :: ${:,.2f}".format(salary.min()))
print("Q1 Salary  :: ${:,.2f}".format(np.percentile(salary, 25)))
print("Median Salary  :: ${:,.2f}".format(salary.median()))
print("Mean Salary :: ${:,.2f}".format(salary.mean()))
print("Q3 Salary  :: ${:,.2f}".format(np.percentile(salary, 75)))
print("Maximum Salary :: ${:,.2f}\n".format(salary.max()))

# distribution of salaries
# converting salaries to millions for sake of plot readability
graphing_salary = salary / 1000000
plt.figure(figsize = (10, 5))
plt.title("Salary Distribution for All Players (Dollars in Millions)")
plt.xlabel("Salary (in millions of dollars)")
plt.ylabel("Frequency")
plt.xticks(np.arange(0, 40, step = 2.5))
plt.hist(graphing_salary, bins = 15, color = "b")

# distribution of the top 125 salaries for a closer look
# converting salaries to millions for sake of plot readability
graphing_top_125 = top_125 / 1000000
plt.figure(figsize = (8, 5))
plt.title("Distribution of the 125 Largest Salaries (Dollars in Millions)")
plt.xlabel("Salary (in millions of dollars)")
plt.ylabel("Frequency")
plt.xticks(np.arange(0, 40, step = 2.5))
plt.hist(graphing_top_125, bins = 8, color = "r")

plt.show()




