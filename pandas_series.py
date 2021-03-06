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
fruits.dtype
# dtype('O')

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

fruits.nunique()
# 13

# 9. Determine the string value that occurs most frequently in fruits.
fruits.value_counts().nlargest(n=1, keep = 'all')
# kiwi    4
# dtype: int64

fruits.value_counts().idmax()
# 'kiwi'

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



# Exercises Part II
# Explore more attributes and methods while you continue to work with the fruits Series.

# 1. Capitalize all the string values in fruits.
fruits.str.capitalize()
# 0                 Kiwi
# 1                Mango
# 2           Strawberry
# 3            Pineapple
# 4           Gala apple
# 5     Honeycrisp apple
# 6               Tomato
# 7           Watermelon
# 8             Honeydew
# 9                 Kiwi
# 10                Kiwi
# 11                Kiwi
# 12               Mango
# 13           Blueberry
# 14          Blackberry
# 15          Gooseberry
# 16              Papaya
# dtype: object

# 2. Count the letter "a" in all the string values (use string vectorization).
fruits.str.count('a')
# 0     0
# 1     1
# 2     1
# 3     1
# 4     3
# 5     1
# 6     1
# 7     1
# 8     0
# 9     0
# 10    0
# 11    0
# 12    1
# 13    0
# 14    1
# 15    0
# 16    3
# dtype: int64

# 3. Output the number of vowels in each and every string value.
def count_vowels(listName):
    string = ''.join(listName)
    count = 0
    vowels = 'aeiouAEIOU'
    for ch in string:
        if ch in vowels:
            count += 1
    return count

fruits.apply(count_vowels)

# 0     2
# 1     2
# 2     2
# 3     4
# 4     4
# 5     5
# 6     3
# 7     4
# 8     3
# 9     2
# 10    2
# 11    2
# 12    2
# 13    3
# 14    2
# 15    4
# 16    3
# dtype: int64
# 4. Write the code to get the longest string value from fruits.
max(fruits.str.len())
#  16
fruits[fruits.str.len().idxmax()
#  'honeycrisp apple'

# 5. Write the code to get the string values with 5 or more letters in the name.
fruits[fruits.str.len() >= 5]
# 1                mango
# 2           strawberry
# 3            pineapple
# 4           gala apple
# 5     honeycrisp apple
# 6               tomato
# 7           watermelon
# 8             honeydew
# 12               mango
# 13           blueberry
# 14          blackberry
# 15          gooseberry
# 16              papaya
dtype: object

# 6. Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
fruits[fruits.apply(lambda m : m.count('o') >= 2)]
# 6         tomato
# 15    gooseberry
# dtype: object

# 7. Write the code to get only the string values containing the substring "berry".
fruits[fruits.str.contains('berry')]
# 2     strawberry
# 13     blueberry
# 14    blackberry
# 15    gooseberry
# dtype: object
# 8. Write the code to get only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]
# 3           pineapple
# 4          gala apple
# 5    honeycrisp apple
# dtype: object
# 9. Which string value contains the most vowels?
fruits[fruits.apply(count_vowels).idxmax()]
# 'honeycrisp apple'

# Exercises Part III
# Use pandas to create a Series named letters from the following string:

letters = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
ll = list(letters)
letters = pd.Series(11)

# 1. Which letter occurs the most frequently in the letters Series?
letters.value_counts().nlargest(1)
# y    13
# p    12
# w    10
# m     9
# b     9
# dtype: int64

# 2. Which letter occurs the Least frequently?
letters.value_counts().nsmallest()
# l    4
# g    5
# s    5
# i    5
# j    6
# dtype: int64
# 3. How many vowels are in the Series?
letters.apply(count_vowels).sum()
# 34

# 4. How many consonants are in the Series?
letters.str.count('[bcdfghjklmnpqrstvwxyz]').sum()
# 166

# 5. Create a Series that has all of the same letters but uppercased.
caps = letters.str.capitalize()
cap_ser = pd.Series(caps)

# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.
cap_ser.value_counts().head(6).plot.bar(color = 'orange', width =.5, ec = 'black')
plt.title('Question 6')
plt.grid(True, ls=':')
plt.xlabel('$Letters$', size = 12)
plt.ylabel('$Frequency$', rotation = 0, labelpad = 25)
plt.xticks(rotation = 0)
plt.show()

Use pandas to create a Series named numbers from the following list:

# 1. What is the data type of the numbers Series?
numbers.dtype
# dtype('O')

# 2. How many elements are in the number Series?
numbers.describe()
# count                20
# unique               20
# top       $4,338,283.54
# freq                  1
# dtype: object

# 3. Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.
numbers = numbers.str.replace('$', '').str.replace(',', '').astype(float)

# 4. Run the code to discover the maximum value from the Series.
numbers.max()
# 4789988.17

# 5. Run the code to discover the minimum value from the Series.
numbers.min()
# 278.6

# 6. What is the range of the values in the Series?
num_range = numbers.max() - numbers.min()
4789709.57

# 7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
pd.cut(numbers, 4)
pd.cut(numbers, 4).value_counts()
# (-4511.11, 1197705.993]       7
# (3592560.778, 4789988.17]     6
# (1197705.993, 2395133.385]    4
# (2395133.385, 3592560.778]    3
# dtype: int64

# 8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
pd.cut(numbers,4).value_counts(sort = False).plot.barh(color = 'olive', ec = 'black')

plt.title('Fancy Meaningful Chart')
plt.xlabel('$Quantity$')
plt.ylabel('$Range$', rotation = 0)
plt.grid(True, ls = ':')

plt.show()

# Use pandas to create a Series named exam_scores from the following list:

# 1. How many elements are in the exam_scores Series?
exam_scores.describe()
# count    20.000000
# mean     78.150000
# std      11.352139
# min      60.000000
# 25%      70.500000
# 50%      79.000000
# 75%      85.250000
# max      96.000000
# dtype: float64

# 2. Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
exam_scores.min()
# 60
exam_scores.max()
# 96
exam_scores.mean()
# 78.15
exam_scores.median()
# 79.0

# 3. Plot the Series in a meaningful way and make sure your chart has a title and axis labels.

# 4. Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.
curved_grades = exam_scores + 4
curved_grades
# 5. Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.
def letter_score(score):
        if score < 70:
            return 'F'
        elif score < 75:
            return 'D'
        elif score < 80:
            return 'C'
        elif score < 90:
            return 'B'
        elif score >= 90:
            return 'A'
        
letter_grades = curved_grades.apply(letter_score)
letter_grades
# 6. Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
pd.cut(exam_scores, [0,69,74,79,84,89,94,100]).value_counts(sort=False).plot.bar(color = 'green', ec = 'black', linewidth = 2)
plt.title('Exam Scores Histogram', color = 'maroon', fontsize = 16, weight = 'bold')
plt.xlabel('Letter Grade Range', color = 'olive', fontsize = 12, weight = 'bold')
plt.ylabel('Grade\nFrequency', color = 'olive', fontsize = 12, weight = 'bold', rotation = 0, labelpad = 50)
plt.grid(True, ls = ':')
plt.xticks([0,1,2,3,4,5,6], ['F', 'D', 'C', 'B', 'B+', 'A', 'A+'], color = 'olive', fontsize = 10, weight = 'bold', rotation = 0)

plt.show()
