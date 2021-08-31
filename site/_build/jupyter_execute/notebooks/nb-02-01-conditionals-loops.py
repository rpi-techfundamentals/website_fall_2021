#!/usr/bin/env python
# coding: utf-8

# [![AnalyticsDojo](https://github.com/rpi-techfundamentals/spring2019-materials/blob/master/fig/final-logo.png?raw=1)](http://introml.analyticsdojo.com)
# <center><h1>Introduction to Python - Conditional Statements and Loops</h1></center>
# <center><h3><a href = 'http://introml.analyticsdojo.com'>introml.analyticsdojo.com</a></h3></center>
# 

# # Conditional Statements and Loops
# - (Need to know) Indentation in Python
# - What are conditional statements? Why do we need them?
# - If statements in Python
# - Why, Why not Loops?
# - Loops in Python
# - Exercises

# ## [Tabs vs Spaces](https://www.youtube.com/watch?v=SsoOG6ZeyUI)
# (Worth Watching)

# ## Indentation in Python
# - Indentation has a very specific role in Python and is **important!**
# - It is used as alternative to parenthesis, and getting it wrong will cause errors. 
# - Python 3 allows 4 spaces or tabs, but not both. [But in working in Jupyter seems to work fine.]
# - In Python, spaces are preferred according to the [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/).
# 
# 

# ## What are conditional statements? Why do we need them?

# ## `if` Statements
# - Enables logical branching and recoding of data.
# - BUT, `if statements` can result in long code branches, repeated code.
# - Best to keep if statements short.
# - Keep in mind the [Zen of Python](https://www.python.org/dev/peps/pep-0020/) when writing if statements.  

# ## Conditional Statements and Indentation
# - The syntax for control structures in Python use _colons_ and _indentation_.
# - Beware that indentation affects flow.
# - `if` statemenet enable logic. 
# - `elif` give additional conditions.
# - `else` gives what to do if other conditions are not met.

# In[1]:


y = 5
x = 3
if x > 0:
    print ('x is strictly positive')
    print (x)    
print ('Finished.', x, y)
x


# In[2]:


x = 1
y = 0
if x > 0:
    print ('x is greater than 0')
    if y > 0:
        print ('& y is also greater than 0')
    elif y<0:
        print ('& y is  0')
    else:
        print ('& y is equal 0')
print ("x: ",x)
print ('Finished.')


# In[10]:


x > 0


# In[11]:


x != 5 or 


# In[15]:


x=5
x


# ## Python Logit and Conditions
# - Less than	<
# - Greater than		>
# - Less than or equal	≤	<=
# - Greater than or equal >=
# - Equals	==
# - Not equal	!=
# - `and` can be used to put multiple logical expressions together.
# - `or` can be used to put multiple logical expressions together.

# In[19]:


x = -1
y = 1
if x >= 0 and y >= 0:
    print ('x and y are greater than 0 or 0')
elif  x >= 0 or y >= 0:
    if x > 0:
        print ('x is greater than 0')
    else:
        print ('y is greater than 0')
else:
    print ('neither x nor y greater than 0')


# ## Python Conditionals (Alt Syntax) 
# - Clean syntax doesn't get complex branching 
# - Python ternary conditional operator `(falseValue, trueValue)[<logicalTest>]`
# - Lambda Functions as if statement.

# In[21]:


x=0
z = 5 if x > 0 else 0
print(z)


# In[22]:


# This is a form of if statement called ternary conditional operator 
x=1
#The first value is the value if the conditional is false
z=(0, 5)[x>0]
print(z)


# ## Why, Why Not Loops?
# - Iterate over arrays or lists easily. `for` or `while` loops can be nested.
# - BUT, in many cases for loops don't scale well and are slower than alternate methods involving functions. 
# - BUT, don't worry about prematurely optimizing code.
# - Often if you are doing a loop, there is a function that is faster.  You might not care for small data applications.
# - Keep in mind the [Zen of Python](https://www.python.org/dev/peps/pep-0020/#id3) when writing `for` statements.

# In[23]:


#Here we are iterating on lists.
sum=0
for ad in [1, 2, 3]: 
    sum+=ad    #This is short hand for sum = sum+ad
    print(sum) 
    
for country in ['England', 'Spain', 'India']:
    print(country)


# In[24]:


x=[0,1,2]
y=['a','b','c']
#Nested for loops
for a in x:
    for b in y:
        print(a,b)


# ## The `for` Loop
# - Can accept a `range(start, stop, step)` or `range(stop)` object
# - Can break out of it with a `break` command

# In[21]:


z=range(5)
z


# In[25]:


#Range is a built in function that can be passed to a for loop
#https://docs.python.org/3/library/functions.html#func-range
#Range accepts a number and a (start/stop/step) like the arrange command.
z=range(5)
print(z, type(z))
#Range
for i in z:
    print('Printing ten')
for i in range(5):
    print('Print five more')
for i in range(5,20,2):
    print('i: %d is the value' % (i)) 
    print(f'i:{i}  is the value' ) #This is an alternate way of embedding values in text.


# In[26]:


#Sometimes you need to break out of a loop
for x in range(3):
    print('x:',x)
    if x == 2:
        break


# ### List, Set, and Dict Comprehension (Fancy for Loops)
# - Python has a special way of compressing list building to a single line. 
# - Set Comprehension is very similar, but with the `{` bracket.
# - Can incorporate conditionals. 
# - S
# 

# In[26]:


#This is the long way of building lists.
L = []
for n in range(10):
    L.append(n ** 2)
L


# In[22]:


#With list comprehension.  
L=[n ** 2 for n in range(10)]
L


# In[28]:


#Any actions are on left side, any conditionals on right side 
[i for i in range(20) if i % 3 == 0]


# ### Multiple Interators
# - Iterating on multiple values

# In[29]:


[(i, j) for i in range(2) for j in range(3)]


# ### Set Comprehension
# - Remember sets must have unique values.

# In[30]:


#We can change it to a setby just changing the brackets.
{n**2 for n in range(6)}


# ### Dict Comprehension
# - Remember sets must have unique values.

# In[30]:


#We can change it to a dictionary by just changing the brackets and adding a colon.
{n:n**2 for n in range(6)}


# ## While Loops
# - Performs a loop while a conditional is True.
# - Doesn't auto-increment.
# 

# In[31]:


# While loop is a very interesting 
x = 1
sum=0
while x<10:
    print ("Printing x= %d sum= %d" % (x, sum)) #Note this alternate way of specufiy
    x += 1
    sum+=10


# ## Recoding Variables/Creating Features with `for/if`
# - Often we want to recode data applying some type of conditional statement to each value of a series, list, or column of a data frame.
# - [Regular Expressions](https://docs.python.org/3/howto/regex.html) can be useful in recoding 

# In[32]:


#Titanic Preview Women and Children first

gender=['Female', 'Female','Female', 'Male', 'Male', 'Male' ]
age=[75, 45, 15, 1, 45, 4 ]
name = ['Ms. Sally White', 'Mrs. Susan King', 'Amanda Russ', 'Rev. John Smith' ]
survived=[]
for i in range(len(gender)):
#This is encoding a simple model that women survived.  
    if gender[i]=='Female':
        survived.append('Survived')
    else:
        survived.append('Died')      
print(survived)
        
#BUT, we won't typically be using this type of recoding, so we aren't going to do a lot of exercises on it.     


# This work is licensed under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) license agreement.
# Adopted from [materials](https://github.com/phelps-sg/python-bigdata) Copyright [Steve Phelps](http://sphelps.net) 2014
