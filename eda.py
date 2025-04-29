import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\Python\exoplanet\exo_dataset\exoTest\exoTest.csv")

print("First five rows")
print(df.head())

print("\nData info :")
print(df.info())

print("\nSummary :")
print(df.describe())

sns.countplot(x = 'LABEL', data=df)
plt.title("Distribution of labels")
plt.xlabel("Label (2 = Exoplanet candidate)")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(12,6))
for i, col in enumerate(df.columns[1:6]) :
    plt.subplot(2, 3, i + 1)
    sns.histplot(df[col], bins=50, kde=True)
    plt.title(f"Distribution of {col}")
    
plt.tight_layout()
plt.show()

corr_matrix = df.iloc[:, 1:].corr()

plt.figure(figsize = (12, 8))
sns.heatmap(corr_matrix, cmap = "coolwarm", annot = False)
plt.title("Correlation heatmap of Flux Values")
plt.show()

flux_values = df.iloc[0, 1:]

plt.figure(figsize = (10, 5))
plt.plot(flux_values)
plt.title("Flux time series for row 0")
plt.xlabel("Time steps")
plt.ylabel("Flux Values")
plt.show()