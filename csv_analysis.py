import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
df = pd.read_csv("data.csv")

# Display first few rows
print("First 5 Rows of Data:")
print(df.head())

# Basic Summary
print("\nData Summary:")
print(df.describe())

# Choose a numeric column for average calculation (modify as per your data)
column_to_average = df.select_dtypes(include='number').columns[0]
average = df[column_to_average].mean()
print(f"\nAverage of '{column_to_average}': {average:.2f}")

# Bar Plot
df[column_to_average].head(10).plot(kind='bar', title=f"Top 10 '{column_to_average}' Values")
plt.xlabel("Index")
plt.ylabel(column_to_average)
plt.tight_layout()
plt.show()

# Scatter Plot (if 2 numeric columns exist)
numeric_cols = df.select_dtypes(include='number').columns
if len(numeric_cols) >= 2:
    plt.scatter(df[numeric_cols[0]], df[numeric_cols[1]])
    plt.title(f"{numeric_cols[0]} vs {numeric_cols[1]}")
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
    plt.tight_layout()
    plt.show()

# Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
