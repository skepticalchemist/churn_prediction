import matplotlib as plt
import pandas as pd
import numpy as np
import sklearn.metrics as metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.model_selection import learning_curve
from sklearn.tree import DecisionTreeClassifier



def model_eval(y_test, y_pred):
    f1 = f1_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    acc = accuracy_score(y_test, y_pred)

    print(f"F1 score:  {round(f1, 4)}"),
    print(f"Precision: {round(precision, 4)}"),
    print(f"Recall:    {round(recall, 4)}"),
    print(f"Accuracy:  {round(acc, 4)}"),

    return


def plot_learning_curve(X, y, maxdepth, plt):
    # create cv training and test scores for various training set sizes
    train_sizes, train_scores, test_scores = learning_curve(
    DecisionTreeClassifier(max_depth=maxdepth, random_state=42),
    X,  # feature matrix
    y,  # target vector
    cv=5,  # number of folds in cross-validation
    scoring="f1",  # metric
    #scoring="neg_mean_squared_error",  # metric
    n_jobs=-1,  # use all computer cores,
    train_sizes=np.linspace(
        0.01, 1.0, 30
        ),  # 30 different sizes of the training set
        )
    # create means and standart deviations of training set scores
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)

    # create means and standart deviations of test set scores
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)

    # draw lines
    plt.plot(train_sizes, train_mean, "--", color="#111111", label="Training score")
    plt.plot(train_sizes, test_mean, color="#111111", label="Cross-validation score")
        
    # draw bands
    plt.fill_between(
        train_sizes, train_mean - train_std, train_mean + train_std, color="#DDDDDD"
        )
    plt.fill_between(
        train_sizes, test_mean - test_std, test_mean + test_std, color="#f4d0d7"
        )

    # create plot
    plt.title("Learning curve for Decision Tree")
    plt.xlabel("Training set size", fontsize=18)
    plt.ylabel("F1 score", fontsize=18)
    plt.legend(loc="best")
    plt.tight_layout()

    return