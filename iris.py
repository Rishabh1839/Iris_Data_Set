# iris demo
# np as alias to reference it in code
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

# importing the iris data set
iris_data_set = load_iris()

# printing out information for the user
print("=" * 70)
print("This is the Iris Data Set which is used to classify 3 types of flowers.")
print("This data set has 150 rows and 50 rows for each flower to classify.")
print("These rows are in a sequential order.")
print("The rows ranging from 0-49 is Setosa.")
print("The rows ranging from 50-99 is Versicolor.")
print("The rows ranging from 100-149 is Virginica.")

# print out the features in the data set
print("=" * 70)
print("Here are 4 different Features of the flower names")
print(iris_data_set.feature_names)

# lets print out the labels such as flower names
print("=" * 70)
print("Here are 3 different Labels of the flower names")
print(iris_data_set.target_names)

# A peek towards our data
# A peek towards the first row of the data
print("=" * 70)
print("This is the data of the 4 features that includes the sequential data set of ")
print("sepal width/length and petal width/length")
print(iris_data_set.data[0])

# A peek towards our data set for the labels
print("=" * 70)
print("Shows the label for 0.")
print("==========Label Table==========")
print("0 = setosa 1 = versicolor 2 = virginica")
print("Label =", iris_data_set.target[0])

print("=" * 70)
print("The full data set to reference: ")
for i in range(len(iris_data_set.target)):
    print("Example %d: label %s: Features %s:" % (i, iris_data_set.target[i], iris_data_set.data[i]))
