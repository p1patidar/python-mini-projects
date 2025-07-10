

📘 Python Fundamentals & Practice Challenges

This repository contains beginner-to-intermediate level Python code snippets and logic-building exercises that demonstrate core programming concepts in a practical, real-world context. It’s part of my journey transitioning from a PSU (HPCL) career to a high-impact software engineering role.

⸻

🧠 Topics Covered:
	•	✅ Prime number generation (two approaches)
	•	✅ List utilities: enumerate, zip, map, filter
	•	✅ Anonymous functions using lambda
	•	✅ Dictionary challenges:
	•	Inverting key-value pairs
	•	Grouping values smartly
	•	Creating fast lookup structures
	•	Value transformation
	•	✅ Real-world structuring:
	•	Student scores
	•	Stock tickers & prices

⸻

🔍 Code Highlights:

🔢 Get Prime Numbers up to 1000

def get_prime_numbers(limit):
    return [x for x in range(2, limit) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]

🧮 Combine Lists with zip()

for name, score in zip(names, scores):
    print(name, score)

🧠 Dictionary Inversion & Grouping

inverted = {v: k for k, v in employee_dept.items()}

# Smart grouping
for k, v in dict.items():
    if v not in invert_smart:
        invert_smart[v] = [k]
    else:
        invert_smart[v].append(k)

⚙️ Quick Lookups

stocks = [('RELIANCE', 2850), ('TCS', 3750)]
stock_dict = {i: v for i, v in stocks}

🎯 Combined Data Mapping

updated_dict = {st: {"Math": m, "Science": s} for st, m, s in zip(students, math_scores, science_scores)}


⸻

📁 File Info:

This code can be used as:
	•	An interview prep kit
	•	A reference for teaching beginners
	•	A base to build small real-world projects

⸻

🧔 About Me

I’m Pawan, an ex-HPCL officer transitioning into tech with a focus on backend development, AI tools, and algorithmic trading systems.
I’m sharing my journey, tools, and learnings in public.

🎥 Smart Trader’s Hub YouTube

