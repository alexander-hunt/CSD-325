# Alexander Hunt - Nuvember 9th 2025 -  Module 4.2
# The purpose of this code is to display a plot of high and low temperatures
"""
sitka_highs_lows_menu.py

Adds a simple text menu to view Sitka 2018 daily high or low temperatures.
Loops until the user chooses Exit. Uses sys for clean exit.

DOCUMENTED CHANGES vs. original sitka_highs.py:
1) Added a text menu so the user can choose Highs, Lows, or Exit.
2) Added support to plot daily LOW temperatures in blue.
3) Wrapped file parsing into a reusable load_weather() function.
4) Added a generic plot_series() function to remove duplication.
5) Added a loop that repeats the menu after each plot until Exit.
6) Added input normalization and short aliases: h/l/e/q also work.
7) Added robust CSV parsing with try/except to skip bad/missing rows.
8) Added sys import and used sys.exit() with an explicit message.
9) Improved messages and basic error handling for missing CSV file.
"""

import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'


def load_weather(filename):
    """Return lists of dates, highs, lows parsed from the CSV file.
    Skips rows with missing or invalid data.
    """
    dates, highs, lows = [], [], []
    try:
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            header_row = next(reader, None)  # skip header
            for row in reader:
                try:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    tmax = int(row[5]) if row[5] else None
                    tmin = int(row[6]) if row[6] else None
                    if tmax is None or tmin is None:
                        continue
                    dates.append(current_date)
                    highs.append(tmax)
                    lows.append(tmin)
                except (ValueError, IndexError):
                    # Skip malformed rows
                    continue
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Place it beside this script.")
        sys.exit(1)
    return dates, highs, lows


def plot_series(dates, values, linecolor, title, ylabel):
    """Plot a single time series with standard formatting."""
    fig, ax = plt.subplots()
    ax.plot(dates, values, color=linecolor)
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel(ylabel, fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()


def main():
    dates, highs, lows = load_weather(filename)

    MENU = (
        "\nMenu:\n"
        "  [H]ighs  - Show daily high temperatures (red)\n"
        "  [L]ows   - Show daily low temperatures (blue)\n"
        "  [E]xit   - Quit the program\n"
    )
    print("Sitka Weather Viewer")
    print("Choose what to plot. Close the chart window to return to the menu.")
    while True:
        print(MENU)
        choice = input("Enter choice (H/L/E): ").strip().lower()
        if choice in ('h', 'high', 'highs'):
            plot_series(
                dates, highs, 'red',
                title="Daily high temperatures - 2018",
                ylabel="Temperature (F)")
        elif choice in ('l', 'low', 'lows'):
            plot_series(
                dates, lows, 'blue',
                title="Daily low temperatures - 2018",
                ylabel="Temperature (F)")
        elif choice in ('e', 'q', 'exit', 'quit'):
            print("Exiting. Goodbye.")
            sys.exit(0)
        else:
            print("Invalid choice. Type H, L, or E.")

if __name__ == '__main__':
    main()
