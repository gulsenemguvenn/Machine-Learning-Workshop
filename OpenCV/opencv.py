import cv2
import numpy as np

# Görüntüyü Yükleme ve Gösterme
img = cv2.imread("ornek.jpg")
cv2.imshow("Orijinal Goruntu", img)

# Görüntü Boyutunu Öğrenme
print("Boyut:", img.shape)

# Görüntüyü Griye Tonlama
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gri Goruntu", gray)

# Görüntüyü Çevirme (flip)
flip_y = cv2.flip(img, 0)  # Dikey
flip_x = cv2.flip(img, 1)  # Yatay
cv2.imshow("Dikey Cevirme", flip_y)
cv2.imshow("Yatay Cevirme", flip_x)

# Görüntü Boyutlandırma
resized = cv2.resize(img, (300, 300))
cv2.imshow("Yeniden Boyutlandirilmis", resized)

# Görüntüyü Döndürme
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, matrix, (w, h))
cv2.imshow("Dondurulmus", rotated)

# Görüntü Kanallarını Ayırma
b, g, r = cv2.split(img)
cv2.imshow("Mavi Kanal", b)
cv2.imshow("Yesil Kanal", g)
cv2.imshow("Kirmizi Kanal", r)

# Renk Kanallarını Değiştirme
merged = cv2.merge([r, g, b])
cv2.imshow("Kanallar Degistirildi", merged)

# Kamera Açma
cap = cv2.VideoCapture(0)
cv2.namedWindow("Kamera", cv2.WINDOW_NORMAL)
print("Kamerayi kapatmak icin 'q' tusuna basin.")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Kamera", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyWindow("Kamera")

# Şekil Çizme
canvas = np.zeros((400, 400, 3), dtype="uint8")
cv2.line(canvas, (0, 0), (400, 400), (255, 0, 0), 2)
cv2.rectangle(canvas, (50, 50), (300, 300), (0, 255, 0), 3)
cv2.circle(canvas, (200, 200), 50, (0, 0, 255), -1)
cv2.imshow("Cizimler", canvas)

# Görüntüden Parça Kesme
kesit = img[100:300, 100:300]
cv2.imshow("Kesit", kesit)

# Görüntüyü Kaydetme
cv2.imwrite("kaydedilen_goruntu.jpg", img)
print("Goruntu 'kaydedilen_goruntu.jpg' olarak kaydedildi.")

cv2.waitKey(0)
cv2.destroyAllWindows()
