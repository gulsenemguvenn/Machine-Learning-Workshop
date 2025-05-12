
import cv2

# Kamerayı başlat
cap = cv2.VideoCapture(0)
cv2.namedWindow("Nesne Algilama", cv2.WINDOW_NORMAL)

print("Kamerayi kapatmak icin 'q' tusuna basin.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü griye çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Kenar algılama (Canny)
    edges = cv2.Canny(gray, 50, 150)

    # Kontur (çizgi/şekil) bulma
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Konturları çiz
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # küçük gürültüleri engelle
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Görüntüyü göster
    cv2.imshow("Nesne Algilama", frame)

    # Çıkmak için 'q' tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()