# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import os
import csv

from dask.array import average
from openpyxl.styles.builtins import output, total

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 1
total_net = 0

# Add more variables to track other necessary financial data
changes = []
gincrease = 0
gdecrease = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    row1 = next(reader)

    # Track the total and net change
    total_net += int(row1[1])
    previncome = int(row1[1])

    # Process each row of data
    for row in reader:
        income = int(row[1])

        # Track the total
        total_months += 1
        total_net += income

        # Track the net change
        change = income - previncome
        changes.append(change)
        previncome = income

        # Calculate the greatest increase in profits (month and amount)
        if change > gincrease:
            gincrease = change
            gincreasem = row[0]
        elif change < gdecrease:
            gdecrease = change
            gdecreasem = row[0]

        # Calculate the greatest decrease in losses (month and amount)


# Calculate the average net change across the months
avgchange = sum(changes)/len(changes)

# Generate the output summary
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${round(avgchange, 2)}
Greatest Increase in Profits: {gincreasem} (${gincrease})
Greatest Decrease in Profits: {gdecreasem} (${gdecrease})"""

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
