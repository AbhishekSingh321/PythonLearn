import pandas as pd
import numpy as np

# ============================================================
# 1️⃣ Creating Series
# ============================================================

s = pd.Series([10, 20, 30, 40])
print("Series:\n", s)

# ============================================================
# 2️⃣ Creating DataFrame
# ============================================================

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Salary": [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# ============================================================
# 3️⃣ Basic Data Inspection
# ============================================================

print("\nHead:\n", df.head())
print("\nTail:\n", df.tail())
print("\nShape:", df.shape)
print("\nInfo:")
df.info()
print("\nDescribe:\n", df.describe())

# ============================================================
# 4️⃣ Column Access
# ============================================================

print("\nSingle Column:\n", df["Age"])
print("\nMultiple Columns:\n", df[["Name", "Salary"]])

# ============================================================
# 5️⃣ Row Access (loc & iloc)
# ============================================================

print("\nRow using iloc:\n", df.iloc[1])
print("\nRow using loc:\n", df.loc[2])

# ============================================================
# 6️⃣ Filtering Rows (VERY IMPORTANT)
# ============================================================

high_salary = df[df["Salary"] > 60000]
print("\nFiltered Rows:\n", high_salary)

# ============================================================
# 7️⃣ Adding New Columns
# ============================================================

df["Tax"] = df["Salary"] * 0.1
print("\nAfter Adding Column:\n", df)

# ============================================================
# 8️⃣ Updating Values
# ============================================================

df.loc[df["Name"] == "Alice", "Salary"] = 55000
print("\nAfter Update:\n", df)

# ============================================================
# 9️⃣ Handling Missing Values
# ============================================================

df_missing = df.copy()
df_missing.loc[2, "Age"] = np.nan

print("\nWith Missing Value:\n", df_missing)

print("\nIs Null:\n", df_missing.isnull())
print("\nFill NaN:\n", df_missing.fillna(df_missing.mean(numeric_only=True)))

# ============================================================
# 🔟 Sorting Data
# ============================================================

print("\nSort by Salary:\n", df.sort_values("Salary", ascending=False))

# ============================================================
# 1️⃣1️⃣ GroupBy (INDUSTRY CORE)
# ============================================================

dept_data = {
    "Dept": ["IT", "IT", "HR", "HR"],
    "Salary": [70000, 80000, 50000, 60000]
}

dept_df = pd.DataFrame(dept_data)

print("\nGroupBy Mean Salary:\n", dept_df.groupby("Dept")["Salary"].mean())

# ============================================================
# 1️⃣2️⃣ Apply Function
# ============================================================

df["Salary_Level"] = df["Salary"].apply(lambda x: "High" if x > 65000 else "Low")
print("\nAfter Apply:\n", df)

# ============================================================
# 1️⃣3️⃣ Reading & Writing Files
# ============================================================

# df.to_csv("employees.csv", index=False)
# loaded_df = pd.read_csv("employees.csv")

# ============================================================
# 1️⃣4️⃣ Drop Columns & Rows
# ============================================================

print("\nDrop Column:\n", df.drop(columns=["Tax"]))
print("\nDrop Row:\n", df.drop(index=0))

# ============================================================
# 1️⃣5️⃣ Pandas → ML Style Separation
# ============================================================

X = df[["Age", "Salary"]]
y = df["Salary_Level"]

print("\nFeatures:\n", X)
print("\nTarget:\n", y)
