import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# read data
file_loc = os.path.join('data', 'churn.csv')
df = pd.read_csv(file_loc)
X = df.iloc[:, 3:-1].values
y = df.iloc[:, -1].values

# encode GENDER col
le = LabelEncoder()
X[:, 2] = le.fit_transform(X[:, 2])

# encode COUNTRY col
ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(), [1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# scale data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# make model
model = Sequential()
model.add(Dense(units=6, activation='relu'))
model.add(Dense(units=6, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

# compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# train model
model.fit(X_train, y_train, batch_size=32, epochs=100)

# test data
y_pred = model.predict(X_test, batch_size=32)
y_pred = y_pred > 0.5
print(accuracy_score(y_test, y_pred))
