#make an api call: will allow to get and read json data from an api call
# https://www.alphavantage.co/documentation/
import json, requests, datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# create a function to ask a user to pick a stock symbol
def get_stock_symbol():
    # give user a choice
    stock_symbols = ['Apple: APPL', 'Microsoft: MSFT', 'International Business Machines: IBM', 'Natural Gas: NG']
    # use a for loop to print out choices to user
    for stock in stock_symbols:
        print(stock)
    # ask user which symbol they wante
    stock_choice = input('Type in the stock symbol you want')
    # apply all caps to user input
    stock_choice = stock_choice.upper()
    return stock_choice
#make code reusable. function = reuable code so you don't need to keep writing the same thing over again.
# apply user choice to make a custom api call
def create_url(symbol):
    #api key
    api_token = "AH2JFP3LQ9R00HZX"
    #api call (request info from api) and url
    #url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=MSFT&apikey=demo'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol='+symbol+'&interval=1min&apikey='+api_token
    print(url)    #call data
    data = requests.get(url).json()

    meow = data["Monthly Time Series"]
    return meow
#taking the dictionary, parsing it (y = dictionary) and sorting for "2. high" only
def parse_high(data):
    # create a list
    parsed_data = []
    for x,y in data.items():
        # add y to list
        parsed_data.append(y['2. high'])
        #print(y['2. high'])
    # return list
    return parsed_data
def parse_low(data):
    # create a list
    parsed_data = []
    for x,y in data.items():
        # add y to list
        parsed_data.append(y['3. low'])
        #print(y['2. high'])
    # return list
    return parsed_data


# main program by calling funcitons
#user_choice is taking the symbol, user_call is calling the data which user chose, parse_data is taking it and sorting it
#print(parse_data) is printing the parsed data, "2. high" in this case
user_choice = get_stock_symbol()
user_call = create_url(user_choice)
high_data = parse_high(user_call)
low_data = parse_low(user_call)

#print out data
#print(high_data)
#print(low_data)

# https://github.com/kyle1james/mlc_2018/blob/master/homework_py3%20(1).ipynb

# Create x and y variables as linear arrays
X = high_data
y = low_data

# transform x,y from string to int
X = list(map(float, X))
y = list(map(float, y))

# import scikit-learn
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression





#how we want it to look on the linear regression

#printing coefficiants

lm = LinearRegression()

# transform data
X = np.array(X).reshape((len(X), 1))
y = np.array(y)

# train our data: half data for predictions and half for training the compairson
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)


# Fit Data
lm.fit(X_train, y_train)


predictions = lm.predict(X_test)
#print(predictions)

# ** Create a scatterplot of the real test values versus the predicted values. **
plt.scatter(y_test,predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.show()
# Plot a histogram of the residuals and make sure it looks normally distributed
sns.distplot((y_test-predictions),bins=50)
plt.show()
