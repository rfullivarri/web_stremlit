import pandas as pd
import numpy as np

df= pd.read_csv(r"/Users/ramirofernandezdeullivarri/Documents/GitHub/web_stremlit/smarthome.csv")

filtro= df[(df["Category"]=="lights")&(df["Subcategory"]=="bathroom")]
count_on= (filtro["Action"]=="on").sum()
count_off= (filtro["Action"]).count()
print(filtro,"\n",count_on,"\n",count_off)
    

# filtro = (df["Category"]== "lights") & ( df["Subcategory"]=="kitchen" ) & ( df["Action"]=="on")
# cant_luces_prendidas= len(df[filtro])
# #print(cant_luces_prendidas)

# # listaa= df.columns

# # columns = [] 
# # for i in listaa:
# #     columns.append(i)
# # #print(columns)

# # for i in columns:
# #     i = df[str(i)].unique()
# #     print(i,"\n")

# print(df["Category"].unique(),"\n")
# print(df["Subcategory"].unique())