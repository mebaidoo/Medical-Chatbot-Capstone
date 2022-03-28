import pandas as pd

def disease_repo():
    # pd.set_option('display.max_rows', None)
    df = pd.read_csv("df_diseases.csv")
    df= df[["name","symptoms","treatment"]]

    #print(df)
    return df
