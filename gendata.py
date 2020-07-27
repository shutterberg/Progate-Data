import pandas as pd
import numpy as np
file="data_csv.csv"
df=pd.read_csv(file,index_col=0)
save="progate_data.txt"
file=open(save,"w+")
python_names=df[df['Python']=='100%'].index.tolist()
file.write('----------------------------------------\n')
file.write("Python Only:")
file.write(str(len(python_names)))
for name in range (len(python_names)):
    file.write('\n')
    file.write(python_names[name])
    
java_names=df[df['Java']=='100%'].index.tolist()
file.write('\n----------------------------------------\n')
file.write("Java Only:")
file.write(str(len(java_names)))
for name in range (len(java_names)):
    file.write('\n')
    file.write(java_names[name])
both_names=df[(df['Java']=='100%')&(df['Python']=='100%')].index.tolist()
file.write('\n----------------------------------------\n')
file.write("Python and Java:")
file.write(str(len(both_names)))
for name in range (len(both_names)):
    file.write('\n')    
    file.write(both_names[name])
file.write('\n----------------------------------------\n')
file.write("Ranking")
rank=df.sort_values('Rank ',ascending=False).index.tolist()
for name in range (len(rank)):
    file.write('\n')
    ranking=str(name)+" "+rank[name]
    file.write(ranking)

