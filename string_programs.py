
#1.Write a Python program to calculate the length of a string.
"""
s='Rohan Gajanan Katkar'
print(len(s))
"""

#2.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'

"""
def func(str):
    s = str
    new_s = s.replace(s[0], '$')
    res = s[0] + new_s[1:]
    print(res) 

func('initialize')
"""



#3.Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'
"""
s1='abc'
s2='xyz'
new_s1=s1.replace(s1[:2],s2[:2])
new_s2=s2.replace(s2[:2],s1[:2])

res=new_s1+' '+new_s2
print(res)
"""


#4.Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
#Sample String : 'abc'
#Expected Result : 'abcing'
#Sample String : 'string'
#Expected Result : 'stringly'
"""
a=input('enter a string :')
if (len(a))<3:
    print(a)
elif a.endswith('ing'):
    print(a+'ly')
else:
    print(a+'ing')
"""


#5.Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
#Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
#Expected Result : 'The lyrics is good!'
#'The lyrics is poor!'

'''
def lyric():
    str='The lyrics is not that poor!'\
            'The lyrics is poor!'
    n1=str.find('not')
    p1=str.find('poor')+len('poor')
    msg=str.replace(str[n1:],'good') + str[p1:]
    return msg

obj=lyric()
print(obj)
'''

#6.Write a Python function that takes a list of words and returns the word with the longest length.
'''
def wordli(li):
    msg=''.join(li)
    return msg

obj=wordli(['Python','With','Data','Science'])
print(obj)
'''



#7.Write a Python program to remove the nth index character from a nonempty string.
'''
str='The lyrics is not that poor!'
indx='not'
prefix=str[:str.index(indx)]
suffix=str[str.index(indx)+1:]

res=prefix+suffix
print(res)
'''

#8.Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
'''
s='rohan'

res=s[-1]+s[1:-1]+s[0]
print(res)
'''

#9.Write a Python program to remove the characters which have odd index values of a given string.
'''str='The lyrics is not that poor!'
for ele in str:
    if str.index(ele)%2==0:
        print(ele,end='')'''


#10.Write a Python program to count the occurrences of each word in a given sentence.

'''s='rohangajanankatkar'
dic = {}
for i in s:
    dic[i] = s.count(i)
print(dic)'''

#11.Write a Python script that takes input from the user and displays that input back in upper and lower cases
'''
str = input('Enter the string : ')
print('This is upper :',str.upper())
print('This is lower : ',str.lower())
'''


#12.Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
#Sample Words : red, white, black, red, green, black
#Expected Result : black, green, red, white,red
'''
str = 'red,white,black,red,green,black'
li = str.split(',')
print(li)
'''




#15.Write a Python program to print the following floating numbers upto 2 decimal places and with no decimal places.
#Given :- 203.556787655




#16.Write a Python program to convert a string in a list.
'''
str = 'Rohan Gajanan Katkar'
li = str.split()
print(li)
'''


