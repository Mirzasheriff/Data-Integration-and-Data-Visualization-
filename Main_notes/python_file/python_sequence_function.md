
# Python Sequence Functions: `filter`, `map`, `reduce`, and More

This guide covers core sequence-processing functions in Python with real-world use cases, syntax, and usage recommendations.

---

## 🔁 Core Sequence Functions in Python

| Function     | Purpose                            | Type          |
|--------------|-------------------------------------|---------------|
| `filter()`   | Filters items using a function      | Functional    |
| `map()`      | Transforms items using a function   | Functional    |
| `reduce()`   | Aggregates sequence to a single value | Functional (from `functools`) |
| `zip()`      | Combines multiple sequences         | Built-in      |
| `enumerate()`| Returns index and value             | Built-in      |
| `sorted()`   | Sorts the sequence                  | Built-in      |
| `any()`      | Checks if any item is `True`        | Built-in      |
| `all()`      | Checks if all items are `True`      | Built-in      |
| `sum()`      | Returns the sum of items            | Built-in      |
| `len()`      | Returns number of items             | Built-in      |
| `max()` / `min()` | Returns maximum or minimum     | Built-in      |
| `reversed()` | Returns items in reverse order      | Built-in      |

---

## 1. `filter(function, iterable)`

### ✅ Use: Select elements based on a condition.

### 📌 Real-world Example:
```python
marks = [45, 67, 89, 32, 76]
passed = list(filter(lambda x: x >= 50, marks))
print(passed)  # [67, 89, 76]
```

---

## 2. `map(function, iterable)`

### ✅ Use: Transform elements in a sequence.

### 📌 Real-world Example:
```python
prices_usd = [10, 20, 30]
prices_inr = list(map(lambda x: x * 83.2, prices_usd))
print(prices_inr)  # [832.0, 1664.0, 2496.0]
```

---

## 3. `reduce(function, iterable)`

📦 Needs: `from functools import reduce`

### ✅ Use: Accumulate values into a single result.

### 📌 Real-world Example:
```python
from functools import reduce
cart = [200, 150, 350]
total = reduce(lambda x, y: x + y, cart)
print(total)  # 700
```

---

## 4. `zip(*iterables)`

### ✅ Use: Combine items from multiple lists.

### 📌 Real-world Example:
```python
names = ["Alice", "Bob", "Charlie"]
scores = [82, 76, 91]
result = list(zip(names, scores))
print(result)  # [('Alice', 82), ('Bob', 76), ('Charlie', 91)]
```

---

## 5. `enumerate(iterable, start=0)`

### ✅ Use: Get index and value in iteration.

### 📌 Real-world Example:
```python
questions = ["What is Python?", "What is List?"]
for i, q in enumerate(questions, start=1):
    print(f"Q{i}: {q}")
```

---

## 6. `sorted(iterable, key=..., reverse=...)`

### ✅ Use: Sort elements by key or value.

### 📌 Real-world Example:
```python
students = [("Alice", 90), ("Bob", 70), ("Charlie", 85)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
```

---

## 7. `any(iterable)` / `all(iterable)`

### ✅ Use:
- `any`: True if **at least one** item is True.
- `all`: True if **all** items are True.

### 📌 Real-world Example:
```python
access_rights = [True, False, True]
print(any(access_rights))  # True
print(all(access_rights))  # False
```

---

## 8. `sum(iterable)`, `max(iterable)`, `min(iterable)`

### ✅ Use: Quick math operations.

### 📌 Real-world Example:
```python
salaries = [35000, 47000, 29000]
print(sum(salaries))  # 111000
print(max(salaries))  # 47000
print(min(salaries))  # 29000
```

---

## 9. `reversed(sequence)`

### ✅ Use: Reverse the order of elements.

### 📌 Real-world Example:
```python
names = ["Alice", "Bob", "Charlie"]
print(list(reversed(names)))  # ['Charlie', 'Bob', 'Alice']
```

---

## 🧠 When to Use Which?

| Function     | Use Case                                               |
|--------------|--------------------------------------------------------|
| `filter()`   | When you want to remove items based on a condition     |
| `map()`      | When you want to apply the same operation to all items |
| `reduce()`   | When you want a single result from many items          |
| `zip()`      | When you want to combine multiple sequences            |
| `enumerate()`| When you need both item and index                      |
| `sorted()`   | When order matters (e.g. rankings, reports)            |
| `any()`/`all()` | Logical checks across booleans                     |
| `sum()`      | Totaling values                                        |
| `reversed()` | Reverse data for display/order                        |

---
