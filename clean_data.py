import pandas as pd
df = pd.read_csv("2025-yl-yaa_gore_rayl_sistemler_istasyon_bazl_yolcu_ve_yolculuk_saylar.csv", sep=";", encoding="utf-8-sig")
df = df.drop(columns=["longitude", "latitude", "station_number"])
df["date"]=pd.to_datetime(dict(year=df.transaction_year, month=df.transaction_month, day=df.transaction_day))
df["weekday"] = df["date"].dt.day_name()
df["is_weekend"] = df["date"].dt.weekday >= 5
bos_istasyon = df["station_name"].isna()
df.loc[bos_istasyon & (df["line"] == "T3-KADIKOY-MODA"), "station_name"] = "Kadıköy-Moda T3"
df.loc[bos_istasyon & (df["line"] == "IETT NOSTALJIK TRAMVAY"), "station_name"] = "Taksim-Tünel Nostaljik Tramvay"
df.loc[df["station_name"] == "ÇIRÇIR DOĞU", "town"] = "EyüpSultan"
df.loc[df["station_name"] == "KAZIMKARABEKİR", "town"] = "Gaziosmanpaşa"
df["age"] = df["age"].replace({"Unkown": "Bilinmiyor"})
yas_sirasi = ["<20", "20-30", "30-60", "60+", "Bilinmiyor"]
df["age"] = pd.Categorical(df["age"], categories=yas_sirasi, ordered=True)
df["line_code"] = df["line"].str.extract(r"^([A-Z]+\d+)")[0].fillna(df["line"])
df["line_code"] = df["line_code"].replace({
    "TCDD TASIMACILIK A.S.": "Marmaray",
    "TCDD - GAYRETTEPE-ISTANBUL YENI HAVALIMANI": "M11",
    })
df.to_csv("passenger_clean.csv", index=False, sep=";", encoding="utf-8-sig")
print("Kaydedildi:", df.shape)