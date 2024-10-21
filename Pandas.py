import pandas as pd

df = pd.read_csv("pokemon_data.csv")

# print(df.head(3))
# print(df.columns)
# print(df[['Name','Type 1']])
# print(df.iloc[2,1])

print(df.sort_values("Name"))

df["Total"]=df["HP"]+df["Attack"]+df["Defense"]+df["Sp. Atk"]+df["Sp. Def"]+df['Speed']
print(df.columns)

# df=df.drop(columns=["Total"])
# print(df.columns)

df["Total"] = df.iloc[:,4:10].sum(axis=1)
print(df.head(5))

cols=list(df.columns.values)
df=df[cols[0:4]+[cols[-1]]+cols[4:12]]

df.head(5)

df.to_csv("modified.csv")

# filtered_df=df.loc[(df['Type 1']=='Grass')&(df['Type 2']=='Poison')]
filtered_df=df.loc[~df["Name"].str.contains("Mega")]
print(filtered_df.head(5))

df=pd.read_csv("modified.csv")
df.groupby(['Type 1']).mean().sort_values("Defense", ascending=False)