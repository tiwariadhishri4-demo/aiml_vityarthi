# aiml_vityarthi
This repo consist vityarthi project of AIML
# COVID-19 Data Analysis Project 

# Overview
This project analyzes COVID-19 data using Python libraries like Pandas, NumPy, and Matplotlib.

# Objectives
- Analyze COVID-19 cases
- Visualize trends using graphs
- Generate insights

# Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib

# PROGRAM CODE::::::
# ==============================
# COVID-19 Data Analysis Project
# ==============================

# Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Load Dataset
# Make sure covid_data.csv is in the same folder
df = pd.read_csv("covid_data.csv")

print("\n===== ORIGINAL DATA =====")
print(df)

# Step 3: Basic Information
print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATA INFO =====")
print(df.info())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# Step 4: Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Step 5: Create Active Cases Column
df['Active'] = df['Confirmed'] - df['Deaths'] - df['Recovered']

print("\n===== DATA AFTER PROCESSING =====")
print(df)

# Step 6: Numerical Analysis using NumPy
print("\n===== KEY INSIGHTS =====")
print("Maximum Confirmed Cases:", np.max(df['Confirmed']))
print("Maximum Deaths:", np.max(df['Deaths']))
print("Maximum Recoveries:", np.max(df['Recovered']))
print("Average Confirmed Cases:", np.mean(df['Confirmed']))

# Step 7: Line Graph (Trends Over Time)
plt.figure()
plt.plot(df['Date'], df['Confirmed'], label='Confirmed')
plt.plot(df['Date'], df['Deaths'], label='Deaths')
plt.plot(df['Date'], df['Recovered'], label='Recovered')

plt.title("COVID-19 Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 8: Bar Graph (Confirmed Cases)
plt.figure()
plt.bar(df['Date'], df['Confirmed'])

plt.title("Daily Confirmed Cases")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 9: Pie Chart (Latest Data)
latest = df.iloc[-1]

labels = ['Confirmed', 'Deaths', 'Recovered']
values = [latest['Confirmed'], latest['Deaths'], latest['Recovered']]

plt.figure()
plt.pie(values, labels=labels, autopct='%1.1f%%')

plt.title("Latest COVID-19 Distribution")
plt.show()

# Step 10: Active Cases Trend
plt.figure()
plt.plot(df['Date'], df['Active'])

plt.title("Active Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Active Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 11: Save Processed Data
df.to_csv("processed_covid_data.csv", index=False)

print("\n Processed data saved as 'processed_covid_data.csv'")
print("\n Project executed successfully!")

# OUTPUT:::::::

===== ORIGINAL DATA =====
         Date  Confirmed  Deaths  Recovered
0  2020-04-01       1000      50        100
1  2020-04-02       1200      60        150
2  2020-04-03       1500      75        200
3  2020-04-04       1800      90        300
4  2020-04-05       2200     120        500
5  2020-04-06       2600     150        700
6  2020-04-07       3000     200        900

===== FIRST 5 ROWS =====
         Date  Confirmed  Deaths  Recovered
0  2020-04-01       1000      50        100
1  2020-04-02       1200      60        150
2  2020-04-03       1500      75        200
3  2020-04-04       1800      90        300
4  2020-04-05       2200     120        500

===== DATA INFO =====
<class 'pandas.DataFrame'>
RangeIndex: 7 entries, 0 to 6
Data columns (total 4 columns):
 #   Column     Non-Null Count  Dtype
---  ------     --------------  -----
 0   Date       7 non-null      str
 1   Confirmed  7 non-null      int64
 2   Deaths     7 non-null      int64
 3   Recovered  7 non-null      int64
dtypes: int64(3), str(1)
memory usage: 356.0 bytes
None

===== STATISTICAL SUMMARY =====
        Confirmed      Deaths   Recovered
count     7.00000    7.000000    7.000000
mean   1900.00000  106.428571  407.142857
std     737.11148   53.906886  303.354264
min    1000.00000   50.000000  100.000000
25%    1350.00000   67.500000  175.000000
50%    1800.00000   90.000000  300.000000
75%    2400.00000  135.000000  600.000000
max    3000.00000  200.000000  900.000000

===== DATA AFTER PROCESSING =====
        Date  Confirmed  Deaths  Recovered  Active
0 2020-04-01       1000      50        100     850
2 2020-04-03       1500      75        200    1225
3 2020-04-04       1800      90        300    1410
4 2020-04-05       2200     120        500    1580
5 2020-04-06       2600     150        700    1750
6 2020-04-07       3000     200        900    1900

===== KEY INSIGHTS =====
Maximum Confirmed Cases: 3000
Maximum Deaths: 200
Maximum Recoveries: 900
Average Confirmed Cases: 1900.0

 Processed data saved as 'processed_covid_data.csv'

 Project executed successfully!


## output screenshot 








