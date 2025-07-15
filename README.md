# AcademyPatikaDev_Courses_Web_Scraping
# Patika Dersleri Web Scraper

Bu Python scripti, [Patika.dev](https://academy.patika.dev/paths) sitesindeki **ders** türündeki kursları otomatik olarak çekip Excel dosyasına kaydetmek için geliştirilmiştir.

---

## Özellikler

* Sitedeki `paths` sayfasından sadece **ders (course\_type = "ders")** türündeki kursları seçer.
* Her ders için:

  * Kurs adı
  * Puan (rating)
  * Kullanıcı sayısı
  * Puan değeri
  * Süre
  * Bağlantı (link)
  * Tip (ders)
* Aynı kurslar varsa tekrarları otomatik temizler.
* Veriyi Excel (`patika_dersler_temiz.xlsx`) olarak kaydeder.

## 📁 Örnek Çıktı

| Kurs Adı                 | Puan | Kullanıcı Sayısı | Puan Değeri | Süre    | Bağlantı                                                                                           | Tip  |
| ------------------------ | ---- | ---------------- | ----------- | ------- | -------------------------------------------------------------------------------------------------- | ---- |
| Python Programlama       | 4.8  | 15.000           | 1000 Puan   | 20 saat | [https://academy.patika.dev/courses/python](https://academy.patika.dev/courses/python)             | ders |
| Web Geliştirme Temelleri | 4.5  | 12.500           | 950 Puan    | 15 saat | [https://academy.patika.dev/courses/web-dev](https://academy.patika.dev/courses/web-dev)           | ders |
| Veri Bilimi Giriş        | 4.7  | 8.000            | 980 Puan    | 18 saat | [https://academy.patika.dev/courses/data-science](https://academy.patika.dev/courses/data-science) | ders |

---

## Gereksinimler

* Python 3.x
* Selenium
* Pandas
* Chrome WebDriver (bilgisayarınızda Chrome yüklü olmalı)

---

### Python Kütüphaneleri

Aşağıdaki komutla gerekli kütüphaneleri yükleyebilirsiniz:

```bash
pip install selenium pandas openpyxl
````

Sorun yaşarsanız sırayla kütüphaneleri yükleyiniz:

```bash
pip install selenium
````

```bash
pip install openpyxl pandas
````

---

## 🔧 Kurulum ve Kullanım

1. **ChromeDriver İndir**
   Mevcut Chrome tarayıcınızla uyumlu ChromeDriver sürümünü buradan indirin:
   [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)

2. **chromedriver.exe Dosyasını Yerleştir**
   `chromedriver.exe` dosyasını bu proje dizinine yerleştirin veya sistem PATH’inize ekleyin.

---

## Kullanım

1. Scripti çalıştırın:

```bash
python patika_scraper.py
```

2. Script, `https://academy.patika.dev/paths` sayfasını açar, dersleri toplar ve `academypatikadev_courses.xlsx` adlı dosyaya kaydeder.

3. Çalışma sonunda terminalde "✅ Yalnızca path-altı dersler kaydedildi." mesajı görünecektir.

---

## Dikkat Edilmesi Gerekenler

* Site yapısı değişirse script çalışmayabilir, element seçiciler güncellenmelidir.
* Script sayfanın yüklenmesi için `time.sleep(5)` kullanıyor, internet hızına göre artırılabilir.
* ChromeDriver versiyonu Chrome tarayıcı sürümünüzle uyumlu olmalıdır.

---

## 📌 Excel Düzenleme İpucu

Excel'deki veri görünümünü otomatik olarak düzgün hale getirmek için:

1. `Sheet1` sekmesine sağ tıklayın → **Kod Görüntüle** seçeneğine tıklayın.
2. Sol üstte açılan kod penceresinde `(General)` yazan yeri **Worksheet** olarak değiştirin.
3. Aşağıdaki kod satırını ekleyin:

```vba
Columns.AutoFit
```

4. `Ctrl + S` ile kaydedin ve dosyayı kapatın.
5. Şimdi Excel dosyanız açıldığında sütunlar otomatik olarak içeriklere göre hizalanmış olacaktır.

---

## İletişim

Herhangi bir sorun ya da öneri için bana ulaşabilirsiniz.

---

## 👨‍💻 Geliştirici

**Baran Hüseyin Kençü**
Otomasyon ve veri işleme tutkusu ile geliştirildi. 💻❤️
