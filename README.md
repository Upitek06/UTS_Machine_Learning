# Klasifikasi Kanker Payudara (Breast Cancer Wisconsin)
**Kelompok:** 5
**Mata Kuliah:** Machine Learning (Semester Ganjil 2026/2027)

Repositori ini berisi seluruh artefak komputasi untuk Tugas Besar UTS Klasifikasi Kanker Payudara menggunakan algoritma klasik (Decision Tree, kNN, Random Forest).

## Struktur Repositori
* `data/`: Memuat dataset asli dan `split_uji.csv` (indeks test data yang dikunci).
  * **Hash MD5 split_uji.csv:** [Isi dengan Hash yang kamu generate dari 01_eda.ipynb]
* `notebooks/`: Memuat 3 Jupyter Notebook yang dipecah secara berurutan (01 EDA, 02 Model Pipeline, 03 Analisis Akhir).
* `laporan/`: Memuat laporan final berformat PDF.
* `requirements.txt`: Memuat spesifikasi library untuk reproduktibilitas.
* `AI-USAGE.md`: Deklarasi transparansi penggunaan alat bantu AI.

## Cara Menjalankan (Reproduksi Hasil)
1. Lakukan *clone* repositori ini: git clone https://github.com/Upitek06/uts_ml_kelompok_05.
2. Instal dependensi: `pip install -r requirements.txt`
3. Jalankan Jupyter Notebook secara berurutan mulai dari `01_eda.ipynb` hingga `03_analisis.ipynb`.
4. Tekan tombol **"Restart and Run All"** pada setiap notebook. Kode akan otomatis mengekstrak metrik evaluasi (F1, CI 95%, Cost) dan visualisasi Confusion Matrix.

## Pembagian Kerja Kelompok
* **Lutfian Fallah:** Merancang infrastruktur kode (Pipeline, GridSearchCV), protokol evaluasi test data, analisis statistik (Uji-t, CI 95%), dan penyusunan laporan akademik.
* **Muhammad Ihsan Adz-Dzikra:** Membantu penysunan hasil data evaluasi menjadi laporan hasil analisis kelompok, dan membantu penyusunan power point.
* **Abdurrohman Ash Shiddiq:** Membantu penyusunan laporan, membantu mengumpulkan data sebelum dilakukan pengujian dan analisis statistik
* **Raulmizal Maulana:** Membantu mengumpulkan data, Dan menyiapkan power point hasil analisis kami untuk dipresentasikan sesuai standar yang telah ditentukan.