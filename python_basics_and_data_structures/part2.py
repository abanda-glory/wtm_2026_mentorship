# Lists
foods = ["Achu", "Eru", "poridge cocoyams", "Fufu and huckleberry", "Plantains"]

# Prints the entire list
print(*foods, sep=", ")

# Prints the first and last food respectively
print(foods[0])

print(foods[len(foods)-1])


# Adds one food
foods.append("Khati Khati")

# Remove one food 
foods.pop(4)

# Change one food to another
foods[3] = "Fried Rice"

print(*foods, sep=', ')


# Student Scores
scores = [75, 80, 65, 90, 85]

# Prints all scores
print(scores)

# Prints the highest score
print(max(scores))

# Print the lowest score
print(min(scores))

# Add new score
scores.append(95)

# Final list
print(scores)