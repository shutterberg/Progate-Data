import pandas as pd
import numpy as np
save="progate_data2.txt"
file1=open(save,"w+")
file="data_csv.csv"
df=pd.read_csv(file,index_col=0)
df['Certified']=0
df.loc[(df['Python']=='100%')|(df['Java']=='100%'),'Certified']=1
df.loc[(df['Python']=='100%')&(df['Java']=='100%'),'Certified']=2

df=df.copy()
print(df)
file1.write('Name               Number Of Certifications')
condict=df['Certified'].to_dict()
#file1.write(str(df['Certified']))
for x,y in condict.items():
    ster=x+'\t'+str(y)
    file1.write(str(ster))
    file1.write('\n')