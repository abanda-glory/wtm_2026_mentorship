# Student Information Manager
name = "Abanda Glory"
age = 23
height = 1.60
is_currently_enrolled = True

# 1. List
skills = ['Python', 'Java', 'CSS', 'HTML', 'JavaScript']

# Prints the first item
print(skills[0])

# Add a new item
skills.append('React')

# Remove an item
skills.remove('Java')

# Updated list
print(skills)

# 2. Tuple
numbers = (1, 5, 10)

# Print the second number
print(numbers[1])

# 3. Set
hobbies = {'Singing', 'Cooking', 'Coding', 'Reading', 'Coding'}

# Print set
print(hobbies)

# The set automatically takes care of the duplicate values by deleting one

# Add a new hobby
hobbies.add('Swimming')

print(hobbies)

# 4. Dictionary
student_info = {
    'name':'John Doe',
    'age':25,
    'height':1.25,
    'is_enrolled':True,
    'skills':['Python', 'SQL', 'Excel'],
    'fav_numbers':(1, 5, 10),
    'hobbies':{'Reading', 'Gaming', 'Football'},
}

# Print the student's name
print(student_info['name'])

# Print skills
print(student_info['skills'])

# Add new key "country"
student_info['country'] = 'Cameroon'

# Update student's age
student_info['age'] = 27

# Print complete dictionary
print(student_info)

