count = 1
total = 0

# BUG: The while statement was missing a colon, so I added : at the end.
# BUG: The condition stopped the loop before 5 was added, so I changed < 5 to <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: I was trying to join text and an integer with +, so I used a comma instead.
print("Sum of 1 to 5 is:", total)
