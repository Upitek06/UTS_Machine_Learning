# Data: Breast Cancer Wisconsin (Diagnostic)

Folder ini menyimpan dataset yang digunakan untuk melatih dan menguji model klasifikasi kanker payudara pada tugas besar ini.

## Sumber Data & Lisensi
* **Sumber:** Diunduh dari UCI Machine Learning Repository / Kaggle.

## Cara Mengunduh Data
Dataset orisinal dapat diunduh secara publik melalui [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) atau melalui portal Kaggle. Untuk proyek ini, dataset telah diunduh, dibersihkan, dan dikunci pada file `split_uji.csv`.

## Lisensi
Dataset ini berlisensi **Creative Commons Attribution 4.0 International (CC BY 4.0)** (atau lisensi terbuka akademik UCI). Data ini bebas digunakan untuk keperluan edukasi, riset, maupun komersial dengan syarat memberikan atribusi kepada kreator aslinya (Dr. William H. Wolberg, W. Nick Street, dan Olvi L. Mangasarian dari University of Wisconsin).

## Kartu Data (Data Card)
Dataset Breast Cancer Wisconsin (Diagnostic) terdiri dari 569 baris rekam medis pasien. Terdapat 30 fitur numerik yang merepresentasikan karakteristik geometri inti sel (seperti radius, tekstur, perimeter, area), dan 1 kolom target diagnosis yang terbagi menjadi dua kelas: Malignant (ganas) dan Benign (jinak).

## Isi Direktori
* `breast_cancer.csv`: Dataset asli yang berisi 569 baris rekam medis pasien dengan 30 fitur geometri sel (seperti radius, tekstur, area) dan 1 kolom target diagnosis (Malignant/Benign).
* `split_uji.csv`: File yang menyimpan indeks baris dari 20% data uji (Test Data). Indeks ini dikunci dan disimpan secara fisik untuk membuktikan bahwa data uji tidak pernah bocor ke dalam fase pelatihan model (*preventing data leakage*).