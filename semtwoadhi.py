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