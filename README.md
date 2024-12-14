# Uncommon ZeroDivisionError in Conditional Statement

This repository demonstrates a simple Python function that triggers a ZeroDivisionError in an unexpected way.  The error, while common itself, is placed within a conditional statement intending to avoid division by zero.  This highlights the importance of robust error handling and carefully considering edge cases.

## The Bug

The `bug.py` file contains a function that attempts division, with a conditional statement designed to prevent ZeroDivisionError. However, due to the logic, the error still occurs under certain input conditions.

## The Solution

The `bugSolution.py` file demonstrates an improved version of the function, including robust error handling to prevent the ZeroDivisionError and gracefully handle potential issues.
