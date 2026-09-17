stud_info = {'name':'Abanda Glory', 
             'age':23, 
             'course':'Backend Development With Python', 
             'level':100, 
             'skills':['Python', 'PHP', 'Laravel', 'Django', 'Git & GitHub']}

# Print entire dictionary
print(stud_info)

# Print student's name 
print(stud_info['name'])

# Add new key email
stud_info['email'] = 'abandaglory91@gmail.com'

# Change student's level
stud_info['level'] = '500'

# Remove age key 
del stud_info['age']

print(stud_info)