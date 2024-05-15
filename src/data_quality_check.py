# data_quality_check.py

import pandas as pd

class DataQualityCheck:
    def __init__(self, file_path, sep='|'):
        self.file_path = file_path
        self.sep = sep
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path, sep=self.sep, low_memory=False)
        return self.data

    def basic_info(self):
        if self.data is not None:
            print(self.data.head())
            print(self.data.shape)
            print(self.data.info())
        else:
            print("Data not loaded. Please load the data first using load_data method.")