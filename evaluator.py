import pandas as pd

def evaluate_numeric(output_file, answer_file):

    out_df = pd.read_csv(output_file).set_index('SNO')
    ans_df = pd.read_csv(answer_file).set_index('SNO')

    MSE = (out_df-ans_df)**2

    print("RMSE:")
    print(MSE.pow(0.5).mean(axis=0))