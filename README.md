# Personal Expense Tracker

This project is a **Personal Expense Tracker** built using **Python**, **Pandas**, **NumPy**, and **Matplotlib**. It helps users record daily expenses, analyze spending patterns, and visualize category-wise spending. The goal of the project is to improve financial awareness and budgeting habits by showing clear insights into where money is being spent.

---

## ✨ Project Overview

Managing personal expenses is important for tracking savings and avoiding unnecessary spending. This project provides a simple menu-based system where users can:

- Add daily expense records
- View all saved expenses
- See monthly spending totals
- Analyze category-based spending
- Generate bar chart visualizations

All expense records are stored in a `.csv` file so data is **not lost** when the program is closed.

---

## 🧠 Key Concepts Used

| Concept / Library | How It Is Used |
|------------------|----------------|
| **Pandas** | Storing, reading, grouping, and analyzing data |
| **NumPy** | Supporting numerical operations for calculations |
| **Matplotlib** | Creating bar charts for spending visualization |
| **CSV File Storage** | Saving expenses permanently without database |

---

## 📂 How the Project Works

1. When the program starts, it checks if `expenses.csv` exists.
   - If not found, a new file is created.
2. The user interacts with a menu to perform actions.
3. Data entered is stored as a new row in the CSV file.
4. Grouping and summarizing is done using Pandas:
   - By **Month** → total spending per month
   - By **Category** → total spending per category
5. A bar chart is displayed showing spending comparison between categories.

---

## 🖥️ Menu Options

| Option | Description |
|--------|-------------|
| 1 | Add a new expense entry |
| 2 | View all expenses in table form |
| 3 | Show monthly spending summary |
| 4 | Show category-wise spending & bar chart |
| 5 | Exit the program |

---

## 📊 Example Output (Category Summary)

