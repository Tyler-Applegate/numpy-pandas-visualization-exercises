# Exercises Part I
# Make a file named pandas_series.py or pandas_series.ipynb for the following exercises.

import pandas as pd

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# Use Series attributes and methods to explore your fruits Series.

# 1. Determine the number of elements in fruits.
fruits.shape
# (17,)
fruits.size
#  17

# 2. Output only the index from fruits.
fruits.index
# RangeIndex(start=0, stop=17, step=1)

# 3. Output only the values from fruits.
fruits.values
# array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
    #    'honeycrisp apple', 'tomato', 'watermelon', 'honeydew', 'kiwi',
    #    'kiwi', 'kiwi', 'mango', 'blueberry', 'blackberry', 'gooseberry',
    #    'papaya'], dtype=object)

# 4. Confirm the data type of the values in fruits.
type(fruits.values)
# numpy.ndarray

# 5. Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
fruits.head(5)
# 0          kiwi
# 1         mango
# 2    strawberry
# 3     pineapple
# 4    gala apple
# dtype: object

fruits.tail(3)
# 14    blackberry
# 15    gooseberry
# 16        papaya
# dtype: object

fruits.sample(2)
# 8      honeydew
# 2    strawberry
# dtype: object

# 6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.
fruits.describe()
# count       17
# unique      13
# top       kiwi
# freq         4
# dtype: object

# 7. Run the code necessary to produce only the unique string values from fruits.
fruits.unique()
# array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
    #    'honeycrisp apple', 'tomato', 'watermelon', 'honeydew',
    #    'blueberry', 'blackberry', 'gooseberry', 'papaya'], dtype=object)

# 8. Determine how many times each unique string value occurs in fruits.
fruits.value_counts()
# kiwi                4
# mango               2
# blueberry           1
# blackberry          1
# honeycrisp apple    1
# pineapple           1
# strawberry          1
# honeydew            1
# gooseberry          1
# papaya              1
# watermelon          1
# tomato              1
# gala apple          1
# dtype: int64

# 9. Determine the string value that occurs most frequently in fruits.
fruits.value_counts().nlargest(n=1, keep = 'all')
# kiwi    4
# dtype: int64

# 10. Determine the string value that occurs least frequently in fruits.
fruits.value_counts().nsmallest(n=1, keep = 'all')
# blueberry           1
# blackberry          1
# honeycrisp apple    1
# pineapple           1
# strawberry          1
# honeydew            1
# gooseberry          1
# papaya              1
# watermelon          1
# tomato              1
# gala apple          1
# dtype: int64