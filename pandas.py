import pandas as pd


data = {
    "nama" : ["ali","siti","kumar","mei ling","aiman"],
    "markah" : [70,85,90,65,80]
}

df = pd.DataFrame(data)

print (df)

##data teratas
print(df.head())
print()

##nama pelajar sahaja
print(df["nama"])
print()

##markah sahaja
print(df["markah"])

purata = df["markah"].mean()
print (purata)

##tambah lajur status

df["status"] = np.where(df['markah']>= 66,"lulus","gagal")
print (df)

## tambah lajur grade


def tentukan_grad(markah):
    if markah >= 80:
        return "A"
    elif markah >= 65:
        return "B"
    elif markah >= 50:
        return "C"
    else:
        return "D"
df["grad"] = df["markah"].apply(tentukan_grad)


df.to_csv("markah_pelajar.csv",index=False)

print("Fail berjaya disimpan")
