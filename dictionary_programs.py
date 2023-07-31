# 1. Write a Python script to sort (ascending and descending) a dictionary by value. 
"""
dic = {
    "name": "John",
    "age": "20",
    "grade": "A",
    "subjects": "Math",
    "street": "123 Main St",
    "city": "New York",
    "state": "NY"
}

#By using in-build fuction
dic1 = {}
for key in sorted(dic.keys()):
    print(key)
    dic1[key] = dic[key]
print(dic1)
"""
#without using in-build function
"""
li = [(key, val) for key, val in dic.items()]
for i in range(len(li)-1):
    for j in range(i+1, len(li)):
        if li[i][1] > li[j][1]:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp
# dic1 = {key:val for key, val in li}
# print(dic1)
print(dict(li))
"""
#By using lambda function
"""
res = sorted(dic.items(), key=lambda x:x[1])
print(dict(res))
"""


# 2. Write a Python script to add a key to a dictionary. 
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30} 
"""
dic = {0: 10, 1: 20}
# dic[2] = 30
dic.setdefault(2, 30)
print(dic)
"""


# 3. Write a Python script to concatenate following dictionaries to create a new one. 
# Sample Dictionary : 
# dic1={1:10, 2:20} 
# dic2={3:30, 4:40} 
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 

"""
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}

res = {}
res.update(dic1)
res.update(dic2)
res.update(dic3)
print(res)
"""


# 4. Write a Python script to check if a given key already exists in a dictionary.

"""
dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 

for i in range(1,10):
    if i in dic:
        print(i, 'is already exist in dic')
"""


# 5. Write a Python program to iterate over dictionaries using for loops. 
"""
dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8:80, 9:90}
for key, val in dic.items():
    print("Key:", key, "value:", val)
"""


# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
# Sample Dictionary ( n = 5) : 
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
"""
n = 10
dic = {}
for i in range(n+1):
    dic[i] = i*i
print(dic)
"""


# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. 
# Sample Dictionary : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225} 
"""
dic = {}
for i in range(1,16):
    dic[i] = i*i
print(dic)
"""


# 8. Write a Python script to merge two Python dictionaries. 
"""
dic1={1:10, 2:20} 
dic2={3:30, 4:40}

new_dic = {}
new_dic.update(dic1)
new_dic.update(dic2)
print(new_dic)
"""


# 9. Write a Python program to sum all the items in a dictionary. 
"""
dic = {1: 1, 2: 4, 3: 9, 4: 16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100}

sum = 0
for key, val in dic.items():
    sum += key
print(sum)
"""


# 10. Write a Python program to multiply all the items in a dictionary. 
"""
dic = {1: 1, 2: 4, 3: 9, 4: 16, 5:25}

res = 1
for key, val in dic.items():
    res *= key
print(res)
"""


# 11. Write a Python program to remove a key from a dictionary. 
"""
dic = {1: 1, 2: 4, 3: 9, 4: 16, 5:25}
#we can't remove key from dictionary...
val = []
for k, v in dic.items():
    val.append(v)
print(val)
"""


# 12. Write a Python program to map two lists into a dictionary. 
"""
l1 = ['Rohan', 'Amol', 'Atul', 'Vaibhav', 'Ashish']
l2 = ['Kolhapur', 'Jalgaon', 'Sangli', 'Usmanabad', 'Nanded']

dic = dict(zip(l1, l2))
print(dic)
"""


# 13. Write a Python program to sort a dictionary by key. 
"""
dic = {'Rohan': 'Kolhapur', 'Amol': 'Jalgaon', 'Atul': 'Sangli', 'Vaibhav': 'Usmanabad', 'Ashish': 'Nanded'}
# print(dict(sorted(dic.items(), key= lambda x:x[0])))

li = [(key, val) for key, val in dic.items()]

for i in range(len(li)-1):
    for j in range(i, len(li)):
        if li[i][0] > li[j][0]:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp

print(dict(li)) 
"""


# 14. Write a Python program to get the maximum and minimum value in a dictionary. 

"""
dic = {1: 1, 12:144, 8:64, 2: 4, 3: 9, 11:121, 4: 16, 5:25, 15:225}
print(sorted(dic.values(), reverse=True)[0])
"""


# 16. Write a Python program to get a dictionary from an object's fields.

"""
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

def get_dict_from_object_field(obj):
    if not isinstance(obj, object):
        raise TypeError("Input must be an object.")
    return obj.__dict__


if __name__=="__main__":
    person_obj = Person("Rohan", 22, "Student")
    person_dict = get_dict_from_object_field(person_obj)
    print(person_dict)
"""


# 17. Write a Python program to remove duplicates from Dictionary. 
"""
dic = {1: 1, 12:144, 8:64, 2:4, 3:9, 11:121, 4: 16, 7:25, 6:9, 13:121, 4: 16, 5:25, 16:225, 15:225}
dic1 = {}
li = []
for key, val in dic.items():
    if val not in li:
        li.append(val)
    else:
        dic1[key] = val
for i in dic1:
    dic.pop(i)
    
print(dic)
"""


# 18. Write a Python program to check a dictionary is empty or not. 
"""
dic = {1: 1, 12:144, 8:64, 2: 4, 3: 9, 11:121, 4: 16, 5:25, 15:225}

if not dic:
    print('given dictionory is empty')
else:
    print("given dictionory is not empty")
"""


# 19. Write a Python program to combine two dictionary adding values for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300}) 

"""
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

for key in d2:
    if key in d1:
        d1[key] += d2[key]
    else:
        d1[key] = d2[key]
print(d1)
"""


# 20. Write a Python program to print all unique values in a dictionary. 
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'} 

"""
li = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

res = set()
for i in li:
    for j in i:
        res.add(i[j])
print(res)
"""


# 21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. 
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output: 
# ac
# ad
# bc
# bd 
"""
temp = []
dic = {'1':['a','b'], '2':['c','d']}

for val in dic.values():
    temp.append(val)

for i in temp[0]:
    for j in temp[1]:
        print(i+j)
"""


# 22. Write a Python program to find the highest 3 values in a dictionary.
"""
dic = {1: 1, 12:144, 8:64, 2: 4, 3: 9, 11:121, 4: 16, 5:25, 15:225}

li = []
for val in sorted(dic.values(), reverse=True):
    li.append(val)
    if len(li)==3:
        break

print(li)
"""


# 23. Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300}) 
"""
li = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

dic = {}
for item in li:
    if item['item'] not in dic:
        dic[item['item']] = item['amount']
    else:
        dic[item['item']] += item['amount']
print(dic)
"""


# 24. Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} 
"""
str = 'w3resource'
dic = {}

for i in str:
    dic[i] = str.count(i)
print(dic)
"""


# 25. Write a Python program to print a dictionary in table format. 
"""
from tabulate import tabulate
def dict_to_table(dic):
    headers = ["Key", "Value"]
    data = [(key, val) for key, val in dic.items()]
    table = tabulate(data, headers=headers, tablefmt="grid")
    print(table)

dictionary = {
        "Name": "John Doe",
        "Age": 30,
        "Occupation": "Engineer",
        "Location": "New York",
        "Hobbies": ["Reading", "Traveling", "Photography"]
}

dict_to_table(dictionary)

"""



# 26. Write a Python program to count the values associated with key in a dictionary. 
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True 
"""
li = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

count = 0
for i in li:
    if i['success'] == True:
        count += 1
print(count, 'dictionaries have success as True')
"""


# 27. Write a Python program to convert a list into a nested dictionary of keys. 
"""
def list_to_nested_dict(li, val):
    result = {}
    dic = {}

    dic[li[-1]] = val
    for key in li[::-1][1:]:
        result = {}
        result[key] = dic
        dic = result
    print(result)


li = ["first", "second", "third", "fourth"]
value = "Nested Dictionary"

list_to_nested_dict(li, value)

"""


# 28. Write a Python program to sort a list alphabetically in a dictionary. 
"""
dic = {"Developer":["rohan", "atul", "anil", "vaibhav"], "Tester":["Govind", "Ashish", "Trishala", "Raju",]}

result = {}
for key, val in dic.items():
    result[key] = sorted(val)
print(result)

"""


# 29. Write a Python program to remove spaces from dictionary keys. 
"""
dic = {"Python Developer":["rohan", "atul", "anil", "vaibhav"], "Python Tester":["Govind", "Ashish", "Trishala", "Raju",]}
result = {}

for key,val in dic.items():
    result[''.join(key.split())] = val
print(result)
"""


# 30. Write a Python program to get the top three items in a shop. 
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output: 
# item4 55
# item1 45.5
# item3 41.3
"""
dic = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
result = []

for item in sorted(dic.items(), key=lambda x:x[1], reverse=True):
    result.append(item)
for i in result[:3]:
    print(*i)
"""


# 31. Write a Python program to get the key, value and item in a dictionary. 
"""
from tabulate import tabulate

def dic_items(dict):
    headers = ['Key', 'Value', 'Items']
    data = [(key, val, (key, val))for key, val in dict.items()]
    table = tabulate(data, headers=headers, tablefmt="grid")
    return table

dic = {1: 1, 2: 4, 3: 9, 4: 16, 5:25, 8:64, 11:121, 12:144, 15:225}
obj = dic_items(dic)
print(obj)
"""


# 35. Write a Python program to sort Counter by value. 
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)] 
"""
dic = {'Math':81, 'Physics':83, 'Chemistry':87}

result = sorted(dic.items(), key=lambda x:x[1], reverse=True)
print(result)
"""


# 36. Write a Python program to create a dictionary from two lists without losing duplicate values. 
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}}) 
"""
li1 =['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
li2 = [1, 2, 2, 3]

dic = dict(zip(li1,li2))
print(dic)
"""



# 37. Write a Python program to replace dictionary values with their sum. 
"""
dic = {"realme": [1500,2000,1200,3000], "boat": [1000,1800,3000], "oppo": [2500,1700,5000], "Oneplus": [2500,3000,4500]}
newdic = {}
for key, val in dic.items():
    newdic[key] = sum(val)
print(newdic)
"""


# 38. Write a Python program to match key values in two dictionaries. 
# Sample dictionary: x={'key1': 1, 'key2': 3, 'key3': 2}, y={'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
"""
x={'key1': 1, 'key2': 3, 'key3': 2}
y={'key1': 1, 'key2': 2}

for key, val in y.items():
    if x[key] == val:
        print(key,':',val, "is present in both x & y ")
"""

