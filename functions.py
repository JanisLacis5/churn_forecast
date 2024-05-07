import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


# X -> numpy array of data
# encoder -> data encoder, for example, LabelEncoder, OneHotEncoder etc.
# cols -> list of columns to  encode
def encode_data(X, *args, encoder, cols=[]):
    # make copy of given data array X
    X = X.copy()

    # check if encoder given is OneHotEncoder and if it is, use ColumnTransformer
    if isinstance(encoder, OneHotEncoder):
        transformer = ColumnTransformer(
            [("one_hot_enc", encoder, cols)], remainder="passthrough"
        )

        # set array X to transformed data
        X = np.array(transformer.fit_transform(X))

        # set encoder to ColumnTransformer object for return
        encoder = transformer

    else:
        # if there is columns list given then iterate over each column and perform encoding
        if cols:
            for col in cols:
                X[:, col] = encoder.fit_transform(X[:, col])
        # if there is no cols list given then encoder is always StandardScaler => perform scaling on the whole data array X
        else:
            X = encoder.fit_transform(X)

    return {
        "X": X,  # transformed data array X
        "encoder": encoder,  # encoder if the same encoder needs to be used again (anly use case for encoder return is for StandardScaler)
    }
