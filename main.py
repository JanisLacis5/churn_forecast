# system installed packages
import os

# pip installed packages
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# custom functions
from functions import encode_data


# this code block will read data
file_loc = os.path.join("data", "churn.csv")  # create a path str to read from
df = pd.read_csv(file_loc)
X = df.iloc[
    :, 3:-1
].values  # this snippet allows selection of all rows and columns from index 3 to -1
y = df.iloc[:, -1].values  # same intention columns(0, -1)

# simply encodes Female -> 0 Males -> 1
label_enc = encode_data(
    X, encoder=LabelEncoder(), cols=[2]
)  # the gender column is indicated by index 2 (3 col)
# set X to transformed data
X = label_enc["X"]

# encode COUNTRY col
one_hot_encoder = encode_data(X, encoder=OneHotEncoder(), cols=[1])
# set X to transformed data
X = one_hot_encoder["X"]

# standard ml test-train split to create training and test data with a 80-20 split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)  # control param -> test_size: float = [0, 1]

# scale data
scaler = encode_data(
    X_train,
    encoder=StandardScaler(
        with_mean=True, with_std=True
    ),  # with_mean -> L1 normalization without L2
)
# set X_train to transformed data
X_train = scaler["X"]
# scale X_test with the same scaler that was used for X_train
X_test = scaler["encoder"].transform(X_test)

# make model
# we init a sequential network, add two dense layers where the convolution are relU and output layer is a sigmoid function, output: float = [0,1]
model = Sequential()
model.add(Dense(units=6, activation="relu"))
model.add(Dense(units=6, activation="relu"))
model.add(Dense(units=1, activation="sigmoid"))

# compile model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# train model
model.fit(X_train, y_train, batch_size=32, epochs=100)

# test data
y_pred = model.predict(X_test, batch_size=32)
y_pred = y_pred > 0.5
print(accuracy_score(y_test, y_pred))
