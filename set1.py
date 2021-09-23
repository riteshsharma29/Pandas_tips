import pandas as pd

'''
Splitting delimeter(, ; | etc) separated values into multiple rows with only 2 columns data
'''

df = pd.read_excel("data.xlsx",sheet_name='setI')
df_new = df['Annual Budget'].str.split(',',expand=True).set_index(df['Department']).stack().reset_index(level=0,name='Annual Budget')
df_new = df_new.reset_index(drop=True)[['Department','Annual Budget']]
print(df_new)
df_new.to_excel("setI_Output.xlsx",index=False)