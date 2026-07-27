import matplotlib.pyplot as plt
import pandas as pd


markah = np.array([70, 85, 90, 65, 80])
print(markah)

data = {
    "nama" : ["ali","siti","kumar","mei ling","aiman"],
    "markah" : [70,85,90,65,80]
}
print("Purata markah:", purata)

tertinggi = np.max(markah)
print("Markah tertinggi:", tertinggi)

terendah = np.min(markah)
print("Markah terendah:", terendah)

jumlah = np.sum(markah)
print("Jumlah markah:", jumlah)

markah_baru = markah + 5
print(markah_baru)

plt.bar(df["nama"], df["markah"])
plt.title("Markah Pelajar")
plt.xlabel("Nama Pelajar")
plt.ylabel("Markah")
plt.show()

plt.plot(df["nama"], df["markah"], marker="o")
plt.title("Prestasi Markah Pelajar")
plt.xlabel("Nama Pelajar")
plt.ylabel("Markah")
plt.show()

plt.hist(df["markah"], bins=5)
plt.title("Taburan Markah Pelajar")
plt.xlabel("Julat Markah")
plt.ylabel("Bilangan Pelajar")
plt.show()

jumlah_gred = df["grad"].value_counts()
plt.pie(
jumlah_gred,
labels=jumlah_gred.index,
autopct="%1.1f%%"
)
plt.title("Peratusan Gred Pelajar")
plt.show()
