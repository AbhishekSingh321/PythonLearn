import numpy as np

# ============================================================
# 1️⃣ Creating NumPy Arrays
# ============================================================

arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4, 5])

print("Array:", arr)
print("Type:", type(arr))
print("Element-wise addition:", arr + arr2)

# ============================================================
# 2️⃣ Special Arrays
# ============================================================

arr3 = np.zeros((3, 3))
arr4 = np.ones((2, 4))
arr5 = np.full((2, 2), 7)

print("\nZeros:\n", arr3)
print("Ones:\n", arr4)
print("Full:\n", arr5)

# ============================================================
# 3️⃣ Range-based Arrays
# ============================================================

print("\nArange:", np.arange(0, 10, 2))
print("Linspace:", np.linspace(0, 1, 5))

# ============================================================
# 4️⃣ Array Properties
# ============================================================

print("\nShape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Size:", arr.size)
print("Data type:", arr.dtype)

# ============================================================
# 5️⃣ Indexing & Slicing
# ============================================================

print("\nFirst element:", arr[0])
print("Last element:", arr[-1])
print("Slice [1:4]:", arr[1:4])

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

print("\n2D Array:\n", arr2d)
print("Element [1,2]:", arr2d[1, 2])
print("First row:", arr2d[0, :])
print("Second column:", arr2d[:, 1])

# ============================================================
# 6️⃣ Boolean Indexing
# ============================================================

print("\nElements > 3:", arr[arr > 3])

# ============================================================
# 7️⃣ Vectorized Operations
# ============================================================

print("\nMultiply by 2:", arr * 2)
print("Square:", arr ** 2)
print("Add 10:", arr + 10)

# ============================================================
# 8️⃣ Aggregation Functions
# ============================================================

print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Min:", np.min(arr))
print("Max:", np.max(arr))

# ============================================================
# 9️⃣ Copy vs View
# ============================================================

view_arr = arr[1:4]
copy_arr = arr[1:4].copy()

view_arr[0] = 100

print("\nOriginal after view change:", arr)
print("Copy array:", copy_arr)

# ============================================================
# 🔟 Reshape & Flatten
# ============================================================

reshaped = np.arange(12).reshape(3, 4)
print("\nReshaped:\n", reshaped)

print("Flatten:", reshaped.flatten())

# ============================================================
# 1️⃣1️⃣ Broadcasting Example
# ============================================================

X = np.array([[1, 2, 3],
              [4, 5, 6]])

bias = np.array([0.1, 0.2, 0.3])
print("\nBroadcasting:\n", X + bias)

# ============================================================
# 1️⃣2️⃣ Simple ML-style Example
# ============================================================

data = np.array([
    [2, 50],
    [4, 65],
    [6, 80],
    [8, 90]
])

X_feat = data[:, 0]
y_label = data[:, 1]

print("\nFeatures:", X_feat)
print("Labels:", y_label)
