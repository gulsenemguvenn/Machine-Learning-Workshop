# 🤖 Machine Learning (Makine Öğrenmesi) Nedir

Makine öğrenmesi, bilgisayarların geçmiş verilerden veya deneyimlerden öğrenerek gelecekteki verilerle ilgili tahminlerde bulunmasını ya da kararlar almasını sağlayan bir yapay zeka (AI) tekniğidir.
Bilgisayarlar çok sayıda örnek veriyi analiz ederek aralarındaki desenleri öğrenir ve bu desenlere dayanarak yeni durumlar karşısında tahmin yapabilir veya karar verebilir.

---

## 📚 Machine Learning Türleri

### ✅ Supervised Learning (Denetimli Öğrenme)
- Etiketli verilerle eğitilir.
- Girdi (X) ve çıktı (Y) bellidir.
- Örnek: Maaş, yaş gibi verilere bakarak "terfi alır mı?" sorusuna yanıt aranması.
- Örnek algoritmalar: Logistic Regression, Decision Trees, SVM

### ✅ Unsupervised Learning (Denetimsiz Öğrenme)
- Etiketli olmayan verilerle eğitilir.
- Sadece giriş verisi vardır, etiket (çıktı) yoktur. Veri gruplandırılır.
- Örnek: K-Means, PCA

### ✅ Reinforcement Learning (Pekiştirmeli Öğrenme)
- Ajan, bir ortamda ödül veya ceza alarak öğrenir.
- Örnek: Oyun oynayan yapay zekâlar

---

## 🌐 Sanal Ortam (Virtual Environment) Nedir ve Neden Kurarız?

Python projeleri için bağımsız çalışma ortamları oluşturur.  
Böylece her proje kendi bağımlılıklarını izole biçimde kullanır.

**Neden Gerekli:**  
- Kütüphane çatışmalarını engeller  
- Proje taşınabilirliğini artırır

**Kullanım:**
```bash
python -m venv env
pip install virtualenv

# 🧰 Makine Öğrenmesinde Sık Kullanılan Kütüphaneler

- **pandas** : Veri analizi ve manipülasyon
- **numpy** : Sayısal işlemler, matris hesaplamaları
- **matplotlib** : Grafik ve görselleştirme
- **scikit-learn** : ML algoritmaları, preprocessing, model değerlendirme
- **tensorflow / keras** : Derin öğrenme modelleri
- **opencv** : Görüntü işleme

---

# 📁 Dosya İşlemleri

## 🔹 open() Fonksiyonu

Dosya açmak için kullanılır. Kullanım modları:

- `"r"` – Read (sadece okuma)
- `"w"` – Write (yazma, varsa içeriği siler!)
- `"a"` – Append (dosyanın sonuna ekleme)
- `"x"` – Create (sadece yeni dosya oluşturur)
- `"b"` – Binary mod
- `"t"` – Text mod (varsayılan)
"""

# 📄 Dosya Okuma ve Yazma İşlemleri

### 🔹 Okuma Fonksiyonları
- `read()` : Tüm içeriği string olarak okur.
- `readline()` : Bir satır okur.
- `readlines()` : Tüm satırları liste olarak döner.

### 🔹 Yazma Fonksiyonları
- `write()` : Dosyaya veri yazmak için kullanılır. Sadece `str` türü alır.
  - `"w"` modu: Dosyayı baştan yazar. Mevcut veriler silinir.
  - `"a"` modu: Dosyanın sonuna ekleme yapar (append).
- `writelines()` : Liste veya iterable içindeki tüm stringleri sırasıyla dosyaya yazar.

---

### 📌 Dosya Kapatma

- `close()` : Dosyayı kapatır. (Bellekte yer kaplamaması için gereklidir.)
- `with open(...) as ...:` : Dosya işlemlerinde otomatik kapanma sağlar.  
  Avantajı: `close()` çağırmaya gerek kalmaz, dosya otomatik kapanır.

---

# 📁 os Modülü

Dosya ve klasör işlemleri için kullanılır:

```python
import os

os.mkdir("klasor")            # Yeni klasör oluşturur
os.remove("dosya.txt")        # Dosya siler
os.rename("a.txt", "b.txt")   # Dosya adını değiştirir
os.rmdir("klasor")            # Klasörü siler
os.path.exists("dosya.txt")   # Dosya var mı kontrol eder
os.path.isdir("klasor")       # Bu bir klasör mü?

# 📦 JSON Modülü

**Tanım:**  
Sözlük yapısını `.json` dosyasına yazmak ve okumak için kullanılır.

### 🔹 json.dump()
Bir Python nesnesini JSON formatına çevirip doğrudan bir dosyaya yazmak için kullanılır.

---

# ⚠️ try-except Bloğu

**Tanım:**  
Dosya işlemleri sırasında oluşabilecek hataları (örneğin: dosya bulunamadı, izin yok gibi) yakalayarak programın çökmesini önler.

---

# 🐼 Pandas Kütüphanesi

**Pandas**, Python'da veri analizi ve veri manipülasyonu için kullanılan güçlü ve esnek bir kütüphanedir.  
Verileri **tablolar (DataFrame)** ve **seriler (Series)** şeklinde işler.

---

## 🔧 Kurulum
```bash
pip install pandas

---

# 🐼 Pandas Fonksiyonları ile Veri İşleme

Pandas, veri analizi ve temizleme işlemlerinde yaygın olarak kullanılan fonksiyonlara sahiptir. Aşağıda temel işlevler listelenmiştir:

---

## 📄 Temel Fonksiyonlar

- `pd.DataFrame()` : Veri seti oluşturmak için kullanılır (satır/sütun yapısında tablo).
- `head()` : Veri setinin ilk 5 satırını gösterir.
- `info()` : Veri seti hakkında genel bilgi verir (sütun tipi, eksik değerler, bellek kullanımı vb.).
- `isnull()` + `sum()` : Eksik değerleri kontrol etmek için kullanılır. Her sütundaki eksik veri sayısını verir.
- `fillna()` : Eksik verileri doldurur.
- `dropna()` : Eksik verileri içeren satırları siler.

---

## 🔢 Kategorik Verileri Sayısala Çevirme

- `LabelEncoder` : Kategorik verileri sayılara dönüştürür.
- `pd.get_dummies()` : One-Hot Encoding uygular; kategorik sütunları ayrı sütunlara bölerek 0-1 ile ifade eder.

---

## 📏 Veri Ölçeklendirme

- `StandardScaler` : Sayısal verileri aynı ölçeğe getirir. Modelin daha sağlıklı öğrenmesini sağlar.

---

## 🔀 Veri Setini Bölme

- `train_test_split()` : Veriyi eğitim ve test olarak ikiye böler. Genelde %80 eğitim, %20 test oranı kullanılır.

---

## 🔁 Dönüşümler

- `fit_transform()` : Veriye uyum sağlar ve dönüştürür. (eğitim verisinde kullanılır)
- `transform()` : Daha önce öğrenilen ölçekte sadece dönüştürme işlemi yapar. (test veya yeni verilerde kullanılır)


---


Bağımsız Değişken : Modelin tahmin yapmak için kullandığı girdi verisidir.
Bağımlı Değişken : Bu girdiye bağlı olarak tahmin edilmek istenen çıktıdır.

Veri ölçeklendirme : Farklı büyüklüklerdeki verileri ortak bir ölçeğe getirerek makine öğrenmesi algoritmalarının daha doğru ve verimli çalışmasını sağlamaktır.
Verileri neden ölçeklendiririz? Bazı algoritmalar veri büyüklüklerinden etkilenir. Ölçek farklılıkları modelin doğru çalışmasını engeller. 
Verileri ölçeklendirmezsek ne olur ? Büyük veriler küçük verileri ezer , model yanlış öğrenir ya da hiç öğrenmez , özellikle mesafe temelli algortimalar kötü sonuç verir. 

Verileri ölçeklendirdikten sonra eğitim ve test olarak ayırırız.(%80 eğitim , % 20 test)

Rastgele işlem (random process): Zaman içinde değişen ve gelecekteki değerleri yalnızca olasılıklarla tahmin edilebilen, belirsiz bir süreçtir. Modelin sonuçlarının sabit kalması isteniyorsa random_state verilmelidir.

---

Prediction(tahmin) : Model eğitildikten sonra yeni verilerle sonuç üretilmesine prediction denir.

random_state: Rastgelelik içeren işlemlerde (örneğin, veri bölme veya model eğitimi) aynı sonuçları elde edebilmek için rastgele sayı üretecinin başlangıç değerini sabitleyen bir parametredir.

Kategorik verileri sayısala çevirmek için, genellikle etiket kodlama (Label Encoding) veya tek sıcaklık kodlama (One-Hot Encoding) yöntemleri kullanılır.
Label Encoding: Her kategoriyi bir sayıya dönüştürür. Örneğin, "Kırmızı", "Mavi", "Yeşil" kategorilerini 0, 1, 2 olarak kodlar.
One-Hot Encoding: Her kategori için ayrı bir sütun oluşturur ve sadece o kategorinin olduğu yerde 1, diğerlerinde 0 değerini atar.

train_test_split: scikit-learn kütüphanesindeki bir fonksiyondur ve veri kümesini eğitim (training) ve test (testing) setlerine ayırmak için kullanılır. Genellikle modelin eğitimi ve değerlendirilmesi için veri kümesinin bir kısmı eğitim, geri kalan kısmı ise test verisi olarak ayrılır.

fit_transform : scikit-learn gibi kütüphanelerde, bir modelin veya dönüşüm işleminin hem eğitim (fit) hem de dönüşüm (transform) adımlarını aynı anda gerçekleştiren bir fonksiyondur. Örneğin, veriyi standartlaştırma işlemi yaparken önce verinin özelliklerini öğrenir (fit) ve ardından bu özelliklere göre dönüşüm yapar (transform).