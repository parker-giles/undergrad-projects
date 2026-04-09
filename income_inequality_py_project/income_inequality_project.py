# Notice: This uses a inaccurate/truncated data set as the maximum income is at $250001. 

import requests 
import numpy as np
import matplotlib.pyplot as plt

response = requests.get("https://api.census.gov/data/2022/acs/acs5?get=NAME,B19013_001E&for=zip%20code%20tabulation%20area:*")
data = response.json()

# defining the headers and rows
headers = data[0]
rows = data [1:]

# defining the columns 
zip_codes = []
nincomes = []

# cleaning data

for row in rows:
    name = row[0]
    income = row[1]

    if income is None or income == "":
        continue
    try:
        income = int(income)
        zip_codes.append(name)
        nincomes.append(income)
    except:
        continue

# This gets rid of the "-66666666" outliers in the data.
nincomes = np.array(nincomes)
incomes = nincomes[nincomes>=0]


print(f"Total number of ZIP codes: {len(incomes)}")

# Basic stats
mean_income = np.mean(incomes)
median_income = np.median(incomes)
std_income = np.std(incomes)

print(f"mean income: ${mean_income:,.2f}")
print(f"median income: ${median_income:,.2f}")
print(f"Standard Deviation: ${std_income:,.2f}")

sorted_indices = np.argsort(incomes)

lowest_10 = incomes[sorted_indices[:10]]
highest_10 = incomes[sorted_indices[-10:]]

print(f"lowest 10 incomes: {lowest_10}")
print(f"highest 10 incomes: {highest_10}")

plt.hist(incomes, bins=12, edgecolor = 'black')
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.title('Incomes')

# inequality with lonrenz curve

sorted_income = np.sort(incomes)
cumulative_income = np.cumsum(sorted_income)
cumulative_income = cumulative_income / cumulative_income[-1] 

population = np.arange(1, len(sorted_income)+1) / len(sorted_income)

plt.figure(figsize=(6,6))
plt.plot(population, cumulative_income, label="Lorenz Curve")
plt.plot([0,1],[0,1], linestyle="--", label="perfect equality")

plt.title("income inequality with lorenz curve")
plt.xlabel("cumulative popualtion")
plt.ylabel("cumulative income")
plt.legend()
plt.show()