import pandas as pd

class Dataset_Loader:

    def load_dataset(self, url: str, separador: str = ';'):
        return pd.read_csv(url, sep = separador)
    