# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

test = "hello"
print(test)

""" triple quotes make 
comments for multiple
 lines
"""
#variables slide 14
var_1 = 12
x = 4
y =5

x,y = 4,5
z=x*y
z

talk_sweet_to_py = "Python is fun!"
print(talk_sweet_to_py)

#indexing variables slide 15
talk_sweet_to_py[0]
#returns 0th character
len(talk_sweet_to_py)
#so, talk_sweet_to_py[14] will return an error
talk_sweet_to_py[6:10] #does not include upper bound
talk_sweet_to_py[-1]
#[-1]returns last character of variable
talk_sweet_to_py[-2:]
#returns last 2 characters, starting with -2 onward
#slide 16 activity
x =5
y = 10
x= talk_sweet_to_py
x[0:6]
#slide 18 classes/types of variables
type(14) #int
type(3.14) #float
type("I am a string") #str
type(("I","am","a","tuple")) #tuple single and double quotes generally don't matter
#needs double parenthesis in this case because type takes only one argument
type(['I','am','a','list','lalala',3.14159]) #list
#generally tuples are for things of the same type, lists for things that may differ
#slide 19
#integers are whole numbers
#floats have decimals
x=4
y=round(5.5)
print(y)
type(y) #should make y int
y=3.
y
#you can turn any integer into a float without changing its value
#you can turn any float into an integer, but it will round to the nearest integer
#slide 20
x="I am a string!"
y='I am also a string'
z="Don't forget about me!"
#slide 21
e='I'm an error:)' #ways to get around this:
e="I'm not an error"#use double quotes to avoid the single quote apostrophy
e='I\'m not an error' #use backslash to treat the apostrophy as a literal character
e
#slide 22 tuples
x="a.","b,","c","d"
y='I','am','a','tuple'
#tuples can have multiple types
z="i",'am',"also",'a',"tuple",3.14
len(y)
z[-2:]
#indexes things differently than strings- rather than going by character, it goes by argument
#indexing through strings
y='I','am','a','tuple'
y[1][1]
z[5][2] #cannot index length for some types, including float
t=str(z[5])
t[2]#returns 1 for the 3rd character in 3.14
type(z[5]) #float
type(z) #tuple

#creating empty tuples as placeholder for incoming data (for loops foreshadow) slide 23
empty_tup=()
length_one_tup=('e',) #without comma length_one_tup will result in str type
type(empty_tup)

empty_tup+length_one_tup #results in ('e',) appends one to another because they are of the same type
empty_tup+length_one_tup+('hi','more','tupes') #returns ('e', 'hi', 'more', 'tupes')
empty_tup,length_one_tup,'hi','more','tupes' #returns ((), ('e',), 'hi', 'more', 'tupes')

len(empty_tup+length_one_tup+('hi','more','tupes')) #returns 4 for the elements in each tuple
len((empty_tup,length_one_tup,'hi','more','tupes')) #returns 5 for each tuple
#pluses appends tuples together, commas separate/build elements of tuples

#Lists slide 25
#lists are lists enclosed with [] and items separated by ,
x=['I','am','a','list']
y=['me',2,'!']
empty_list = []
len(x) #4
len(y) #3
len(empty_list) #0

#dictionaries are key value pairs slide 25
dict_1={'Malorie':29,'Jordan':25,'Grant':21}
empty_dict={}
dict_1.keys() #returns all keys
dict_!.values() #returns all values
dict_1['Malorie']#returns 29

#Basics, classes, methods, & print slide 26
#slide 27 integers and floats
y=round(5.5)
x=13; y=10 #can evaluate two statements in one line by inserting a ; between arguments
x+=5 # same as x=x+5
x=x+5
x
x+y
x*y
x**y
x/y
type(20/5)
z=20/6
float(20)/float(6)
print('hello')

#upgrade to 3
x=3
x**=4
x

#bonus: modulo
20/4 #5 no remainder
20%4 #0 remainder
20%6 #2


#slide 30
x= "I am a string"
x.upper() #returns lowercase
x.lower() #returns uppercase
y="I am also a string"
x="I am " + "a string"
x
x= ("I am","a string")
x
x = "I am " + "a string " +3.14 #returns error
x = 'I am ' + 'a string ' + '3.14' #returns I am a string 3.14

#slide 31 activity
#create a string by combining thre separate strings
z= "1" + " 4" + " 6"
z
#create a tuple name q by combining the same three sepearate strings
q= "1"," 4", " 6"
type(q)

r=talk_sweet_to_py 

talk_sweet_to_py[-4:-1].upper() #returns FUN

'fun' in talk_sweet_to_py #returns true

#slide 32 methods and operations: tuples
x = "I","am","a","tuple"
y = "me","2","!"
x+y 
len(x+y) #7
x,y #(('I', 'am', 'a', 'tuple'), ('me', '2', '!'))
len((x,y)) 
x=() #empy tuple x
type(x)
x=()
x+='a','b','c'
x
x+='d', #need comma to make 'd' tuple and not str
x+=tuple("d") #or do this
x

#last activity
x= x,("e","f","g")
x
#slide 34 methods and operations: lists
y=[2,3,"hello"]
y.append(x) #adds x to the end of the list
y.insert(i,x) #inserts x into the ith position of y
y.remove #removes the first instance of x from y, error is x is not in y

y.append("world") #y returns [2, 3, 'hello', 'world']
y.insert(2,4) # returns  [2, 3, 4, 'hello', 'world']
y.remove(4) #[2, 3, 'hello', 'world']
y.count('world') #counts the instances of world in y
y=[1,4,6,2,3]
y.sort() #returns y in numerical order **only works with lists of all same data types
y.sort(reverse=True) #returns reverse sorted order
y

y.index(3) #returns the location of the first 3
y.index(3,y.index(3)+1) #returns the location of the second 3
y.index(3,3)


#slide 37
dict_1={'Malorie':29,'Jordan':25,'Grant':21}
dict_1.keys()
type(dict_1.keys()) #list in python 2, dict type in python 3
dict_1.values()
type(dict_1.values())
dict_1.get('john','key not found') #returns key not found when john not in
# dict_1 returns value when john in dict_1

dict_1.keys()[0] #for python 3 need to do this: list(dist_1.keys()[0])

dict_1.keys()[dict_1.values().index(29)] #returns the key with the same index 
#number as the first instance of the value 29
#in python 3 list(dict_1.keys()[dict_1.values().index(29)])

dict_2={'Grant': 21, 'John': 29, 'Jordan': 25, 'Malorie': 29}
""" how to import packages
import numpy as np
import pandas as pd
"""


dict_1.keys()[dict_1.values().index(25)]

for i in dict_1.keys():
    value = dict_1.values()
    value
    
#Conditionals

#comparisons check a condition. The result is True or False
True == False #False
4 >3 #True

3<2**2

(4>3)==(3 in (1,2,3))

#for and if logic

range(10)
len(range(10))

[x for x in range(10)] #returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[x**x for x in range(5)] #returns [1, 1, 4, 27, 256] or 0**0, 1**1,2**2,3**3,4**4
['s' for x in range(3)] #sequence of s's 3 s's long

for i in range(len(dict_1.keys())):
    test = dict_1.values()
    test

A= (1,2,3)
B=[x for x in range(3) if x in A]
C=[x for x in A if x in B]
B
C

#function syntax inputs and outputs

def name_of_function(placeholder_name_of_input):
    define function of placeholder_name_of_input
    #usually ends with a return or print statement

def simply_print(x):
    print(x)

simply_print() #this is useful for processes that are repetitive

def simply_print2(x):
    print"your input was", str(x)
simply_print2(12)

"""
if(condition):
    do stuff
"""

"""
x,y=3,4

if (x<y):
    print(x*y)
    
for x in dates:
    for y in dealerships:
        for z in product_specialists:
            for q in categories:
"""
x= (1,2,3)

def sum_it(x):
    summed = 0
    for i in x:
        summed += i
    return(summed)
sum_it((2,5,6)) #13

#summed is still 6

x= (1,2,3)

def mean_it(e):
    summed = 0
    for i in e:
        summed += i
    return ( float(summed)/float(len(e)) )
           
mean_it((1,2,3))

