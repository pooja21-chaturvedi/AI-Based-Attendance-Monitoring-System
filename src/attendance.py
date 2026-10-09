"""Attendance recording logic (CSV-based prototype).

Rule used: one attendance record per student per date.
"""
from datetime import datetime
from pathlib import Path

import pandas as pd

COLUMNS = ["student_id", "student_name", "date", "time", "status"]

# Always resolves to <project root>/data/attendance.csv, no matter where you run from.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FILE = PROJECT_ROOT / "data" / "attendance.csv"


def init_file(file=DEFAULT_FILE):
    """Create the CSV with headers if it doesn't exist."""
    file = Path(file)
    file.parent.mkdir(parents=True, exist_ok=True)
    if not file.exists():
        pd.DataFrame(columns=COLUMNS).to_csv(file, index=False)


def mark_attendance(student_id, student_name, file=DEFAULT_FILE):
    """Mark a student present once per date. Returns a message string."""
    student_id = str(student_id).strip()
    student_name = str(student_name).strip()
    if not student_id or not student_name:
        raise ValueError("student_id and student_name cannot be empty.")

    init_file(file)
    df = pd.read_csv(file, dtype=str)
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")

    already = ((df["student_id"] == student_id) & (df["date"] == today)).any()
    if already:
        return "Attendance already marked for today."

    new_row = pd.DataFrame([{
        "student_id": student_id,
        "student_name": student_name,
        "date": today,
        "time": now.strftime("%H:%M:%S"),
        "status": "Present",
    }])
    new_row.to_csv(file, mode="a", header=False, index=False)
    return "Attendance marked successfully."


def get_report(date=None, student_id=None, file=DEFAULT_FILE):
    """Return attendance records, optionally filtered by date and/or student."""
    init_file(file)
    df = pd.read_csv(file, dtype=str)
    if date:
        df = df[df["date"] == date]
    if student_id:
        df = df[df["student_id"] == str(student_id)]
    return df.reset_index(drop=True)


def export_report(output_path, date=None, student_id=None, file=DEFAULT_FILE):
    """Save a filtered report to a new CSV file and return its path."""
    get_report(date, student_id, file).to_csv(output_path, index=False)
    return output_path
