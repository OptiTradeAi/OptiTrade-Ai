
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from joblib import dump

class ModelTrainer:
    def __init__(self):
        self.model = LogisticRegression()

    def train(self, features, labels):
        self.model.fit(features, labels)
        accuracy = accuracy_score(labels, self.model.predict(features))
        return accuracy

    def save_model(self, path='core/trained_model.joblib'):
        dump(self.model, path)
