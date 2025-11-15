[# metode_manipulasi_citradigitall
Adaptive Image Enhancement menggunakan CLAHE (Contrast Limited Adaptive Histogram Equalization)

Project ini mengimplementasikan teknik CLAHE (Contrast Limited Adaptive Histogram Equalization) untuk meningkatkan kualitas visual citra pada domain spasial. Metode ini banyak digunakan untuk memperbaiki kontras gambar yang memiliki pencahayaan kurang merata, sekaligus menjaga agar warna tetap natural dan tidak menimbulkan noise berlebihan.

🎯 Tujuan

Mengoptimalkan detail gambar pada area yang terlalu gelap atau terang.

Meningkatkan kontras lokal tanpa merusak informasi warna.

Menghasilkan citra yang lebih jelas, natural, dan nyaman dilihat.

💡 Kenapa Menggunakan CLAHE?

Perbandingan dengan metode lain:

Metode	Kekurangan
Brightness / Contrast	Hasil terlalu sederhana dan kurang efektif untuk area yang kompleks
Gamma Correction	Cocok hanya untuk gambar yang terlalu gelap/terang
AHE (Adaptive Histogram Equalization)	Menambah noise secara signifikan
ACE (Automatic Color Equalization)	Dapat menimbulkan tekstur kasar pada citra normal
✔ Keunggulan CLAHE:

Hasil natural

Minim noise

Detail lebih muncul

Sangat cocok untuk foto nyata

Oleh karena itu, CLAHE menjadi metode yang sangat efektif untuk enhancement citra dalam project ini.

⚙️ Cara Kerja CLAHE (Ringkas)

Gambar diubah ke ruang warna LAB

L = Lightness (kecerahan)

A = hijau ↔ merah

B = biru ↔ kuning

CLAHE diterapkan khusus pada channel L untuk meningkatkan kontras tanpa mengubah warna asli.

Channel digabungkan kembali dan gambar dikonversi kembali ke RGB.

🚀 Cara Menjalankan Program
1. Pastikan Python 3 sudah terinstall
2. Install library yang dibutuhkan
pip install opencv-python numpy matplotlib

3. Pastikan file gambar (img-1.jpeg) berada satu folder dengan main.py
4. Jalankan program
python main.py

📸 Output

Program akan menampilkan dua gambar:

Original

Enhanced (CLAHE)

Hasil proses CLAHE akan menunjukkan peningkatan kontras yang lebih halus, natural, dan tanpa peningkatan noise secara berlebihan.
