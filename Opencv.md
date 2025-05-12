# 📚 OpenCV Nedir?

**OpenCV (Open Source Computer Vision Library)**, gerçek zamanlı görüntü işleme ve bilgisayarla görme uygulamaları geliştirmek için kullanılan açık kaynaklı bir Python kütüphanesidir.

---

## 🔍 Ne İşe Yarar?

OpenCV ile aşağıdakiler yapılabilir:
- Görüntü ve video analizi
- Kamera kullanımı
- Nesne tanıma ve takip
- Renk uzayı dönüşümleri
- Kenar ve kontur algılama
- Şekil çizimi ve metin ekleme
- Filtreleme ve bulanıklaştırma
- Görüntü boyutlandırma, döndürme, çevirme

---

## ⚙️ Kurulum

```bash
pip install opencv-python

# 🧩 Temel Fonksiyonlar (OpenCV)

| Fonksiyon               | Açıklama |
|-------------------------|----------|
| `cv2.imread()`          | Görüntü dosyasını okur |
| `cv2.imshow()`          | Görüntüyü pencere içinde gösterir |
| `cv2.imwrite()`         | Görüntüyü diske kaydeder |
| `cv2.VideoCapture()`    | Kamera veya video dosyasından görüntü alır |
| `cv2.waitKey()`         | Tuş bekler |
| `cv2.destroyAllWindows()` | Tüm pencereleri kapatır |
| `cv2.cvtColor()`        | Renk uzayı dönüşümü yapar (örneğin RGB → GRAY) |
| `cv2.resize()`          | Görüntü boyutlandırır |
| `cv2.flip()`            | Görüntüyü döndürür (flip eder) |
| `cv2.Canny()`           | Kenar algılama yapar |
| `cv2.findContours()`    | Kontur bulur |
| `cv2.drawContours()`    | Konturları çizer |
| `cv2.getRotationMatrix2D()` | Döndürme matrisi oluşturur |
| `cv2.warpAffine()`      | Görüntüyü affine dönüşümle döndürür |

