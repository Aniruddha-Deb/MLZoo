import pandas as pd
import numpy as np

def create_sets():

    train_set = [1,2,3]
    test_set = [4,5]

    train_csvs = [f'gt_201{i}.csv' for i in [1,2,3]]
    test_csvs = [f'gt_201{i}.csv' for i in [4,5]]

    all_csvs = train_csvs + test_csvs

    df = pd.read_csv(all_csvs[0])

    for csv in train_csvs[1:]:
        df_t = pd.read_csv(csv)
        df = pd.concat([df,df_t])

    n_train = len(df)

    for csv in test_csvs:
        df_t = pd.read_csv(csv)
        df = pd.concat([df,df_t])

    df = df.reset_index()
    df = df.drop(['index'],axis=1)
    df.index.name = 'SNO'

    train_df = df.iloc[:n_train,:]
    test_df = df.iloc[n_train:,:]

    train_df.to_csv("train.csv")
    test_df.drop(['CO','NOX'],axis=1).to_csv("test.csv")
    test_df[['CO','NOX']].to_csv("test_results.csv")

if __name__ == "__main__":
    create_sets()