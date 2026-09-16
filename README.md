# PLP Python Week 3 Assignment

## Files

- `grade_reporter.py` - Calculates grades, pass/fail counts, and the average score.
- `bug_hunt.py` - Finds and fixes three bugs in a Python program that calculates the sum from 1 to 5.

## Part B Bug Hunt

The hardest bug to find was the loop condition because the program did not show an error message. I knew something was wrong because the program produced the wrong answer instead of the expected 15, so I checked the loop condition and realized that `count < 5` stopped the loop before 5 was added.
