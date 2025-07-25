
# 🧵 Python Tutorial: Pattern Matching with Regular Expressions

## 🔍 Introduction

**Regular Expressions (regex)** are used to search, match, and manipulate text using specific patterns. They are especially useful for:

- Validating user input (e.g., email, phone number)
- Searching in logs
- Extracting text from documents

To use regex in Python, you must first import the `re` module:

```python
import re
```

---

## 📌 1. Regular Expression Matching

### ✅ Real-World Use Case:
Validate if a user has entered a valid **phone number** (e.g., `9876543210`)

### 💡 Example:
```python
import re

def is_valid_phone(number):
    pattern = r'^\d{10}$'
    return re.match(pattern, number) is not None

print(is_valid_phone("9876543210"))  # True
print(is_valid_phone("12345"))       # False
```

### 📘 Explanation:
- `^` → Start of the string
- `\d{10}` → Exactly 10 digits
- `$` → End of the string

---

## 📌 2. Finding Patterns of Text with Regular Expressions

### ✅ Real-World Use Case:
Find all **email addresses** in a block of text.

### 💡 Example:
```python
text = "Contact us at support@site.com or sales@company.org"
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(emails)  # ['support@site.com', 'sales@company.org']
```

### 📘 Explanation:
- `\b` → Word boundary
- `[\w.-]+` → Word characters, dots, or hyphens
- `@` → Literal @ symbol
- `\.\w+` → A dot followed by one or more word characters

---

## 📌 3. Grouping with Parentheses

### ✅ Real-World Use Case:
Extract the **day**, **month**, and **year** from a date.

### 💡 Example:
```python
date = "Order placed on 23-04-2025"
match = re.search(r'(\d{2})-(\d{2})-(\d{4})', date)
if match:
    day, month, year = match.groups()
    print(f"Day: {day}, Month: {month}, Year: {year}")
```

### 📘 Explanation:
- `()` → Capturing groups
- `\d{2}` → Two digits (day, month)
- `\d{4}` → Four digits (year)

---

## 📌 4. Matching Multiple Groups with the Pipe (`|`)

### ✅ Real-World Use Case:
Detect whether the user said "yes" or "no".

### 💡 Example:
```python
def detect_choice(response):
    match = re.search(r'yes|no', response.lower())
    return match.group() if match else "No match"

print(detect_choice("Yes, I agree."))  # yes
print(detect_choice("No problem."))    # no
```

### 📘 Explanation:
- `|` → Acts as OR operator

---

## 📌 5. Matching Zero or More with the Star (`*`)

### ✅ Real-World Use Case:
Extract repeated **laughs** (e.g., "ha", "haha", "hahaha") from messages.

### 💡 Example:
```python
text = "That was so funny hahaha!"
match = re.search(r'(ha)*', text)
print(match.group())  # hahaha
```

### 📘 Explanation:
- `(ha)*` → Match zero or more repetitions of "ha"

---

## 🧠 Summary Table

| Feature                         | Regex Pattern               | Example Use Case                    |
|----------------------------------|-----------------------------|-------------------------------------|
| **Matching**                     | `^\d{10}$`                 | Phone number                        |
| **Finding patterns**            | `[\w.-]+@[\w.-]+\.\w+`  | Email extraction                    |
| **Grouping**                    | `(\d{2})-(\d{2})-(\d{4})`| Date breakdown                      |
| **Pipe `|` for multiple groups**| `yes|no`                    | Detect choices                      |
| **Star `*` for zero or more**   | `(ha)*`                     | Extract repeated laughs             |
