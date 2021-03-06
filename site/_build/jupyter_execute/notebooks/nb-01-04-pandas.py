#!/usr/bin/env python
# coding: utf-8

# [![AnalyticsDojo](https://github.com/rpi-techfundamentals/spring2019-materials/blob/master/fig/final-logo.png?raw=1)](http://rpi.analyticsdojo.com)
# <center><h1>Introduction to Python - Introduction to Pandas</h1></center>
# <center><h3><a href = 'http://rpi.analyticsdojo.com'>rpi.analyticsdojo.com</a></h3></center>
# 
# 

# # Introduction to Pandas
# - Pandas Overview
# - Series Objects
# - DataFrame Objects
# - Slicing and Filtering
# - Examples: Financial Data
# - Examples: Iris
# 

# ## Pandas Overview
# - Pandas is object-oriented.
# 
# - We create data frames by constructing instances of different classes.
# 
# - The two most important classes are:
# 
#     - `DataFrame`
#     - `Series`
#     
# - Pandas follows the Java convention of starting the name of classes with an upper-case letter, whereas instances are all lower-case.
# - The pandas module is usually imported with the alias `pd`.
# 

# In[ ]:


import pandas as pd


# ## Pandas (like the rest of Python) is object-oriented
# 
# - Pandas is object-oriented.
# 
# - We create data frames by constructing instances of different classes.
# 
# - The two most important classes are:
# 
#     - `DataFrame`
#     - `Series`
#     
# - Pandas follows the Java convention of starting the name of classes with an upper-case letter, whereas instances are all lower-case.
# 

# ## Pandas Series
# - One-dimensional array 
# - Series can be like array, with standard integer index starting at 0
# - Series can be dictionary like, with defined index 
# 

# In[ ]:


data = [1,2,3,4,5] #This creates a list
my_series = pd.Series(data) #array-like pandas series, index created automatically
my_series2 = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])  #dict like, index specified
print(my_series, '\n', my_series2)


# In[ ]:


my_series2['a']


# ## Plotting a Series
# 
# - We can plot a series by invoking the `plot()` method on an instance of a `Series` object.
# 
# - The x-axis will autimatically be labelled with the series index.
# 
# - This is the first time we are invoking a `magic` command. Read more about them [here](http://ipython.readthedocs.io/en/stable/interactive/magics.html). 

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
my_series.plot()


# ## Creating a Series from a `dict`
# 
# 

# In[ ]:


d = {'a' : 0., 'b' : 1., 'c' : 2.}
my_series = pd.Series(d)
my_series


# ## Indexing/Slicing a Series with `[]` or . notation
# 
# - Series can be accessed using the same syntax as arrays and dicts.
# - We use the labels in the index to access each element.
# - We can also use the label like an attribute `my_series.b`
# - We can specify a range with `my_series[['b', 'c']]`
# 
# 

# In[ ]:


#Notice the different ways that the parts of the series are specified. 
print( my_series['b'],'\n', my_series.b, '\n', my_series[['b', 'c']])


# ## Functions on Series
# 
# - We can perform calculations using the entire series similar to numpy.
# - Methods are called from within `np.Series`, for example np.Series.add
# - See a variety of series functions [here](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html) 
# 
# 

# In[ ]:


#These are just a variety of examples of operations on series.


starter = {'a' : 0., 'b' : 1., 'c' : 2.}

a = pd.Series(starter)
print('Print the entire array a: \n', a)

b1=10*a
print('Mulitiply by 10 directly:\n', b1)

b2=a.multiply(10)
print('Mulitiply by 10 using the function:\n', b2)

c1=a+b1
print('Add a and b together directly:\n', c1)

c2=pd.Series.add(a,b1) #Note we are calling the method of the series class. Numpy used us np.add
print('Add a and b together with a function:\n', c2)


suma=pd.Series.sum(a) #Note we are calling the method of the series class. Numpy used us np.add
print('sum all of a:\n', suma)


f=a**2  #This squares the value. 
print('square a:\n', f)
x = pd.Series({'a' : 0., 'b' : 1., 'c' : 2.})
y = pd.Series({'a' : 3., 'b' : 4., 'c' : 5.})
z = x+y
print('Add 2 series together:\n', z)


# ## Time Series
# - Time series models link specific times with rows.

# In[ ]:


dates = pd.date_range('1/1/2000', periods=5)
dates


# In[ ]:


time_series = pd.Series(data, index=dates)
time_series


# ## Plot Time Series
# - With a data and a value, the plot command can be used to provide quick visibility in the form of a line graph.

# In[ ]:


ax = time_series.plot()


# In[ ]:


type(time_series)


# In[ ]:


time_series


# ## DataFrames
# 
# - The `pandas` module provides a powerful data-structure called a data frame.
# 
# - It is similar, but not identical to:
#     - a table in a relational database,
#     - an Excel spreadsheet,
#     - a dataframe in R.
# 
# - A data frame has multiple columns, each of which can hold a *different* type of value.
# 
# - Like a series, it has an index which provides a label for each and every row. 
# 
# 
#     

# ## Creating a DataFrame from Outside Data
# - Data frames can be read and written to/from:
#     - database queries, database tables
#     - CSV files
#     - json files
#     - etc.
#     
# - Beware that data frames are memory resident;
#     - If you read a large amount of data your PC might crash
#     - With big data, typically you would read a subset or summary of the data via e.g. a select statement.

# ## Creating a DataFrame from Python Data Structures
# 
# - Data frames can be constructed from other data structures in memory:
#     - dict of arrays,
#     - dict of lists,
#     - dict of dict
#     - dict of Series
#     - 2-dimensional array
#     - a single Series
#     - another DataFrame

# 
# ## Example: Creating a DataFrame from Multiple Series
# - Pandas codes missing values as `NaN` rather than `None`
# - Series should have matching keys for each matching row.
# 

# In[ ]:


d = {
        'x' : 
            pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
        'y' : 
            pd.Series([4.,  6., 7.], index=['a',  'c', 'd']),
        'z' :
            pd.Series([0.2, 0.3, 0.4], index=[ 'b', 'c', 'd'])
}

df = pd.DataFrame(d)
print (df)


# In[ ]:


type(d)


# ## Plotting DataFrames
# 
# - When plotting a data frame, each column is plotted as its own series on the same graph.
# 
# - The column names are used to label each series.
# 
# - The row names (index) is used to label the x-axis.

# In[ ]:


ax = df.plot()


# In[ ]:


df


# ## Functions and DataFrames
# 
# - We can do calculations and functions with dataframes just like series.
# - Functions will typically return a dataframe or a series, depending. 
# - To make a copy, don't set two dataframes equal us the `copy` method:  `df2= df.copy()` 

# In[ ]:


#Info
nulls=df.isnull()
print(nulls, "\n", type(nulls))

nullsum=nulls.sum()

print("\nNull sum for each column \n", nullsum, "\n", type(nullsum))

print("\nWe can slice these results to get the answer for x \n", nullsum.x)
type(nullsum.x)


# In[ ]:


df2= df.copy()
print(df, '\n', df2)


# In[ ]:


df2=df ** 2 #This squares all values. 
print(df2)


# ## Summary statistics
# - To quickly obtain summary statistics on numerical values use the `describe` method.
# - You will get a warning if there are missing values.
# - The result is itself a DataFrame, that we can slice `dfstats.y['mean']`.

# In[ ]:


dfstats=df.describe()
dfstats
#type(dfstats)

#END HERE.....


# In[ ]:


xmean = dfstats.x['mean'] #This is the X mean
ystd = dfstats['y']['std'] #This is the Y standardard deviation
print(xmean,'\n',ystd)


# ## Data Types
# - Each will have an inferred data type. 

# In[ ]:


print(df.dtypes)


# ## Accessing the Row and Column Labels
# 
# - The row labels (index) can be accessed through `df.index`.
# - The column labels can be accessed through `df.columns`.
# 

# In[ ]:


df.index


# In[ ]:


df.columns


# In[ ]:


print(df.describe())


# ## Loading Files with Pandas
# - We used Pandas in an earlier notebook to load the iris data file.  
# - Whenver you have a dataset with a variety of fields of various types, loading it into Pandas is a good strategy.
# - You can load data from Azure, from a local file, or from a url.  
# 
# 
# 
# 
# 
# 

# In[1]:


get_ipython().system('wget https://raw.githubusercontent.com/rpi-techfundamentals/spring2019-materials/master/input/iris.csv')


# In[ ]:


# Pulling from a local file
frame2 = pd.read_csv('iris.csv')
frame2


# ##  Large Dataframes - Head and Tail
# 
# - Many times you just want a sampling of the available data
# - The `head()` command can view the start of a data frame.
# - The `tail()` command can be used to show the end of a data frame. 

# In[ ]:


frame2.head()


# In[ ]:


frame2.tail()


# In[ ]:


# Pulling from a url.  Notice that this is the raw version of the file.
frame3 = pd.read_csv("https://raw.githubusercontent.com/rpi-techfundamentals/spring2019-materials/master/input/iris.csv")
frame3.head()


# ## Indexing/Slicing Rows of DataFrames
# - Simple ways of selecting all rows and colu (`df[:]`)
# - Rows can be accessed via a key or a integer corresponding to the row number. 
# - Omitting a value generally means *all values* before or after an item.
# - When we retrieve a single or mulitiple rows, the result is a Dataframe.
# - Several ways, either directly, with `iloc`, or with `loc`. (See Examples).
# - Read more [here](http://pandas.pydata.org/pandas-docs/stable/indexing.html)
# 
# 

# In[ ]:


#This is going to create some sample data that we can work with for our analysis. 

import pandas as pd
import numpy as np
 
#Create a dataframe from a random numpy array 
#http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randn.html
df = pd.DataFrame((20+np.random.randn(10, 4)*5),  columns=['a', 'b', 'c', 'd'] )
print (df)
df2 = pd.DataFrame((20+np.random.randn(10, 4)*5),  columns=['e', 'f', 'g', 'h'] )
print (df2)


# ## Indexing/Slicing Columns of DataFrames
# - Simple ways of selecting colum(s) `frame[[colname(s)]]`. 
# - Columns can have one (`df['x']`) or multiple (`df[['x', 'y']]`) columns.
# - When specifying one column, one can use simplified dot notation `df.x`.
# - When we include multiple columns the slice that result is a DataFrame.
# - When we retrieve a single column, the result is a Series.
# - When we retrieve mulitiple column, the result is a Dataframe.
# 

# In[ ]:


#Here we can see that there is a similar structure to R, with selecting the desired columns by passing a list.

print (df[['c', 'd']]) #All rows, column c, d
print (df[[ 'c', 'd']]) #All rows, column c, d
print (df.iloc[:,[0,2,3]]) #All rows, column a,c,d
print (df.iloc[:,0:2])     #All rows, column a-b
print (df.iloc[:,[0,2,3]])     #All rows, column 0,2,3
print (df.loc[:,'a':'b']) #All rows, column a-b
print (df.loc[:,['a','c','d']]) #All rows, columns a, c, d


# ## Dropping Columns from Dataframes
# - Done using the `drop` syntax. 
# - [Drop Documentation](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop.html)

# In[ ]:


#Here, we can remove columns specifically from a dataframe using the drop method.
df2 = pd.DataFrame((20+np.random.randn(10, 4)*5),  columns=['e', 'f', 'g', 'h'] )
print (df2)
df2.drop(['e','f'], inplace=True, axis=1)
print (df2)


# ## Selecting Rows
# - Similarly, we also might want to select out rows, and we can utilize the same syntax.
# - [iloc](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.iloc.html)

# In[ ]:



## Selecting rows
print (df[0:3])     #Select rows 1-3
print (df.iloc[0:3,:])     #Select rows 1-3
print (df.iloc[0:3,])      #Select rows 1-3
print (df.iloc[0:3])       #Select rows 1-3
print (df.iloc[[1,2,4]])   #Select rows 1, 2, and 4


# ## Intro to Filters (Logical indexing)
# - Filters are the selection of rows based on criteria.
# - We can select based on specific criteria.
# - These criteria can be connected together.
# - Most of the time we won't specfically assign selection critia to a list. 

# In[ ]:


# At the foundation of the filter is a boolean array based on some type of condition. 
print(df)
df['a'] >= 20


# In[ ]:


#notice how the logical statement is inside the dataframe specification.  This creates an intermediate boolean array. 
df[df['a'] >= 20]


# In[ ]:


#This is an alternate method where we first set the boolean array. 
included=df['a'] >= 20
df[included]


# In[ ]:


#We can now generate a vector based on a critera and then use this for selection
select = df['a']>=20
print (select,type(select))
print (df.loc[select,'a']) #Notice by including only one variable we are selecting rows and all columns.

select2 = (df['a']>20) & (df['c'] < 30)  #More complex criteria
print (select2)
print (df.loc[select2,['a','c']])


# In[ ]:


#Here we are creating a new variable based on the value of another variable.
df['aboveavg']=0  # We first set the default to 0. 
df.loc[df['a']>=20,'aboveavg']=1 #We then change all rows where a is >=20 to 1.
print(df['aboveavg'])


# ## Joining Dataframes
# - Often you need to combine dataframe, 
# - either matching columns for the smae rows (column  bind)
# - Add rows for the same columns (row bind)

# ## Stacking Dataframes Vertically
# - Adds rows vertially with the `concat` function
# - The index is not automatically reset
# - In R referred to as a row bind.

# In[ ]:


#This first generates 2 dataframes. 
df = pd.DataFrame((20+np.random.randn(10, 4)*5),  columns=['a', 'b', 'c', 'd'] )
df2 = pd.DataFrame((20+np.random.randn(10, 4)*5),  columns=['a', 'b', 'c', 'd'] )

#This will stack the 2 dataframes vertically on top of one another
dfbyrow=pd.concat([df, df2])  #This is equivalent to a rowbind in R. 
print (dfbyrow)


# In[ ]:


# View how the index here from df has been reset and incremented while in the earlier example the index was kept. 

addition = df.append(df2)
print(addition )
addition2 = df.append(df, ignore_index=True)
print(addition2 )


# ## Inner/Outer Joins Dataframes
# - Adds rows vertially with the `concat` function
# - In R referred to as a column bind.
# - Can do the equivalent of an inner and outer join.

# In[ ]:


#Merging additional columns also uses the concat function 
#This is equavalent to an inner join in SQL.
df = pd.DataFrame((20+np.random.randn(10, 4)*5),  columns=['a', 'b', 'c', 'd'] )
df4 = pd.DataFrame((20+np.random.randn(10, 4)*5),  columns=['e', 'f', 'g', 'h'] )


dfbycolumns = pd.concat([df, df4], axis=1, join='inner')
dfbycolumns


# In[ ]:


#Here we are generating a small dataframe to be used in merging so you can see the differences in specifying inner & outer, 
shortdf=df[0:5]
dfbycolumns = pd.concat([df, shortdf], axis=1, join='inner')
dfbycolumns


# In[ ]:


#Here, the outer does the equivalent of a left outer join for this dataset. 
shortdf=df[0:5]
dfbycolumns = pd.concat([df, shortdf], axis=1, join='outer')
dfbycolumns


# Copyright [AnalyticsDojo](http://rpi.analyticsdojo.com) 2016.
# This work is licensed under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) license agreement.

# ## CREDITS
# 
# #### Large sections of this were adopted from Analysing structured data with Pandas by [Steve Phelps](http://sphelps.net).  Thanks Steve!
# 
# 
# This work is licensed under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) license agreement.
# 
# 

# In[ ]:




