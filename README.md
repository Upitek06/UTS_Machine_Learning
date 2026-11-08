# Medical Diagnostic Pipeline: Breast Cancer Classification

Proyek ini mengimplementasikan *Machine Learning Pipeline* untuk mengklasifikasikan data sel tumor payudara secara biner: **Jinak (Benign - 0)** atau **Ganas (Malignant - 1)**. Pipeline ini membandingkan kinerja tiga arsitektur *Supervised Learning* untuk menentukan model yang paling presisi secara matematis.

## Arsitektur & Teknologi
*   **Bahasa Utama:** Python 3.x
*   **Pemrosesan Matriks & Data:** `pandas`
*   **Mesin Klasifikasi:** `scikit-learn`
*   **Algoritma Tersertifikasi:** 
    1. Decision Tree (*Parametric, Rule-based*)
    2. k-Nearest Neighbor (*Non-parametric, Distance-based*)
    3. Random Forest (*Ensemble Learning, Variance Reduction*)

## Struktur Repositori
```text
.
├── data/
│   └── breast_cancer.csv      # Dataset statis (Kaggle)
├── main.py                    # Script eksekusi pipeline ML
└── README.md                  # Dokumentasi proyek

```

## ⚙️ Eksekusi Pipeline Data (Preprocessing)
1. Sanitasi Noise: Membuang kolom id dan Unnamed: 32 agar tidak mendistorsi Inductive Bias algoritma.

2. Transformasi Numerik: Melakukan pemetaan string ke integer absolut (M -> 1, B -> 0).

3. Isolasi Lingkungan (Train-Test Split): Matriks dipecah menggunakan random_state=42 menghasilkan dimensi yang steril:

    - Data Latih (X_train): 455 baris, 30 fitur

    - Data Uji (X_test): 114 baris, 30 
    
## 📊 Hasil Komparasi Performa (Akurasi Global)
Pemenang klasifikasi diuji secara buta menggunakan environment Data Uji (X_test):

| **Algoritma** | **Tingkat Akurasi** | **Evaluasi Arsitektural** |
| :---: | :---: | :---: |
| Random Forest | 96.49%Pemenang. | Mampu mereduksi varians melalui mekanisme voting mayoritas dari kumpulan pohon keputusan.
| k-Nearest Neighbor | 95.61%Tertahan. | Rentan terhadap dominasi skala angka absolut karena menggunakan jarak Euclidean.
| Decision Tree | 94.73%Terendah. | Sangat deterministik dan rentan mengalami overfitting pada data latih.