from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import numpy


def load_data():
    data = numpy.genfromtxt(
        'dataset.csv', delimiter=',', dtype=numpy.int32)

    x = data[:, :-1]
    y = data[:, -1]

    xTrain, xTest, yTrain, yTest = train_test_split(
        x, y, test_size=0.2, random_state=0)

    return xTrain, xTest, yTrain, yTest


def main():
    print("Training a decision tree to detect phishing websites.")

    train_inputs, test_inputs, train_outputs, test_outputs = load_data()
    print("Training data loaded.")

    classifier = tree.DecisionTreeClassifier()
    print("Decision tree classifier created.")

    print("Beginning model training.")
    classifier.fit(train_inputs, train_outputs)
    print("Model training completed.")

    predictions = classifier.predict(test_inputs)
    print("Predictions on testing data computed.")

    accuracy = 100.0 * accuracy_score(test_outputs, predictions)
    print("Accuracy of decision tree is:", accuracy)


if __name__ == '__main__':
    main()
