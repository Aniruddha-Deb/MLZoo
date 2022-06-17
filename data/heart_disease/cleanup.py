#!/usr/bin/env python

import pandas as pd
import numpy as np

def create_sets():

    df = pd.read_csv('processed.cleveland.data', header=None)
    df.columns = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num']
    df['num'] = np.where(df['num'] > 0,1,0)
    df = df.loc[(df['ca'] != '?') & (df['thal'] != '?')]
    df = df.reset_index()
    df = df.drop('index',axis=1)
    df.index.name = 'SNO'

    df.to_csv('cleveland.csv')

if __name__ == "__main__":
    create_sets()