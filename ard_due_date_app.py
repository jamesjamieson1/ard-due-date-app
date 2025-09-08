import streamlit as st
from datetime import datetime, timedelta

# --- Configuration ---
SCHOOL_START = datetime(2025, 8, 11).date()
SCHOOL_END = datetime(2026, 5, 29).date()

HOLIDAYS = {
    datetime(2025, 9, 1).date(),
    datetime(2025, 10, 10).date(),
    datetime(2025, 10, 13).date(),
    datetime(2025, 11, 4).date(),
    datetime(2025, 11, 24).date(),
    datetime(2025, 11, 25).date(),
    datetime(2025, 11, 26).date(),
    datetime(2025, 11, 27).date(),
    datetime(2025, 11, 28).date(),
    datetime(2025, 12, 22).date(),
    datetime(2025, 12, 23).date(),
    datetime(2025, 12, 24).date(),
    datetime(2025, 12, 25).date(),
    datetime(2025, 12, 26).date(),
    datetime(2025, 12, 29).date(),
    datetime(2025, 12, 30).date(),
    datetime(2025, 12, 31).date(),
    datetime(2026, 1, 1).date(),
    datetime(2026, 1, 2).date(),
    datetime(2026, 1, 5).date(),
    datetime(2026, 1, 19).date(),
    datetime(2026, 2, 16).date(),
    datetime(2026, 3, 9).date(),
    datetime(2026, 3, 10).date(),
    datetime(2026, 3, 11).date(),
    datetime(2026, 3, 12).date(),
    datetime(2026, 3, 13).date(),
    datetime(2026, 4, 3).date(),
    datetime(2026, 4, 24).date(),
    datetime(2026, 5, 25).date(),
}

# --- Helper Functions ---
def is_school_day(d):
    return d.weekday() < 5 and d not in HOLIDAYS

def next_school_day(d):
    while not is_school_day(d):
        d += timedelta(days=1)
    return d

def add_school_days(start_date, days):
    current = start_date
    count = 0
    while count < days:
        current += timedelta(days=1)
        if is_school_day(current):
            count += 1
    return current

def subtract_school_days(start_date, days):
    current = start_date
    count = 0
    while count < days:
        current -= timedelta(days=1)
        if is_school_day(current):
            count += 1
    return current

# --- Streamlit App ---
st.title("ARD Due Date Calculator")
st.write(
    "Select the date the consent was signed/received. "
)

# Date picker
consent_date = st.date_input(
    "Consent signed/received date:",
    min_value=SCHOOL_START,
    max_value=SCHOOL_END
)

if consent_date:
    # Adjust if weekend/holiday
    adjusted_date = next_school_day(consent_date)
    due_date = add_school_days(adjusted_date, 55)
    first_attempt = subtract_school_days(due_date, 10)

    st.success(f"The ARD should be held by: {due_date.strftime('%m/%d/%Y')}")
    st.info(f"To allow for 3 attempts, the first attempt should be scheduled by: {first_attempt.strftime('%m/%d/%Y')}")

    if adjusted_date != consent_date:
        st.warning(
            f"The entered date falls on a weekend/holiday, "
            f"so calculations start from next school day: {adjusted_date.strftime('%m/%d/%Y')}"
        )