import pandas as pd


def readxl():
    df = pd.read_excel(io='readToRead.xlsx')
    df_len = len(df)
    df_len -=1
    while df_len >= 0:
        print(f".... removing {df['max_date'][df_len]} from DF")
        df = df.drop([df_len])
        print('.... removed')
        df_len -=1
    


