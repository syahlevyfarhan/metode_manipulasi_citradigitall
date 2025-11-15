import cv2
import numpy as np
import matplotlib.pyplot as plt

# === LOAD IMAGE (otomatis baca dari folder yang sama) ===
img = cv2.imread("img-1.jpeg")

if img is None:
    print("Gambar tidak ditemukan! Pastikan file ada di folder yang sama.")
    exit()

# === CONVERT TO LAB ===
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)

# === APPLY CLAHE ===
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl = clahe.apply(l)

# Gabungkan lagi ke LAB
lab_clahe = cv2.merge((cl, a, b))

# Kembali ke RGB agar warna normal
enhanced = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2RGB)

# === SHOW RESULT ===
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Enhanced (CLAHE)")
plt.imshow(enhanced)
plt.axis("off")

plt.show()