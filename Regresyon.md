Regresyon Nedir?
Regresyon, bağımlı bir değişken (çıktı) ile bir veya daha fazla bağımsız değişken (girdi) arasındaki ilişkiyi modelleyen denetimli (supervised) bir makine öğrenmesi tekniğidir.

Ne Zaman Kullanılır?
Çıktı değeri sürekli bir sayıysa (örneğin: ev fiyatı, sıcaklık, maaş tahmini)
Veriler arasında bir sebep-sonuç ilişkisi olduğunu düşünüyorsak
Geçmiş verilere bakarak tahmin yapmak istiyorsak

Doğrusal Regresyon (Linear Regression)
Bir veya daha fazla değişkenle, hedefi düz bir doğru (lineer ilişki) üzerinden tahmin eder.
Kullanım Örnekleri:
Ev fiyatı tahmini (alan, oda sayısı, konum)
Bir çalışanın maaşını tahmin etme (tecrübe yılına göre)

Dikkat Edilmesi Gerekenler:
Girdiler ile çıktı doğrusal bir ilişki göstermeli.
Aykırı değerler, modelin doğruluğunu bozabilir.
Özellikler arasında yüksek korelasyon (multicollinearity) varsa, model kararsız olabilir.
Verilerin ölçeklenmesi bazı durumlarda faydalı olabilir (özellikle Ridge/Lasso kullanılıyorsa).

Lojistik Regresyon (Logistic Regression)
Çıktının 0 veya 1 (evet/hayır, hasta/sağlıklı) gibi sınıflandırma problemlerinde kullanılır.
Lineer regresyondan farklı olarak, çıktıyı olasılık olarak hesaplar ve bir eşik değeriyle sınıfa karar verir.

Kullanım Örnekleri:
Bir e-postanın spam olup olmadığını tahmin etme
Bir müşterinin ürünü satın alıp almayacağını tahmin etme

Dikkat Edilmesi Gerekenler:
Çıktı kategorik olmalı (genellikle 0–1).
Özelliklerin ölçeklendirilmesi modelin daha iyi çalışmasını sağlar.
Aykırı değerler lojistik regresyonu da etkileyebilir.
Verilerdeki sınıf dağılımı dengesizse (örneğin çok fazla "0", az "1"), model yanlı olabilir → "class imbalance" sorununa dikkat edilmeli.

Farkları:
Doğrusal regresyon ve lojistik regresyon, her ikisi de denetimli öğrenme algoritmalarıdır; ancak farklı problemleri çözmek için kullanılırlar. Doğrusal regresyon, sürekli ve sayısal bir hedef değişkeni tahmin etmek amacıyla kullanılır. Örneğin, bir evin fiyatını alanına veya oda sayısına göre tahmin etmek gibi. Bu model, giriş değişkenleri ile hedef değişken arasında doğrusal bir ilişki olduğunu varsayar ve çıktı olarak gerçek bir sayı üretir. Öte yandan, lojistik regresyon bir sınıflandırma algoritmasıdır ve genellikle hedef değişkenin iki sınıftan birine ait olup olmadığını tahmin eder. Çıktı olarak bir olasılık üretir ve bu olasılığa göre sınıf belirler; örneğin, bir hastanın hasta olup olmadığını tahmin etmek gibi. Doğrusal regresyon düz bir çizgiyle ilişki kurarken, lojistik regresyon bu ilişkiyi sigmoid adı verilen S şeklinde bir eğriyle modeller. Bu temel fark, onları farklı problem türleri için uygun hale getirir.