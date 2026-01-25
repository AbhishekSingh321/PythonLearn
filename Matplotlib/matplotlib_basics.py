import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# 1️⃣ Basic Line Plot
# ============================================================

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 25, 30, 40])

plt.figure()
plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# ============================================================
# 2️⃣ Line Plot with Markers
# ============================================================

plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Plot with Markers")
plt.show()

# ============================================================
# 3️⃣ Multiple Lines in One Plot
# ============================================================

y2 = y * 0.8

plt.figure()
plt.plot(x, y, label="Sales 2024")
plt.plot(x, y2, label="Sales 2023")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.legend()
plt.title("Multiple Line Plot")
plt.show()

# ============================================================
# 4️⃣ Bar Chart
# ============================================================

categories = ["A", "B", "C", "D"]
values = [20, 35, 30, 15]

plt.figure()
plt.bar(categories, values)
plt.title("Bar Chart Example")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()

# ============================================================
# 5️⃣ Horizontal Bar Chart
# ============================================================

plt.figure()
plt.barh(categories, values)
plt.title("Horizontal Bar Chart")
plt.show()

# ============================================================
# 6️⃣ Histogram (VERY IMPORTANT)
# ============================================================

data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=30)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# ============================================================
# 7️⃣ Scatter Plot (ML CORE)
# ============================================================

x = np.random.rand(50)
y = np.random.rand(50)

plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("Feature X")
plt.ylabel("Feature Y")
plt.show()

# ============================================================
# 8️⃣ Scatter Plot with Size & Alpha
# ============================================================

sizes = np.random.rand(50) * 500

plt.figure()
plt.scatter(x, y, s=sizes, alpha=0.6)
plt.title("Enhanced Scatter Plot")
plt.show()

# ============================================================
# 9️⃣ Subplots (DASHBOARD STYLE)
# ============================================================

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [3, 2, 5])
plt.title("Plot 1")

plt.subplot(1, 2, 2)
plt.bar([1, 2, 3], [4, 1, 6])
plt.title("Plot 2")

plt.tight_layout()
plt.show()

# ============================================================
# 🔟 Customizing Plots
# ============================================================

plt.figure()
plt.plot(x, y)
plt.grid(True)
plt.title("Customized Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# ============================================================
# 1️⃣1️⃣ Saving a Figure (PRODUCTION USE)
# ============================================================

plt.figure()
plt.plot([1, 2, 3], [10, 20, 30])
plt.title("Saved Plot")
plt.savefig("line_plot.png")
plt.close()

# ============================================================
# 1️⃣2️⃣ ML-Style Visualization Example
# ============================================================

# Feature vs Target
X = np.array([2, 4, 6, 8])
y = np.array([50, 65, 80, 90])

plt.figure()
plt.scatter(X, y)
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Feature vs Target")
plt.show()
