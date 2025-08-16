import pandas as pd
from ucimlrepo import fetch_ucirepo

class DataHandler:

    def __init__(self, dataset_id: int, parquet_file: str = "dataset.parquet"):
        self.dataset_id = dataset_id
        self.parquet_file = parquet_file
        self.data = None

    def fetch_data(self):
        dataset = fetch_ucirepo(id=self.dataset_id)
        X = dataset.data.features
        y = dataset.data.targets

        self.data = pd.concat([X, y], axis=1)

    def save_as_parquet(self):
        self.data.to_parquet(self.parquet_file, index=False)

class DataAnalyzer:

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def compute_statistics(self):
        stats = {}
        for col in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[col]):
                stats[col] = {
                    "Max": self.df[col].max(),
                    "Min": self.df[col].min(),
                    "Average": self.df[col].mean(),
                    "AbsoluteSum": self.df[col].abs().sum()
                }
        #return pd.DataFrame(stats)
        return pd.DataFrame(stats).T  # Transpose for better readability



def main():
    # Step 1: Fetch and save dataset
    handler = DataHandler(dataset_id=320, parquet_file="student_performance.parquet")
    handler.fetch_data()
    handler.save_as_parquet()

    # Step 2: Analyze numeric columns with foreach
    analyzer = DataAnalyzer(handler.data)
    stats = analyzer.compute_statistics()

    # Display results
    print("Dataset Statistics :")
    print(stats)

if __name__ == "__main__":
    main()