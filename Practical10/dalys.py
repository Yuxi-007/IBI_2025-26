import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Change the working directory to the folder that contains this script.
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print("Working directory:", os.getcwd())
print("Files in directory:", os.listdir())

# Find the CSV file automatically.
csv_candidates = [
    name for name in os.listdir()
    if name.startswith("dalys-rate-from-all-causes") and name.endswith(".csv")
]
if not csv_candidates:
    raise FileNotFoundError("Could not find the DALYs CSV file in the current directory.")
csv_file = csv_candidates[0]
print("\nReading file:", csv_file)

dalys_data = pd.read_csv(csv_file)

# 1. Explore the dataframe
print("\nFirst 5 rows:")
print(dalys_data.head(5))
print("\nDataframe info:")
dalys_data.info()
print("\nSummary statistics:")
print(dalys_data.describe())
print("\nOverall maximum DALYs:", dalys_data["DALYs"].max())
print("Overall minimum DALYs:", dalys_data["DALYs"].min())
print("First year in dataset:", dalys_data["Year"].min())
print("Most recent year in dataset:", dalys_data["Year"].max())

# 2. Show the Year and DALYs columns for the first 10 rows
print("\nYear and DALYs for the first 10 rows:")
print(dalys_data.iloc[0:10, 2:4])

# Afghanistan reported the maximum DALYs across its first 10 recorded years in 1998.
afghanistan_first_10 = dalys_data.loc[dalys_data["Entity"] == "Afghanistan", ["Year", "DALYs"]].iloc[0:10]
print("\nAfghanistan: first 10 recorded years:")
print(afghanistan_first_10)
print("Afghanistan max DALYs in first 10 recorded years occurred in:",
      afghanistan_first_10.loc[afghanistan_first_10["DALYs"].idxmax(), "Year"])

# 3. Use a Boolean to show all years recorded for Zimbabwe
zimbabwe_years = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]
print("\nAll years recorded for Zimbabwe:")
print(zimbabwe_years)

# Zimbabwe has records from 1990 to 2019.
print("Zimbabwe first recorded year:", zimbabwe_years.min())
print("Zimbabwe last recorded year:", zimbabwe_years.max())

# 4. Find the countries with maximum and minimum DALYs in 2019
recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]
max_row = recent_data.loc[recent_data["DALYs"].idxmax()]
min_row = recent_data.loc[recent_data["DALYs"].idxmin()]

# In 2019, the country with the maximum DALYs was Lesotho.
# In 2019, the country with the minimum DALYs was Singapore.
print("\n2019 maximum DALYs:")
print(max_row)
print("\n2019 minimum DALYs:")
print(min_row)

# 5. Plot DALYs over time for one of those countries (Lesotho)
lesotho = dalys_data.loc[dalys_data["Entity"] == "Lesotho", ["Year", "DALYs"]]

plt.figure(figsize=(10, 5))
plt.plot(lesotho["Year"], lesotho["DALYs"], "bo-")
plt.title("DALYs over time in Lesotho")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(lesotho["Year"], rotation=90)
plt.tight_layout()
plt.savefig("lesotho_dalys_over_time.png", dpi=300)
plt.show()

# 6. My own question
# Question: How has the difference in DALYs between China and the United Kingdom changed over time?
china = dalys_data.loc[dalys_data["Entity"] == "China", ["Year", "DALYs"]].rename(columns={"DALYs": "China_DALYs"})
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["Year", "DALYs"]].rename(columns={"DALYs": "UK_DALYs"})
china_uk = pd.merge(china, uk, on="Year")
china_uk["Difference"] = china_uk["China_DALYs"] - china_uk["UK_DALYs"]

print("\nChina vs United Kingdom DALYs:")
print(china_uk)
print("\nDifference in 1990:", china_uk.loc[china_uk["Year"] == 1990, "Difference"].iloc[0])
print("Difference in 2019:", china_uk.loc[china_uk["Year"] == 2019, "Difference"].iloc[0])

plt.figure(figsize=(10, 5))
plt.plot(china_uk["Year"], china_uk["China_DALYs"], "r-o", label="China")
plt.plot(china_uk["Year"], china_uk["UK_DALYs"], "g-s", label="United Kingdom")
plt.title("DALYs over time: China vs United Kingdom")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(china_uk["Year"], rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig("china_uk_dalys_comparison.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(china_uk["Year"], china_uk["Difference"], "m-^")
plt.title("Difference in DALYs between China and the United Kingdom over time")
plt.xlabel("Year")
plt.ylabel("DALYs difference (China - UK)")
plt.xticks(china_uk["Year"], rotation=90)
plt.tight_layout()
plt.savefig("china_uk_dalys_difference.png", dpi=300)
plt.show()