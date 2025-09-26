# Stock Optimizer — OC P7 (Algorithms in Python)

> **Educational project (OpenClassrooms)** — solve a classic **0/1 knapsack** problem: **select the most profitable set of stocks under a budget**. Includes a naive **brute‑force** baseline and an **optimized** dynamic‑programming solver.

---

## ✨ Features

- 📊 Read CSV datasets of candidate stocks
- 💰 Respect a fixed **budget** constraint
- 🧮 Two solvers:
  - **Brute force** (exhaustive search, exponential)
  - **Optimized** **dynamic programming** (pseudo‑polynomial in budget)
- 📈 Returns **selected stocks**, **total cost**, **total profit** and runtime

> This repo is for learning/portfolio demonstration.

---

## 🧱 Tech stack

- **Python 3.10+**
- Standard library + packages in `requirements.txt` (minimal)

---

## 📦 Repository layout

```
.
├─ data/                         # Input CSVs
├─ old/                          # (optional) earlier attempts
├─ bruteforce.py                 # naive exhaustive solver
├─ optimized.py                  # dynamic‑programming solver
├─ requirements.txt
└─ readme.md                     # you are here
```

---

## 🗃️ Dataset format

Expected CSV (example):

```csv
name,price,profit_percent
Action‑1,20,5
Action‑2,30,10
```

- `price` is the **cost** (same currency for all rows)
- `profit_percent` is the gain percentage (e.g., `10` → 10%)

> If your file uses another header/delimiter, adjust the reader accordingly (see top of the scripts).

---

## 🚀 Quickstart

```bash
# 1) Create & activate a virtual env (recommended)
python3 -m venv .venv && source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run a solver
python optimized.py          # or: python bruteforce.py
```

By default the scripts use the bundled dataset and a default **budget** (e.g., 500). If your version accepts CLI parameters, you can typically run:

```bash
python optimized.py --file data/dataset1.csv --budget 500
```

> If no CLI is implemented in your copy, set the `BUDGET` and input file path at the top of the script.

---

## 🧠 Algorithm notes

### Brute force
- **Idea**: try all subsets (2^n)
- **Complexity**: O(2^n) — only for very small `n`

### Dynamic programming (0/1 knapsack)
- **Idea**: build a DP table `dp[i][b]` = best profit using first `i` items within budget `b`
- **Complexity**: O(n × B) time, O(n × B) or O(B) memory where `B` is the budget (integer)

The DP approach scales much better for typical training datasets.

---

## 🧪 (Optional) tests & benchmarking

```bash
# basic unit tests if present
pytest -q

# quick timing (Linux/macOS)
/usr/bin/time -lp python optimized.py
```

---

## 🔧 Troubleshooting

- CSV parse errors → check delimiter and headers
- Empty result → budget too small or all items too costly
- Slow run with brute force → prefer `optimized.py`

---

## 🗺️ Improvements

- Add a **CLI** with `argparse` (file, budget)
- Export results to CSV/JSON
- Add a greedy heuristic for comparison
- Plot Pareto curves (risk/return) for extended datasets

---

## 👤 Author

**Mathieu Vieillefont**  
LinkedIn: https://www.linkedin.com/in/mathieu-vieillefont/

---

## 📄 License

Released for **educational purposes** (OpenClassrooms). Add a license (e.g., MIT) if you plan to reuse/redistribute.

