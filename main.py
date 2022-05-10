import os

import fire as fire
import pandas as pd


class Breaker(object):
    @staticmethod
    def divide_chunks(lst, number):
        for i in range(0, len(lst), number):
            yield lst[i:i + number]

    def breaker(self, path, col):
        file_name_no_ext = os.path.splitext(path)[0]
        df = pd.read_excel(path, header=None, names=['temp_col'])

        print("Dividing columns...")
        divided_columns_list = list(self.divide_chunks(list(df.temp_col), col))
        new_df = pd.DataFrame(divided_columns_list).transpose()

        print("Writing to file..")
        new_df.to_excel(f'{file_name_no_ext}_result.xlsx', index=False, header=False)

        print("Breaking complete.")


if __name__ == '__main__':
    fire.Fire(Breaker)
