#!/usr/bin/env python3
"""
A simple script to print user details based on command-line arguments.
Usage: python3 test1script.py <name> <lastname> <age> <visible>
"""

import sys

# Check if less than 4 arguments are passed
if len(sys.argv) < 5:
    print(f"Usage: {sys.argv[0]} <name> <lastname> <age> <visible>")
    sys.exit(1)

name = sys.argv[1]
lastname = sys.argv[2]
age = sys.argv[3]
visible = sys.argv[4].lower()  # Convert to lowercase for case-insensitivity

if visible == "true":
    print(f"I am {name} {lastname}, and I am {age} years old.")
else:
    print("Please pass the visible true!!!")

# Ensure the file ends with a blank line (fix for C0304)
