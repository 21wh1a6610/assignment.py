#implementation of strings
#Splitting and Concatenating Strings
str1 = "This is the string we will split into a list of words"
list_of_words = str1.split()
print(list_of_words)
#Operations on String in Python
print("python".upper())
print("PYTHON".lower())
print('Python'.find('th'))
print('Python Is Fun 0 Percent'.replace('0','100'))
#implementation of list
#Adding Elements
my_list = [1, 2, 3]
print(my_list)
my_list.append([555, 12]) 
print(my_list)
my_list.extend([234, 'more_example']) 
print(my_list)
my_list.insert(1, 'insert_example') 
print(my_list)
#Deleting Elements
my_list = [1, 2, 3, 'example', 3.132, 10, 30]
del my_list[5] 
print(my_list)
my_list.remove('example')
print(my_list)
a = my_list.pop(1) 
print('Popped Element: ', a, ' List remaining: ', my_list)
my_list.clear() 
print(my_list)
#implementation of dictionary
#Creating a Dictionary
my_dict = {} 
print(my_dict)
my_dict = {1: 'Python', 2: 'Java'} 
print(my_dict)
#Changing and Adding key, value pairs
my_dict = {'First': 'Python', 'Second': 'Java'}
print(my_dict)
my_dict['Second'] = 'C++' 
print(my_dict)
my_dict['Third'] = 'Ruby' 
print(my_dict)
#Deleting key, value pairs
my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
a = my_dict.pop('Third') #pop element
print('Value:', a)
print('Dictionary:', my_dict)
b = my_dict.popitem() #pop the key-value pair
print('Key, value pair:', b)
print('Dictionary', my_dict)
my_dict.clear() #empty dictionary
print('n', my_dict)


