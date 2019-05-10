import tensorflow as tf
from tensorflow import keras

import numpy

from decision_tree import load_data


def main():
    print("Training a logistic regression to detect phishing websites.")

    train_inputs, test_inputs, train_outputs, test_outputs = load_data()
    print("Training data loaded.")

    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(31, activation=tf.nn.relu),
        tf.keras.layers.Dense(150, activation=tf.nn.relu),
        tf.keras.layers.Dense(100, activation=tf.nn.relu),
        tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)
    ])

    print("Neural network model created.")
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    print("Beginning model training.")

    model.fit(train_inputs, train_outputs, epochs=30)
    print("Model training completed.")

    scores = model.evaluate(test_inputs, test_outputs)
    accuracy = scores[1]*100
    print("Accuracy of logistic regression is:", accuracy)


if __name__ == '__main__':
    main()
