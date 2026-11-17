<div align="center">

# 📊 Attendance Percentage Predictor

**Predict your future attendance before it becomes a problem.**

A console-based Python application that fits a linear regression model to weekly attendance records and forecasts whether a student will stay above the 75% attendance threshold.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Linear%20Regression-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-CSV%20Support-150458?style=flat-square&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-PRD%20Compliant-success?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

</div>

---

## 📄 Project Info

| | |
|---|---|
| **Project / PS No.** | 85 |
| **Institution** | Rungta International Skills University — School of Computer Science and Engineering |
| **Program** | B.Tech — Computer Science and Engineering |
| **Application Type** | Console-Based Python Application |
| **Author** | Kavya Jain |

## ✨ Overview

Students usually only know their **current** attendance percentage — not where it's heading. This tool closes that gap: it analyzes a student's weekly attendance history, fits a trend line to it using **NumPy's `np.polyfit`**, and projects attendance forward to any future week, flagging the result as `Safe` or `Warning: below 75%`.

Built to satisfy every functional, validation, and test-case requirement defined in the project's PRD (v1.0) — all 4 official test cases pass exactly against spec.

## 🚀 Features

- 📈 **Linear regression forecasting** — fits a trend line with `np.polyfit` and reports slope & intercept
- 📂 **Two input modes** — load data from a CSV file or type it in interactively
- 🔢 **Flexible week numbering** — sequential by default (1, 2, 3...), or supply your own week numbers
- 🛡️ **Full input validation** — minimum 2 records, attendance within 0–100, positive & unique week numbers, future week must be ahead of the latest recorded week
- 🎯 **Smart capping** — predictions are clamped to the realistic 0–100% range and labeled `(capped)` when triggered
- 🧯 **Graceful error handling** — invalid numbers, bad file paths, and malformed CSVs are caught with a plain-English message, never a crash
- ✅ **Instant verdict** — a clear `Safe` / `Warning: below 75%` status at a glance

## 📸 Example Run

```
========================================
ATTENDANCE PERCENTAGE PREDICTOR
========================================
Load data from CSV file or enter manually? (csv/manual): manual
How many weeks of attendance data do you have? 5
Enter custom week numbers instead of 1, 2, 3...? (y/n): n
Enter attendance % for week 1: 90
Enter attendance % for week 2: 88
Enter attendance % for week 3: 86
Enter attendance % for week 4: 84
Enter attendance % for week 5: 82
Enter future week to predict: 10
----------- PREDICTION RESULT -----------
Slope: -2.00
Intercept: 92.00
Predicted: 72.00%
Warning: below 75%
-----------------------------------------
```

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/attendance-percentage-predictor.git
cd attendance-percentage-predictor

# Install the required packages
pip install numpy pandas
```

## ▶️ Usage

```bash
python attendance_predictor.py
```

You'll be prompted to choose how to load your data:

### Option 1 — Manual entry
Type the number of weeks you have data for, optionally supply your own week numbers, then enter each week's attendance percentage.

### Option 2 — CSV file
Point the script at a CSV file with `Week` and `Attendance` columns. The `Week` column is optional — if omitted, sequential week numbers are generated automatically.

```csv
Week,Attendance
1,90
2,88
3,86
4,84
5,82
```

In both modes, you'll be asked for a future week to predict (it must come after your last recorded week) — and the script handles the rest.

## 🧮 How It Works

1. Collects weekly attendance data (minimum 2 weeks, each validated between 0–100%).
2. Fits a straight line `attendance = slope × week + intercept` using `np.polyfit(weeks, attendance, 1)`.
3. Plugs the requested future week into the fitted line to get a raw prediction.
4. Clamps the result to `[0, 100]`, flagging it as `(capped)` when the raw value falls outside that range.
5. Declares `Safe` if the predicted attendance is **≥ 75%**, otherwise `Warning: below 75%`.

## 📋 Requirements

| Package | Purpose |
|---|---|
| `numpy` | Linear regression via `np.polyfit` |
| `pandas` | Reading attendance data from CSV |

Python 3.x is required.

## 📁 Project Structure

```
attendance-percentage-predictor/
├── attendance_predictor.py   # Main script
├── sample_attendance.csv     # Example CSV input (optional)
└── README.md                 # You are here
```

## 🧪 Test Coverage

| Test Case | Scenario | Result |
|---|---|---|
| TC1 | Normal declining trend | ✅ Pass |
| TC2 | Minimum (2-week) boundary input | ✅ Pass |
| TC3 | Invalid input (insufficient data, out-of-range attendance) | ✅ Pass |
| TC4 | Rising trend with upper-bound capping | ✅ Pass |

All four official test cases from the project PRD pass with exact expected output, alongside additional validation for duplicate/invalid week numbers, non-numeric input, and missing CSV files.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
Made with 🐍 Python and a healthy fear of falling below 75% attendance.
</div>
