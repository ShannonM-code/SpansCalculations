# Written by: Shannon Murray
# Last edited: April 25, 2021
# Description: Implements linear algorithms to compute the spans with a stack.

# Importing Pandas to make reading from excel files easy
# Pandas will return a data frame object which can be used
# to access columns, rows, or entire sheets in excel
# https://www.datacamp.com/community/blog/python-pandas-cheat-sheet?
# utm_source=adwords_ppc&utm_campaignid=12492439679&utm_adgroupid=122563407481&
# utm_device=c&utm_keyword=pandas%20cheat%20sheet&utm_matchtype=b&utm_network=
# g&utm_adpostion=&utm_creative=504158802862&utm_targetid=aud-392016246653:kwd-
# 385658525885&utm_loc_interest_ms=&utm_loc_physical_ms=9007733&gclid=CjwKCAjwmv-
# DBhAMEiwA7xYrd0UoZ3rFW-UyLNswZ57d2kcZU6_2_TYVKUyUW0ORQRhrPxjVzBRmIRoCTA0QAvD_BwE
#

import pandas as pd
import matplotlib.pyplot as plt


# Define a stack class
class ArrayStack:

    def __init__(self):
        # Create an empty stack.
        self._data = []  # nonpublic list instance

    def __len__(self):
        # Return the number of elements in the stack.
        return len(self._data)

    def is_empty(self):
        # Return True if the stack is empty.
        return len(self._data) == 0

    def push(self, e):
        # Add element e to the top of the stack.
        self._data.append(e)  # new item stored at end of list

    def top(self):
        # Return (but do not remove) the element at the top of the stack.

        # Raise Empty exception if the stack is empty.

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]  # the last item in the list

    def pop(self):
        # Remove and return the element from the top of the stack (i.e., LIFO).

        # Raise Empty exception if the stack is empty.

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()  # remove last item from list


class Empty(Exception):
    # Error attempting to access an element from an empty container.
    pass


# Define a function for calculating the spans
def spans(c):
    # Obtain the length of c
    n = len(c)

    # Create an array with the n + 1 elements and an empty stack
    # with the first index pushed onto the stack
    s = [0]*(n+1)
    a = ArrayStack()
    a.push(0)

    # The first span value is always 1
    s[0] = 1

    # Loop through the closing prices to calculate the spans.
    # Starting at 1 up until the last element n.
    for i in range(1, n):
        # Evaluate while the stack is not empty
        # and the top is less than the closing price
        while len(a) > 0 and c[a.top()] <= c[i]:
            # Remove an element from the stack
            a.pop()

        # If the stack becomes empty, this means that c[i]
        # is greater than all other closing prices in the array
        # and the index is equal to the span value plus 1
        if len(a) <= 0:
            s[i] = i + 1
        # If the stack is not empty, c[i] is greater than the
        # closing prices after the top of the stack
        else:
            s[i] = i - a.top()

        # Push the element to the stack
        a.push(i)

    return s


# Define a function for finding the max
def maximum(c):
    # assign the first element as the maximum value
    max_element = c[0]

    # Loop through the array and find the maximum
    # by comparing the elements and reassigning
    # max_element as needed
    for i in range(1, len(c)):
        if c[i] > max_element:
            max_element = c[i]

    return max_element


# Define a function for finding the minimum. Similar to
# the maximum function
def minimum(c):
    # Make the first element the minimum
    min_element = c[0]

    # Loop through the array and find the minimum
    # by comparing each element
    for i in range(1, len(c)):
        # Compare each element and reassign minimum
        # as needed
        if c[i] < min_element:
            min_element = c[i]

    return min_element


# Create the list of column names
col_list = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

# Read closing prices from Excel file based on the column names.
df = pd.read_csv('C:/Users/mymus/OneDrive/Documents/ESIOT/Spring 2021/ENEB 355/'
                 'SpansofInvesco/QQQ_52weeks.csv', usecols=col_list)

# Make sure data waS successfully read
print('Data from the excel file:')
print(df)
print()

# Assign the closing values to an array
closing = df['Close']

# Find the maximum and minimum
weeks_high = maximum(closing)
weeks_low = minimum(closing)


# Pass the array to the function to calculate the spans
sp = spans(closing)

# Print the spans
for j in range(0, len(closing)):
    print(sp[j], end=" ")

print()
print('52 Week High: ', weeks_high, '\tSpan: 215')
print('52 Week Low: ', weeks_low, '\tSpan: 1')

# Plot the spans
plt.plot(sp)

# Add titles and labels
plt.title("Spans vs Days")
plt.xlabel("Days")
plt.ylabel("Spans")

# Add 52 week high and 52 week low
# The 52 week high is 336.45 which occurs at
# the 216th row of the excel sheet
# So the span would be 215
plt.annotate('52 Week high', (215, 216), color='green')

# The 52 week low occurs at the very first entry
plt.annotate('52 Week low', (1, 1), color='red')

# Show the graphs
plt.show()
