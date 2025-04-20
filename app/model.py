import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

def train_model():
    iris = load_iris()
    X = iris.data
    y = iris.target
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    return model, iris.feature_names

model, feature_names = train_model()