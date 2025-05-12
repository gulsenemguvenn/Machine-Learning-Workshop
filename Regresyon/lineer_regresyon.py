import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

print("\n Veri Seti Oluşturuluyor...")

data = {
    "TV": [230,44,17,151,180,8,57,120,100,220],
    "Radio": [37,39,45,41,10,2,20,35,15,23],
    "Newspaper": [69,45,78,20,15,10,25,14,50,20],
    "Sales": [22,10,9,18,19,5,8,15,12,21]
}

df = pd.DataFrame(data)

print("Lineer Regresyon Veri Seti:")
print(df.head())

print("\n Veri Eğitim ve Test Setine Ayrılıyor....")

x = df[["TV","Radio","Newspaper"]]
y = df["Sales"]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2,random_state=42)

print(f"Eğitim Seti Boyutu: {x_train.shape}")
print(f"Test Seti Boyutu: {x_test.shape}")

print("\nLineer Regresyon Modeli Eğitiliyor...")

model = LinearRegression()

model.fit(x_train,y_train)

print("\n Lineer Regresyon Modeli Eğitildi!")
print("Katsayılar:")
print(model.coef_)
print(f"Intercept(b0): {model.intercept_}")

print("\n Model Test Verisi ile Tahmin Yapıyor...")

y_pred = model.predict(x_test)

print("\n Gerçek vs Tahmin Edilen Değerler:")
for gerçek, tahmin in zip(y_test, y_pred):
    print(f"Gerçek: {gerçek:.2f} -> Tahmin: {tahmin:.2f}")

print("\n Model Performansı Değerlendirliyor...")

mse = mean_squared_error(y_test, y_pred)

r2 = r2_score(y_test,y_pred)

print("\n Model Performans Sonuçları:")
print(f"MSE: {mse:.4f}")
print(f"r2 Skoru: {r2:.4f}")

print("\n Model Tahminleri Görselleştiriliyor...")

plt.scatter(y_test,y_pred,color='blue')
plt.xlabel("Gercek Degerler")
plt.ylabel("Tahmin Edilen Degerler")
plt.title("Lineer Regresyon: Gercek vs Tahmin")
plt.grid(True)

plt.savefig("lineer_regresyon_sonucu.png")