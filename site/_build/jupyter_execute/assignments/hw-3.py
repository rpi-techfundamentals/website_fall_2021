#!/usr/bin/env python
# coding: utf-8

# #### Homework-3
# ##### Total number of points: 70
# #### Due date: September 27, 2021
# 
# Before you submit this homework, make sure everything runs as expected. First, restart the kernel (in the menu, select Kernel → Restart) and then run all cells (in the menubar, select Cell → Run All). You can discuss with others regarding the homework but all work must be your own.
# 
# This homework will test your knowledge on data manipulation, manipulating strings and feature preprocessing. The Python notebooks shared will be helpful to solve these problems.  
# 
# Steps to evaluate your solutions:
# 
# Step-1: Try on Colab or Anaconda (Windows: https://docs.anaconda.com/anaconda/install/windows/ ; Mac:https://docs.anaconda.com/anaconda/install/mac-os/ ; Linux: https://docs.anaconda.com/anaconda/install/linux/)
# 
# Step-2: Open the Jupyter Notebook by first launching the anaconda software console
# 
# Step-3: Open the homework's .ipynb file and write your solutions at the appropriate location "# YOUR CODE HERE"
# 
# Step-4: You can restart the kernel and click run all (in the menubar, select Cell → Run All) on the center-right on the top of this window.
# 
# Step-5: Now go to "File" then click on "Download as" then click on "Notebook (.ipynb)" Please DO NOT change the file name and just keep it as ".ipynb"
# 
# Step-6: Go to lms.rpi.edu and upload your homework at the appropriate link to submit this homework.
# 
# 
# #### Please note that for any question in this assignment you will receive points ONLY if your solution passes all the test cases including hidden testcases as well. So please make sure you try to think all possible scenarios before submitting your answers.  
# - Note that hidden tests are present to ensure you are not hardcoding. 
# - If caught cheating: 
#     - you will receive a score of 0 for the 1st violation. 
#     - for repeated incidents, you will receive an automatic 'F' grade and will be reported to the dean of Lally School of Management. 

# Use the titanic dataset found here:  (https://raw.githubusercontent.com/lmanikon/lmanikon.github.io/master/teaching/datasets/titanic.csv) 
# Please note that we will use this dataset in some of the questions here below. 

# #### Q1 [5 points]. Shape of a Data Frame. 
# 1. Import pandas package as pd.
# 2. Read the file from the 'url' and load the data into dataframe `df` with default index.
# 3. print the number of rows and columns as `rows1` and `cols1` respectively. 
# 

# In[ ]:



url='https://raw.githubusercontent.com/lmanikon/lmanikon.github.io/master/teaching/datasets/titanic.csv'

# YOUR CODE HERE


# In[ ]:


assert rows1==891
assert df['age'].sum()==21205.17


# Now we will be using the above dataframe df to do preprocessing operations on this data. 
# All the required libraries for further processing will be loaded here. 

# In[ ]:


import numpy as np
import pandas as pd
import re


# #### Q2 [5 points]. Aggregate operation
# 1. Use the dataframe `df` created in the previous cell to group together rows based on the `gender` and assign this output to `ggby`
# - Hint -- Use groupby operation 
# 
# 

# In[ ]:


#Use the Dataframe `df` created in Q1 
#Hint -- use groupby 


# YOUR CODE HERE


# In[ ]:


assert len(ggby)==2


# #### Q3 [5 points]. Now use this `ggby` format to 
# 1. compute the mean age (use the 'age' attribute) of passengers who are `female` and `male` ('gender' attribute) as `fage` and `mage` respectively. 
# 2. Round the `fage` and `mage` to print only 2 decimal places -- for example 3.14156 converts to 3.14 
# 

# In[ ]:


#Hint -- Use ONLY the dataframe's mean operation

# YOUR CODE HERE


# In[ ]:


assert fage==27.92
assert mage==30.73


# #### Q4 [5 points]. Now use the above groups obtained by grouping on the `gender` attribute 
# 1. and consider only the 'female' group to save that group as a sub dataframe `fmdf`. 
# 
# Note that `fmdf` will act as a new dataframe with all the columns as the original dataframe. 
# 

# In[ ]:



# YOUR CODE HERE


# In[ ]:


assert len(fmdf['age'])==314
assert len(fmdf.columns)==15
assert (fmdf['age'].sum())==7286.0


# #### Q5 [5 points]. Now using `fmdf` 
# 1. remove all the rows where atleast one element is missing and 
# 2. save this as a new dataframe object `newfm`

# In[ ]:


#Use 'fmdf' from Q4 above. 

# YOUR CODE HERE


# In[ ]:


assert newfm['age'].sum() == 2875.5
assert newfm['survived'].count() == 88


# #### Q6 [5 points]. Lets focus on stratified sampling 
# 1. Utilize the original dataframe `df` we created in Q1 to now perform 3 different subgroups of data based on the `who` attribute 
# - There are 3 groups -- `woman`, `man`, `child` 
# 2. Perform random sampling to sample 5 data points (or rows) from each group -- `wsample`, `msample` and `csample` -- these will look like dataframes as well
# 

# In[ ]:


#Stratified sampling

# YOUR CODE HERE


# In[ ]:


assert set(wsample['gender'])=={'female'}
assert set(msample['gender'])=={'male'}


# #### Q7 [10 points]. Lets focus on feature manipulation 
# 1. Consider the original dataframe `df`. 
# 2. Remove all the rows with atleast one missing value. 
# 3. Then Standardize the `age` attribute -- which means replace each value in  the `age` attribute with the corresponding standardized value. You are modifying `df['age']`.
# 
# Please use the definition I gave during the lectures about what standardize means. 
# For this question only use `np.mean()` and `np.std()` functions to compute the mean and standard deviation values for a given series. 
# 

# In[ ]:


#Only use numpy's mean() and std() functions 

# YOUR CODE HERE


# In[ ]:


assert round(df['age'].sum(), 2)==145.84


# #### Q8 [10 points]. Lets now focus on binarization
# Utilize the original data frame `df` we created in Q1 (cell 2) to perform binarization
# 1. Re-read the file from url in Q1 and create a dataframe `df`
# 2. Remove all the rows with atleast one missing value
# 3. If the `embark_town` is `Queenstown` replace with 1 otherwise 0.

# In[ ]:


url='https://raw.githubusercontent.com/lmanikon/lmanikon.github.io/master/teaching/datasets/titanic.csv'

# YOUR CODE HERE


# In[ ]:


assert (df['embark_town'].sum())==2
assert set(df['embark_town'])=={0,1}


# #### Q9 [10 points]. Use the html content shared here below and parse it using the 'soup' object to 
# 1. print all the unique `Hometown` values as a list object `hts`
# 2. Convert each value of the hometown to a lower-case
# 3. Failure to print the answer as a list will lead to loss of points. 
# 

# In[ ]:


import requests
from bs4 import BeautifulSoup
import operator
import pandas as pd
import json
newtext = """
<p>
    <strong class="person1">YOB:</strong> 1990<br />
    <strong class="person1">GENDER:</strong> FEMALE<br />
    <strong class="person1">EYE COLOR:</strong> GREEN<br />
    <strong class="person1">HAIR COLOR:</strong> BROWN<br />
    <strong class="person1">GPA:</strong> 4<br />
    <strong class="person1">Hometown:</strong> Minneapolis<br />
</p>

<p>
    <strong class="person2">YOB:</strong> 1993<br />
    <strong class="person2">GENDER:</strong> FEMALE<br />
    <strong class="person2">EYE COLOR:</strong> BROWN<br />
    <strong class="person2">HAIR COLOR:</strong> BLACK<br />
    <strong class="person2">GPA:</strong> 3.5<br />
    <strong class="person2">Hometown:</strong> New York<br />
</p>

"""
hts=[]
soup = BeautifulSoup(newtext)

# YOUR CODE HERE


# In[ ]:


assert len(hts)==2
assert hts==['minneapolis', 'new york']


# #### Q10 [5 points]. Given a string 'str10' first split the string into words and convert them to lowercase. 
# - Now using the 'join' operation we learnt in the class, concatenate these words to a new string `str11` to ensure each word will now be in a new line
# - for example: str1 is 'it is cold today' to str2 will be:
# 
# `it
# is
# cold
# today`

# In[ ]:


str10 = 'Email the company at xyz@abcd.com and is the easiest way compared to tweet @abcdxyz'
# YOUR CODE HERE


# In[ ]:


assert len(str11)==83


# #### Q11 [5 points]. Use the regular expressions package to extract all the email ids mentioned in the above sentence `str10` as a list object `emails`

# In[ ]:


import re
str10 = 'Email the company at xyz@abcd.com and is the easiest way compared to tweet @abcdxyz'
emails=[]
# YOUR CODE HERE


# In[ ]:


assert len(emails)==1
assert emails[0]=='xyz@abcd.com'

