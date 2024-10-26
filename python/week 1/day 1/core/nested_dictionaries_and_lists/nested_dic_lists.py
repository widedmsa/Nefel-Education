#Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['first_name']='Bryant'
print(students)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]='Andres'
print(sports_directory)
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

#Iterate Through a List of Dictionaries
def  iterateDictionary(students) :
    for student in students :
            print(f"first_name - {student['first_name']} , last_name - {student['last_name']}")
x = iterateDictionary([
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ])
print(x)



#Get Values From a List of Dictionaries 
def iterateDictionary2 (key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary2('first_name', students)


#Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key, value_list in some_dict.items():
        print(f"{key}: {len(value_list)}")
        for value in value_list:
            print(value)


