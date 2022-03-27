import pandas as pd

def disease_repo():
    # pd.set_option('display.max_rows', None)
    df = pd.read_csv("df_diseases.csv")
    df= df[["name","symptoms","treatment"]]
    #print(df)
    return df

# def treatment(disease_name):
#     data_two = disease_repo()
#     bad_chars = ["[","]","'"]
#     data_two = data_two.loc[data_two["name"]==disease_name]
#     data_two= data_two.to_dict()
#     data_two = list(data_two.values())[2]
#     data_two = list(data_two.values())[0]
#     for i in bad_chars:
#         data_two = data_two.replace(i,"")
#     return data_two