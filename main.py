"""
Attendance Percentage Predictor
--------------------------------
Implements the PRD (v1.0) for the Attendance Percentage Predictor,
Problem Statement #85 — Rungta International Skills University.

Uses weekly attendance percentages to fit a straight line (via NumPy's
np.polyfit) and predicts the attendance percentage for a future week.

Run from the console:
    python attendance_predictor.py
"""

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_from_csv(path):
    """
    Load weekly attendance data from a CSV file (FR-02).

    Expects an 'Attendance' column. A 'Week' column is optional — if it is
    missing, sequential week numbers are generated automatically (FR-05).
    """
    try:
        df = pd.read_csv(path)
    except Exception:
        raise ValueError(
            "The CSV file could not be found or could not be read. "
            "Please check the file path and try again."
        )

    columns_lower = {col.lower().strip(): col for col in df.columns}
    week_col = columns_lower.get("week") or columns_lower.get("weeks")
    attendance_col = (
        columns_lower.get("attendance")
        or columns_lower.get("attendance%")
        or columns_lower.get("attendance percentage")
    )

    if attendance_col is None:
        raise ValueError("CSV must contain an 'Attendance' column.")

    attendance = df[attendance_col].tolist()

    if week_col is not None:
        weeks = df[week_col].tolist()
    else:
        weeks = list(range(1, len(attendance) + 1))

    return weeks, attendance


def load_manual():
    """Collect weekly attendance data interactively from the console (FR-01)."""
    n = _read_int("How many weeks of attendance data do you have? ")

    use_custom_weeks = input(
        "Enter custom week numbers instead of 1, 2, 3...? (y/n): "
    ).strip().lower() == "y"

    weeks = []
    attendance = []
    for i in range(1, n + 1):
        if use_custom_weeks:
            week_number = _read_int(f"Enter the week number for record {i}: ")
        else:
            week_number = i

        value = _read_float(f"Enter attendance % for week {week_number}: ")

        weeks.append(week_number)
        attendance.append(value)

    return weeks, attendance


def _read_int(prompt):
    """Keep asking until the user types a valid whole number (VR-04/VR-06)."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


def _read_float(prompt):
    """Keep asking until the user types a valid number (VR-04)."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number for attendance.")



def validate_data(weeks, attendance):
    """
    Validate weekly attendance data (FR-03, FR-04, VR-01, VR-02, VR-03, VR-07).
    Raises ValueError with the exact PRD-specified message when invalid.
    """
    if len(weeks) < 2 or len(attendance) < 2:
        raise ValueError("At least 2 weeks of data are required.")

    for value in attendance:
        if value < 0 or value > 100:
            raise ValueError("Attendance must be between 0 and 100.")

    whole_weeks = []
    for w in weeks:
        if float(w) <= 0 or float(w) != int(w):
            raise ValueError("Week numbers must be positive whole numbers.")
        whole_weeks.append(int(w))

    if len(set(whole_weeks)) != len(whole_weeks):
        raise ValueError("Week numbers must be unique. Please check your data.")


def validate_future_week(future_week, weeks):
    """Future week must be after the latest recorded week (VR-06)."""
    if future_week <= max(weeks):
        raise ValueError(
            "Please enter a future week number greater than your latest recorded week."
        )




def compute_prediction(weeks, attendance, future_week):
    """
    Fit a straight line to (weeks, attendance) with np.polyfit (FR-06) and
    predict the attendance percentage for future_week (FR-09, FR-10). The
    prediction is capped to the range [0, 100] (FR-11).
    """
    weeks_arr = np.array(weeks, dtype=float)
    attendance_arr = np.array(attendance, dtype=float)

    slope, intercept = np.polyfit(weeks_arr, attendance_arr, 1)

    predicted_raw = slope * future_week + intercept
    predicted_capped = min(100, max(0, predicted_raw))
    was_capped = predicted_capped != predicted_raw

    return slope, intercept, predicted_capped, was_capped



def main():
    print("=" * 40)
    print("ATTENDANCE PERCENTAGE PREDICTOR")
    print("=" * 40)

    choice = input("Load data from CSV file or enter manually? (csv/manual): ").strip().lower()

    try:
        if choice == "csv":
            path = input("Enter CSV file path: ").strip()
            weeks, attendance = load_from_csv(path)
        else:
            weeks, attendance = load_manual()

        validate_data(weeks, attendance)

        future_week = _read_int("Enter future week to predict: ")
        validate_future_week(future_week, weeks)

        slope, intercept, predicted, was_capped = compute_prediction(
            weeks, attendance, future_week
        )
        status = "Safe" if predicted >= 75 else "Warning: below 75%" 

        print("----------- PREDICTION RESULT -----------")
        print(f"Slope: {slope:.2f}")          
        print(f"Intercept: {intercept:.2f}")  
        suffix = " (capped)" if was_capped else ""
        print(f"Predicted: {predicted:.2f}%{suffix}")  
        print(status)
        print("-" * 41)

    except ValueError as e:
        print(str(e)) 
    except Exception as e:
        print(f"Error: {e}")  


if __name__ == "__main__":
    main()
