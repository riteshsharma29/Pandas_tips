import pandas as pd

'''
Splitting delimeter(, ; | etc) separated values into multiple rows with multiple columns data
'''

df = pd.read_excel("data.xlsx",sheet_name='setII')
# split 'Annual Budget' column into multiple rows with multi index
df_new = (df.set_index(['Department','Mananger','Senior Manager'])
   .stack()
   .str.split(',', expand=True)
   .stack()
   .unstack(-2)
   .reset_index(-1, drop=True)
   .reset_index()
)

# sort df_new dataframe as per previous schema
df_original = df_new[['Department','Annual Budget','Mananger','Senior Manager']]
print(df_original)
df_original.to_excel("setII_Output.xlsx",index=False)
