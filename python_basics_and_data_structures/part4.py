# Sets
numbers = [1,2,3,4,2,5,3,6,1]

# Convert list into set
numbers = set(numbers)

print(numbers)
# print(*numbers, sep=', ')

# Some values disappeared because the set data structure sorts numbers in ascending order and takes care of duplicate values by removing them.

languages = ['Python', 'Java', 'Python', 'C++', 'JavaScript', 'Python']

languages = set(languages)

print(languages)

languages.add('Django')

print(languages)