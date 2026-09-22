import pandas as pd

sefer = pd.read_excel("rayl-sistemler-hat-bazl-sefer-saylar.xlsx")

sefer_uzun = sefer.melt(id_vars="Tarih", var_name="line_code", value_name="sefer_sayisi")
sefer_uzun = sefer_uzun.dropna(subset=["sefer_sayisi"])
sefer_uzun["sefer_sayisi"] = sefer_uzun["sefer_sayisi"].astype(int)
sefer_uzun["year"] = sefer_uzun["Tarih"].dt.year
sefer_uzun["month"] = sefer_uzun["Tarih"].dt.month
sefer_uzun.to_csv("trips_clean.csv", index=False, sep=";", encoding="utf-8-sig")
print("Kaydedildi:", sefer_uzun.shape)