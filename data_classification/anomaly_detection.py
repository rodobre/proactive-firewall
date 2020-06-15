import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import numpy as np
import random

class AnomalyDetection:
    def __init__(self, max_samples=256):
        self.max_samples = max_samples
        self.rng = np.random.RandomState(random.randint(0, 100))
        self.df = None
        self.x = None
        self.x_train = None
        self.x_test = None
        self.y_pred_train = None
        self.y_pred_test = None
        self.iso = None

    def train_test_split(self, x, coeff=0.2):
        margin = int(len(x) * 0.2)
        return (x[:margin], x[margin + 1:])

    def load_model(self, csv_file):
        self.df = pd.read_csv(csv_file)
        self.df = self.df.sample(frac=1)
        self.x = self.df.to_numpy()
        return self.x, self.df

    def train_forest(self):
        self.x_train, self.x_test = self.train_test_split(self.x)
        self.iso = IsolationForest(max_samples=self.max_samples, random_state=self.rng)
        self.iso.fit(self.x_train)
        self.y_pred_train = self.iso.predict(self.x_train)
        self.y_pred_test = self.iso.predict(self.x_test)

        accuracy_train = list(self.y_pred_train).count(-1) / self.y_pred_train.shape[0]
        accuracy_test  = list(self.y_pred_test).count(1) / self.y_pred_test.shape[0]

        return (self.y_pred_train, self.y_pred_test, accuracy_train, accuracy_test)

    def predict_data(self, data):
        return self.iso.predict(data)

'''
with open('plot.html', 'w') as site:
    site.write(df.corr().style.background_gradient(cmap='coolwarm').render())

import subprocess

subprocess.call(['C:\\Program Files\\Mozilla Firefox\\firefox.exe', 'plot.html'])

import plotly.express as ply
import plotly.graph_objects as plygo

fig = plygo.Figure(data = plygo.Scatter3d(x = x_test[:, 2], y = x_test[:, 6], z = x_test[:, 7], mode = "markers", marker_color=y_pred_test, text=y_pred_test))
fig.show()
'''

