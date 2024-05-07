import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


# X -> numpy array of data
# encoder -> data encoder, for example, LabelEncoder, OneHotEncoder etc.
# cols -> list of columns to  encode
def encode_data(X, *args, encoder, cols=[]):
    X = X.copy()
    if isinstance(encoder, OneHotEncoder):
        transformer = ColumnTransformer(
            [("one_hot_enc", encoder, cols)], remainder="passthrough"
        )
        X = np.array(transformer.fit_transform(X))
        encoder = transformer

    else:
        if cols:
            for col in cols:
                X[:, col] = encoder.fit_transform(X[:, col])
        else:
            X = encoder.fit_transform(X)

    return {
        "X": X,
        "encoder": encoder,
    }
