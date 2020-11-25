"""Helper functions.

@author Zhenye Na 05/21/2018

"""

import numpy as np
import pandas as pd



def read_NDX(input_path, debug=True):
    """Read nasdaq stocks data.

    Args:
        input_path (str): directory to nasdaq dataset.

    Returns:
        X (np.ndarray): features.
        y (np.ndarray): ground truth.

    """
    df = pd.read_csv(input_path, nrows=250 if debug else None)
    # X = df.iloc[:, 0:-1].values
    X = df.loc[:, [x for x in df.columns.tolist() if x != 'NDX']].values
    # y = df.iloc[:, -1].values
    y = np.array(df.NDX)

    return X, y
