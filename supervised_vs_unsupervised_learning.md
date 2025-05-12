# 🧠 Denetimli ve Denetimsiz Öğrenme

Makine öğrenmesi (Machine Learning), verilerden otomatik olarak öğrenen algoritmalar geliştirmeyi amaçlar.  
Öğrenme sürecinin yapısına göre modeller genellikle iki temel gruba ayrılır:  
**Denetimli öğrenme (Supervised Learning)** ve **Denetimsiz öğrenme (Unsupervised Learning)**.

---

## ✅ Denetimli Öğrenme (Supervised Learning)

Denetimli öğrenmede, algoritmaya verilen veriler hem **girdi (X)** hem de **etiketlenmiş çıktı (Y)** içerir.  
Model, bu örneklerden öğrenerek yeni veriler için tahmin yapmayı öğrenir.  
Tahmin veya sınıflandırma problemlerini çözmek için kullanılır.

### 🔧 Yaygın Algoritmalar:
- Doğrusal Regresyon
- Lojistik Regresyon
- Karar Ağaçları
- KNN
- Destek Vektör Makineleri (SVM)

### 📌 Kullanım Örnekleri:
- Ev fiyat tahmini (regresyon)
- Bir e-postanın spam olup olmadığını tahmin etme (sınıflandırma)
- Görüntüdeki nesneleri tanıma (kedi mi köpek mi?)

### ⚠️ Dikkat Edilmesi Gerekenler:
- Veri **etiketli** olmalıdır (etiketlenmiş veri toplamak zaman alabilir).
- Eğitim verisinin kalitesi modelin başarısını doğrudan etkiler.
- Aykırı değerler veya dengesiz sınıflar, öğrenmeyi bozabilir.

---

## 🔍 Denetimsiz Öğrenme (Unsupervised Learning)

Denetimsiz öğrenmede veriler **etiketsizdir**.  
Model, verilerdeki **gizli desenleri**, **gruplamaları** veya **dağılım yapısını** kendi başına keşfetmeye çalışır.  
Veri keşfi, segmentasyon, boyut indirgeme gibi problemler için kullanılır.

### 🔧 Yaygın Algoritmalar:
- K-Means Kümeleme
- Hiyerarşik Kümeleme
- Principal Component Analysis (PCA)
- DBSCAN

### 📌 Kullanım Örnekleri:
- Müşteri segmentasyonu (benzer alışveriş davranışlarına göre gruplama)
- Sosyal medya kullanıcılarını etkileşimlere göre sınıflandırma
- Boyut indirgemeyle görselleştirme

### ⚠️ Dikkat Edilmesi Gerekenler:
- Etiketli veri olmadığından sonuçlar yorumlamaya açıktır.
- Kümeleme algoritmalarında **k** gibi bazı parametrelerin dikkatli seçilmesi gerekir.
- Gerçek hayattaki anlamlı grupları bulmak bazen zordur.

---

## 🔄 Kıyaslama

Denetimli öğrenme, elimizde **doğru cevaplar (etiketler)** olduğunda net tahminler yapmak için kullanılır.  
Denetimsiz öğrenme ise etiketlerin **olmadığı** durumlarda verinin yapısını anlamaya yönelik kullanılır.  
Hangi yöntemin kullanılacağı, sahip olduğun veri yapısına ve çözmek istediğin probleme göre değişir.
"""