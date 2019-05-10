# Detecting phishing websites using a decision tree

This repository contains the code for a phishing detector model using a decision tree for a mini project in [phishing](https://en.wikipedia.org/wiki/Phishing). Typically, phishing websites disguise as trustworthy websites in order to gain the trust of their victims, and malicious parties use them to obtain sensitive information from their victims: e.g., passwords or credit card numbers. In this tutorial, we train a decision tree to detect such websites, with a success rate of 96%.

## Installation

To get started, you should first clone this repository by running the following command from a terminal.

```
git clone https://github.com/sidsbrmnn/dc-phishing-detection
```

This will download the code that trains the phishing detector, as well as the training data required for that operation.

You should also install `scikit-learn`, which is a collection of tools for machine learning written in Python.

```
pip install -U scikit-learn
```

Once you have installed `scikit-learn`, you can check whether the library is correctly setup by typing the following in a Python shell:

```
import sklearn
```

If the command runs with no error, you are ready to train the phishing detector!

## Phishing Website Dataset

The dataset was collected by analyzing a collection of `11055` websites among which some were used for phishing and others not. For each website included in the dataset, `31` attributes are given. You can find a list [here](https://github.com/sidsbrmnn/dc-phishing-detection/blob/master/features.md). The list includes for instance the URL length, whether the website uses pop-up windows or i-frames, or how old the domain registration is.

Each website in the dataset is labeled by `-1` if it is not a phishing website and by `1` if it is a website used for phishing.

## Training the decision tree to detect phishing website

You can find the code that trains the decision tree in the [`decision_tree.py`](https://github.com/sidsbrmnn/dc-phishing-detection/blob/master/decision_tree.py) file. To run the code, simply execute it in a terminal:

```
py decision_tree.py
```

This will first train the decision tree on 80% of the dataset, then use the trained model to predict whether the remaining 20% websites are used for phishing or not (these websites were not analyzed during training). The model should make predictions that are about 96% correct, i.e. the accuracy of the model on the testing data should be 96%. Here is a dump of the output made by the script.

```
Training a decision tree to detect phishing websites.
Training data loaded.
Decision tree classifier created.
Beginning model training.
Model training completed.
Predictions on testing data computed.
Accuracy of decision tree is:  96.42695612844867
```

## Questions or suggestions

If you have any questions or suggestions, feel free to send me an email at [`sidsbrmnn@gmail.com`](mailto:sidsbrmnn@gmail.com).
