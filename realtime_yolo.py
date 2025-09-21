from ultralytics import YOLO
import cv2

# 1) YOLOv8 küçük modeli indir
model = YOLO("yolov8n.pt")

# 2) Kamerayı aç
cap = cv2.VideoCapture(0)  # 0: laptop kamerası

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 3) Modeli çalıştır
    results = model(frame)

    # 4) Tahminleri çizdir
    annotated = results[0].plot()

    # 5) Görüntüyü ekrana ver
    cv2.imshow("Gerçek Zamanlı Nesne Tespiti", annotated)

    # q ile çıkış
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# YOLOv8 modelini ONNX'e export et
model.export(format="onnx")
