# data_clean_processing.py

class DataCleanProcessing:
    def __init__(self, data):
        self.data = data

    def clean_missing_values(self):
        # Fill missing values with median for numerical columns and mode for categorical columns
        for column in self.data.columns:
            if self.data[column].dtype == 'object':
                self.data[column].fillna(self.data[column].mode()[0], inplace=True)
            else:
                self.data[column].fillna(self.data[column].median(), inplace=True)
        return self.data

    def verify_no_missing_values(self):
        missing_values = self.data.isnull().sum().sum()
        print(f'Total missing values after cleaning: {missing_values}')
        return missing_values == 0