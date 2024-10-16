# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import os
import csv

from PIL.ImImagePlugin import split
from mypyc.namegen import candidate_suffixes
from numpy.ma.extras import row_stack
from spyder.utils.external.lockfile import unique
from sympy.codegen.cnodes import union

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = {}
candidateinfolist = []
highestvotes = 0

# Winning Candidate and Winning Count Tracker

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        # print(". ", end="") excluded this because i thought it was unnecessary and annoying lol

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidates:
            candidates[f'{candidate}'] = 0

        # Add a vote to the candidate's count
        candidates[f'{candidate}'] += 1

# determining results and formatting
for c in candidates:
    candidateinfo = f"{c}: {round(candidates[c]/total_votes*100,3)}% ({candidates[c]})"
    candidateinfolist.append(candidateinfo)

    if candidates[c] > highestvotes:
        highestvotes = candidates[c]
        currentwinner = c

candidateresults = "\n".join(row for row in candidateinfolist)

results = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidateresults}
-------------------------
Winner: {currentwinner}
-------------------------
"""

print(results)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write(results)

