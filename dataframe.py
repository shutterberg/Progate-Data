import pandas as pd
import numpy as np
file="data_csv.csv"
df=pd.read_csv(file,index_col=0)
#all names are printed in list format
python_names=df[df['Python']=='100%'].index.tolist()
print("Python Only:",len(python_names))
print(python_names)
java_names=df[df['Java']=='100%'].index.tolist()
print("Java Only:",len(java_names))
print(java_names)
both_names=df[(df['Java']=='100%')&(df['Python']=='100%')].index.tolist()
print("Python and Java:",len(both_names))
print(both_names)
print("Ranking")
rank=df.sort_values('Rank ',ascending=False).index.tolist()
print(rank)