# Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]. 
x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)
#2 Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
# students[0].update({"last_name":"Bryant"})
# print(students)
students[0]["last_name"]="Bryan"
print(students)
#3 In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory["soccer"][0]="Andres"
print(sports_directory)
#4 Change the value 20 in y to 30
z = [ {'x': 10, 'y': 20} ]
z[0]["y"]=30
print(z)
################################################################################################################
# Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the associated value. 
# For example, given the following list:
# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
def iterate_dictionary(list):
    for i in range(len(list)):
        print(list[i])
iterate_dictionary(students)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# BONUS CHALLENGUE
def iterateDictionary(students):
    for x in range(0, len(students)):
        first_name = students[x]["first_name"]
        last_name = students[x]["last_name"]
        print(f"first_name - {first_name} - {last_name} - {last_name}")
iterateDictionary(students)  
# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries
# and a key name, the function prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:
def iterate_dictionary_2(list):
    for i in range(len(list)):
        print(list[i]['first_name'])
        print(list[i]['last_name'])
iterate_dictionary_2(students)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
################################################################################################################
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info(dict):
    print('')
    print(f"{len(dict['locations'])} LOCATIONS")
    for i in range(len(dict['locations'])):
        print(dict['locations'][i])
    print('')
    print(f"{len(dict['instructors'])} INSTRUCTORS")
    for i in range(len(dict['instructors'])):
        print(dict['instructors'][i])
print_info(dojo)

# Kyle's challengue
def printInfo(dojo):
    #repeat twice cuz only 2 in dojo list
    for i in dojo:
        print(str(len(dojo[i])) + " " + i)
        for values in range(0,len(dojo[i])):
            print(dojo[i][values])
        print("-" * 25)
# Some Change