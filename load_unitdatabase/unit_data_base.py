# coding=utf-8
import pandas as pd
import os


class UnitDataBase:
    CURRENT_DIRECTORY = os.getcwd()

    def __init__(self, filename=None):
        self.filename = filename

    def load_excel(self):
        """
        Excel読み込み
        """
        index_list = ['Variation', 'test', 'ROM', 'Type', 'Path']
        excel_file_path = os.path.join(self.CURRENT_DIRECTORY, self.filename)
        df = pd.read_excel(excel_file_path, sheet_name=0, header=2, index_col=2)
        df.columns = index_list
        return df

    @staticmethod
    def filter_dataframe_range(df, variation):
        """
        データフレームをバリエーションで絞り込む
        """
        print(df['Variation'][0:5])
