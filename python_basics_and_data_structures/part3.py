# Tuples
days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

# Print entire tuple
print(days_of_the_week)

# Print the first day
print(days_of_the_week[0])

# Print the last day
print(days_of_the_week[len(days_of_the_week) - 1])

# Attempting to change a value
# days_of_the_week[0] = "Sunday" - I got a TypeError: 'tuple' object does not support item assignment
# A list is mutable (Items of a list can be changed once declared) while a tuple is immutable