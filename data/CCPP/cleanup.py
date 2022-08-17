#!/usr/bin/env python

import pandas as pd

if __name__ == "__main__":
    df = pd.read_excel("Folds5x2_pp.xlsx")
    df.to_csv("output.csv", index=None)
