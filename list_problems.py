#1.Write a Python program to sum all the items in a list.
'''
s=[2,4,5,3,9,10,11,12]
res=[]
s1=0
for num in s:
    s1 += num
res.append(s1)
print(res)
'''

#2.Write a Python program to print  multiplies all the items in a list.
'''
s=[2,4,5,3,6,8,9]
res=1
for num in s:
    res *= num
print(res)
'''

#3.Write a Python program to get the largest number from a list.
'''
li=[2,7,4,5,8,22,34,54,3,88,6,93]
li.sort(reverse=True)
print(li[0])
'''

#4.Write a Python program to get the smallest number from a list
'''
li=[2,7,4,5,8,22,34,54,3,88,6,93]
li.sort()
print(li[0])
'''

#5.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2
'''
li=['cat','non','oppo','lol','bat','man','mom','top','om','co','up','a','b','c','aa']
res=0
for str in li:
    if len(str)>=2:
        if str[0]==str[-1]:
            #print(str,end=' ')
            res += li.count(str)
print('res=',res)
'''

#6.	Write a Python program to remove duplicates from a list.
'''
li=[2,4,1,6,3,8,4,7,5,9,6,2,5,2,3,4,5,6,7,9,0,1,2,7,8,9]
lii=[]
new_li=set(li)
lii.extend(new_li)
print(lii)
'''

#7.Write a Python program to check a list is empty or not.
'''
li=[2,4,1,6,3,8,4,7,5,9,6]
if len(li)>=1:
    print('list is not empty')
else:
    print('list is empty')
'''

#8.Write a Python program to clone or copy a list.
'''
li=['Rohan','Rohit','Omkar','Shubham','Aniket']
newli=li.copy()
print(newli)
'''

#9. Write a Python program to find the list of words that are longer than n from a given list of words.
'''
li=['bank','basket','bath','be','bear','beautiful','beer','bed','bedroom','behave','before','begin','behind','bell','below','besides','better','between',]
newli=[]
no=int(input('enter the length that you want than that :'))
for words in li:
    if len(words)>=no:
        newli.append(words)
print(newli,len(newli))
'''

#10.Write a Python function that takes two lists and returns True if they have at least one common member
'''
def funct(a=[],b=[]):
    for i in range(len(a)):
        if a[i] in b:
            return True
val=funct([1,2,4,6,0],[3,5,7,8,0])
print(val)
'''



#11.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
'''
li=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
li.pop(5)
li.pop(4)
li.pop(0)
print(li)
'''

#12.Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''
li=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
li.sort(key=lambda x:x[-1],reverse=True)
print(li)
'''

#14.Write a Python program to print the numbers of a specified list after removing even numbers from it.
'''
li=[2,12,43,1,18,3,0,4,29,5,6,26,8,23,7,9,21,32,65]
newli=[]
for ele in li:
    if ele%2==1 :
        newli.append(ele)
print(newli)
'''


#15.Write a Python program to get the difference between the two lists.
'''
a=['a', 'c', 'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm','x', 'n','r','s']
b=['b','f','g','h','i','j','k','l',a', 'c', 'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm''o','p','t','u','v','w','y']

li=[]
for ele in a:
    if ele not in b:
        li.append(ele)
for el in b:
    if el not in a:
        li.append(el)
print(li)
'''

#16.Write a Python program access the index of a list.
'''
a=['a', 'c', 'e', 'g', 'h', 'i', 'j']
for i in a:
    print(i,'=',a.index(i))
'''

#17.Write a Python program to convert a list of characters into a string.
'''
li=['r','o','h','a','n']
res=''.join(li)
print(res)
'''

#18.Write a Python program to find the index of an item in a specified list.
'''
a=['a',4,45.2,'rohan','c', 'e', 'g', 'h', 'i', 'j']

r=a.index('rohan')
print(r)
'''

#19.Write a Python program to append a list to the second list.
'''
a=['a', 'c', 'e', 'g', 'h', 'i', 'j']
b=[12,34,5,6,78,9,10]
a.append(b)
print(a)
'''

#20.Write a Python program to get unique values from a list.
'''
b=['a','b', 'c', 'e','i', 'g', 'h', 'i', 'j','a','b','c','e']

li=[]
for i in b:
    if i not in li:
        li.extend(i)
print(li)
'''

#21.Write a Python program to get the frequency of the elements in a list
'''
b=['a','b', 'c', 'e','i', 'g', 'h', 'i', 'j','a','b','c','e']
a=input('enter the value : ')
lii=0
for i in b:
    if i==a:
        lii=lii+1
print(lii)

#for integers
li=[2,7,0,6,9,2,3,4,2,5,6,7,2,8]
x=int(input('enter number to find frequency : '))
res=0
for i in range(len(li)):
    if li[i]==x:
        res=res+1
print('Frequenncy=',res)
'''

#22.Write a Python program to find common items from two lists.
'''
a=[2,4,6,8,1,3,5,0]
b=[1,3,5,7,9,0,8]
li=[]
for i in a:
    if i in b:
        li=li+[i]
print(li)
'''

#23.Write a Python program to split a list every Nth element.
#Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
#Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c','f','i','l']]
'''
a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
x=3
li=[]
for i in range(x):
    li.append(a[i::3])
print(li)
'''

#Sort in reverse the given list with printing unique values  without using any builtins.
'''
a = [0.6, 0.6, 0.7, 1, 290, -300, -26, -3.4, -0, -34.9, 1, 3, 4, 2, 2, -3.4, 6, 7, 8]
li = []
for val in a:
    if val not in li:
        li = li + [val]

print(li)
for i in range(len(li)):
    for j in range(len(li) - 1):
        if li[j] >= li[j + 1]:
            empt = li[j]
            li[j] = li[j + 1]
            li[j + 1] = empt
print(li)
'''

#----Bubble sort------#
"""
li = [2,4,9,6,8,1,3,5,7,0]
# li = ['n', 'a', 'b', 'x']
for i in range(len(li)):
    print(i)
    for j in range(i,len(li)):
        if li[i] >= li[j]:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp
print(li)
"""
