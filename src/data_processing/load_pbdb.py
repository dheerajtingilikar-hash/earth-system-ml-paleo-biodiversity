import pandas as pd

def load_pbdb(path):
    df = pd.read_csv(path, low_memory=False)
    return df