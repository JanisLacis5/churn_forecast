import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer


# X -> numpy array of data
# encoder -> data encoder, for example, LabelEncoder, OneHotEncoder etc.
# cols -> needed if
def encode_data(X, *args, encoder, cols=[], col_range=()):
    if cols:
        transformer = ColumnTransformer(
            [("transformer", encoder, cols)], remainder="passthrough"
        )
        return {
            "X": np.array(transformer.fit_transform(X)),
            "transformer": transformer,
        }
