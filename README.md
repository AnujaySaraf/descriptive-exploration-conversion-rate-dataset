# Conversion Rate Dataset

### Question 1
#### Write a function to convert given CSV file to Dataframe
* Define function with name `csv_to_dataframe` which should accept `filepath` as a parameter.
* Function should return a dataframe.
* As we require a dataframe, type of return variable should be pandas dataframe.
* In case if we pass `filepath` which does not exist, function should raise FileNotFoundError.

### Question 2
#### Write a function to convert datatype of given variables to "category"
* Define function with name `dtype_category` which should accept `dataframe` and `list of columns` as parameters.
* Function should return a dataframe with type of given columns changed to "category".
* As we require a dataframe, type of return variable should be `pandas dataframe`.
* In case if we pass column name which does not exist, function should raise KeyError

### Question 3
#### Write a function to count number of "categorical variables"
* Define function with name `categorical_variable_count` which should accept `dataframe` as parameter.
* Function should return count of categorical variables.
* As we require count, type of return variable should be integer.
* In case if we pass dataframe which does not exist, function should raise NameError

### Question 4
#### Write a function to check variance of numeric columns of a dataframe, and if variance is lower than given threshold, drop the column
* Define function with name `var_ckeck` which should accept `dataframe`, `threshold` (int) as parameter.
* Function should drop the the rejected columns and return a list of dropped variables.
* As we require list, type of return variable should be list.

### Question 5
#### Write a function to plot Q-Q plots of all numeric variables
* Define function with name `q_q_plot` which should accept `dataframe`, `column_list` (of variables to be plotted) as parameters.
* Function should return plots of numeric variables.
* As we require plot, type of return variable should be matplotlib object.
* In case if we pass column name which does not exist, function should raise KeyError

### Question 6
#### Write a function to build a Logistic Regression model
* Define function with name `logistic_regression_model` which should accept `dataframe`, `dependent_variable` (as string) and `independent_variable_list` (as a list of columns) as parameters.
* Function should return accuracy of the model in %.
* As we require accuray, type of return variable should be numeric.
* In case if we pass column name which does not exist or is not numerical type, function should raise KeyError