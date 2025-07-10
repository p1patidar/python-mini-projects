


# 🐍 Python Fundamentals & Practice Challenges

This project contains a collection of Python exercises and utilities built as part of my foundational learning phase. It demonstrates important Python concepts through real-world-style challenges and logic-building tasks.

---

## 🧠 Topics Covered

- ✅ Prime number generation (two approaches)
- ✅ Working with `enumerate()`, `zip()`, `map()`, `filter()`
- ✅ Anonymous functions using `lambda`
- ✅ Dictionary challenges:
  - Inverting key-value pairs
  - Grouping values by keys
  - Creating quick lookups
  - Transforming values
- ✅ Real-world data structuring:
  - Student test scores
  - Stock tickers and pricing

---

## 🔍 Code Highlights

### 🔢 Prime Numbers Generator
```python
def get_prime_numbers(limit):
    return [x for x in range(2, limit) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]

🔁 Combine Lists using zip()

names = ['pawan', 'rahul', 'deepak']
scores = [85, 90, 78]
for name, score in zip(names, scores):
    print(name, score)

🔁 Use of map() and filter()

squared = list(map(lambda x: x**2, [1, 2, 3]))
evens = list(filter(lambda x: x % 2 == 0, [10, 15, 20]))

🧠 Inverting a Dictionary

employee_dept = {'Pawan': 'Sales', 'Ravi': 'Marketing'}
inverted = {v: k for k, v in employee_dept.items()}

🧠 Smart Grouping of Dictionary Values

input_dict = {'Pawan': 'Sales', 'Ankit': 'Sales', 'Sneha': 'HR'}
grouped = {}
for k, v in input_dict.items():
    grouped.setdefault(v, []).append(k)

📈 Creating Quick Lookup Dictionary

stocks = [('RELIANCE', 2850), ('TCS', 3750)]
stock_dict = {name: price for name, price in stocks}
print(stock_dict['TCS'])  # Output: 3750

📊 Combined Student Score Mapping

students = ['Pawan', 'Ravi']
math = [88, 77]
science = [92, 81]
combined = {s: {'Math': m, 'Science': sc} for s, m, sc in zip(students, math, science)}


⸻

📁 How to Use
	1.	Clone this repo or copy the script
	2.	Run individual functions from a Python shell or notebook
	3.	Explore & modify challenges to deepen understanding

⸻

👨‍💻 About Me

Hi, I’m Pawan — a former HPCL officer now transitioning into tech, focusing on:
	•	Backend Development (Python, FastAPI)
	•	AI Tools (OpenAI, LangChain)
	•	Algo & Quant Trading (TA-Lib, Backtesting, APIs)

📺 YouTube: Smart Trader’s Hub

⸻

📌 How to Run

python script_name.py

Or explore interactively in Jupyter.

⸻

⭐ Star This Repo If…

You’re a self-learner, career switcher, or preparing for Python interviews and want real, readable, practical examples.

---

Let me know if you want this **converted into a README file** right now (`README.md`) or want help setting it up in your project folder.
