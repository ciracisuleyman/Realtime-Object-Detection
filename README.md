# Gerçek Zamanlı Nesne Tespiti – YOLOv8 + OpenCV

Bu proje, [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) modeli ve OpenCV kullanarak **gerçek zamanlı nesne tespiti** yapmaktadır.  
Laptop kamerası üzerinden görüntü alınır, model çalıştırılır ve tespit edilen nesneler ekranda kutular ile gösterilir.  
Ayrıca model ONNX formatına export edilmiştir.

---

## Özellikler
- Gerçek zamanlı nesne tespiti
- OpenCV ile kamera entegrasyonu
- YOLOv8 önceden eğitilmiş model
- ONNX export (farklı platformlarda kullanım için)

---

## Kullanılan Teknolojiler
- Python
- OpenCV
- Ultralytics YOLOv8

---

##  Kurulum
1. Bu repoyu klonla:
   ```bash
   git clone https://github.com/ciracisuleyman/Realtime-Object-Detection.git
   cd Realtime-Object-Detection

Gerekli kütüphaneleri yükle:

pip install -r requirements.txt

Çalıştırma
python realtime_yolo.py
