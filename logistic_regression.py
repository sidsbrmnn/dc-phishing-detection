from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import numpy

from decision_tree import load_data


def main():
    print("Training a logistic regression to detect phishing websites.")

    train_inputs, test_inputs, train_outputs, test_outputs = load_data()
    print("Training data loaded.")

    model = LogisticRegression(solver='lbfgs', max_iter=150)
    print("Logistic regression model created.")

    print("Beginning model training.")
    model.fit(train_inputs, train_outputs)
    print("Model training completed.")

    predictions = model.predict(test_inputs)
    print("Predictions on testing data computed.")

    accuracy = 100.0 * accuracy_score(test_outputs, predictions)
    print("Accuracy of logistic regression is:", accuracy)


if __name__ == '__main__':
    main()
