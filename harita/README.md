## İstasyon kullanım haritası

İstasyon Kullanım Haritası

Bu proje, İstanbul'daki raylı sistem istasyonlarının 2025 yılı yolcu sayılarını etkileşimli bir harita üzerinde gösterir. Hat güzergâhları, OpenStreetMap'ten alınan gerçek ray geometrileri kullanılarak çizilmiştir.

Altlık: Esri World Gray Canvas (açık/koyu tema).  
Kaynaklar: Yolcu verileri İBB Açık Veri Portalı; ray geometrileri ve durak noktaları © OpenStreetMap katkıcıları (ODbL).

## Haritayı çalıştırma

`istasyon_kullanim_haritasi.html` dosyasını tarayıcıda açmanız yeterli. Harita herhangi bir sunucuya ihtiyaç duymadan çalışır. Yalnızca harita altlığı ve Leaflet için internet bağlantısı gerekir.

İsterseniz projeyi VS Code'daki **Live Server** eklentisiyle de çalıştırabilirsiniz.

## Haritayı yeniden oluşturma

Haritayı mevcut OSM verileriyle yeniden oluşturmak için:

```bash
python harita/build_map.py
```

OSM verilerini Overpass API'den yeniden indirmek isterseniz:

```bash
python harita/build_map.py --yenile
```

Projede yalnızca Python'un standart kütüphanesi kullanılıyor. Bu nedenle çalıştırmak için ek bir Python paketi kurmaya gerek yok.

## Dosyalar

| Dosya | Açıklama |
|---|---|
| `build_map.py` | OSM verilerini alır, ray geometrilerini ayıklar ve sadeleştirir, ardından harita HTML'ini oluşturur. |
| `template.html` | Haritanın Leaflet arayüzünü içerir. Veriler ve hat geometrileri oluşturma sırasında şablona eklenir. |
| `data/istasyonlar.json` | İstasyon adı, hat, ilçe, yıllık yolcu sayısı, koordinat ve yapılan düzeltmeler gibi bilgileri içerir. |
| `data/hatlar_osm.geojson` | Hatlara ait sadeleştirilmiş ray geometrilerini içerir. Harita oluşturulurken üretilir. |
| `data/osm_ham.json` | Overpass API'den alınan ham OSM verilerinin önbelleğidir. Git'e eklenmez. |
| `istasyon_kullanim_haritasi.html` | Kullanıma hazır etkileşimli harita. |

Hat kodlarının OSM'deki güzergâhlarla eşleştirmesi `build_map.py` içindeki `HAT_ROTALARI` sözlüğünde bulunuyor.

Bir hat için OSM'de uygun bir ray geometrisi bulunamazsa, harita o hattı istasyonların sırasını takip eden düz çizgilerle gösterir.

## Veri düzeltmeleri

İstasyon verilerinde yapılan düzeltmeler her istasyonun `fixes` alanında tutuluyor. Bu bilgiler haritada istasyon seçildiğinde sarı bir kutu içerisinde gösteriliyor.

Veri üzerinde yapılan başlıca düzeltmeler:

- İstasyon adlarındaki yazım hataları düzeltildi. Örneğin `15.tem` → `15 Temmuz`, `Itü` → `İTÜ-Ayazağa` ve eksik Türkçe karakterler.
- Yanlış ilçe bilgileri düzeltildi.
- Aynı istasyona ait birden fazla kayıt birleştirildi. Örneğin T4 Kiptaş Venezia ve M2 Seyrantepe.
- Hat güzergâhından 140 metreden fazla uzak kalan 9 istasyonun koordinatları OSM'deki durak noktalarına göre düzeltildi.
- Bu düzeltmeler arasındaki en büyük fark M9 Ataköy'de yaklaşık 800 metreydi.
- M5 Yamanevler'in koordinatı da ayrıca düzeltildi.

## Kaynaklar

- **Yolcu verileri:** İBB Açık Veri Portalı
- **Ray geometrileri ve durak noktaları:** © OpenStreetMap katkıcıları (ODbL)
- **Harita altlığı:** Esri World Gray Canvas
