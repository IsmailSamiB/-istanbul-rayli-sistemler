# İstasyon kullanım haritası

2025 yıllık yolcu sayılarını İstanbul raylı sistem istasyonları üzerinde gösteren etkileşimli harita.
Hat çizgileri OpenStreetMap'teki gerçek ray geometrisinden çizilir.

## Açmak

`istasyon_kullanim_haritasi.html` dosyasını tarayıcıda açmak yeterli (tek dosya, sunucu gerekmez;
sadece harita altlığı ve Leaflet için internet bağlantısı gerekir). VS Code'da *Live Server*
eklentisiyle de açılabilir.

## Yeniden üretmek

```bash
python harita/build_map.py            # önbellekteki OSM verisiyle
python harita/build_map.py --yenile   # OSM verisini Overpass API'den yeniden indir
```

Yalnızca Python standart kütüphanesi kullanılır, ek paket gerekmez.

## Dosyalar

| Dosya | Açıklama |
|---|---|
| `build_map.py` | OSM verisini indirir, hat geometrisini ayıklar/sadeleştirir, HTML'i üretir |
| `template.html` | Harita arayüzü (Leaflet); `__DATA__` ve `__ROUTES__` yer tutucuları doldurulur |
| `data/istasyonlar.json` | Düzeltilmiş istasyon verisi (ad, hat, ilçe, yıllık yolcu, koordinat, düzeltme notları) |
| `data/hatlar_osm.geojson` | Hat başına sadeleştirilmiş ray geometrisi (üretilir) |
| `data/osm_ham.json` | Overpass ham yanıtı, önbellek (git'e eklenmez) |
| `istasyon_kullanim_haritasi.html` | Üretilen harita |

Hat kodu → OSM rota ilişkisi eşlemesi `build_map.py` içindeki `HAT_ROTALARI` sözlüğündedir.
Bir hat için OSM geometrisi bulunamazsa harita o hattı istasyon sırasına göre düz çizgiyle çizer.

## Veri düzeltmeleri

Her istasyonun `fixes` alanı yapılan düzeltmeleri listeler; haritada ilgili istasyonun penceresinde
sarı kutuda görünür. Başlıcaları:

- Ad düzeltmeleri (ör. `15.tem` → 15 Temmuz, `Itü` → İTÜ-Ayazağa, eksik İ/Ü harfleri)
- Yanlış ilçe bilgileri
- Aynı istasyonun çift kaydı birleştirildi (T4 Kiptaş Venezia, M2 Seyrantepe)
- Hattından 140 m'den uzakta kalan 9 istasyon OSM durak noktasına taşındı
  (en büyüğü M9 Ataköy, ~800 m), M5 Yamanevler koordinatı düzeltildi

## Kaynaklar

- Yolcu sayıları: İBB Açık Veri Portalı
- Ray geometrisi ve durak noktaları: © OpenStreetMap katkıcıları (ODbL)
- Altlık: Esri World Gray Canvas
