# Data: Breast Cancer Wisconsin (Diagnostic)

Folder ini menyimpan dataset yang digunakan untuk melatih dan menguji model klasifikasi kanker payudara pada tugas besar ini.

## Sumber Data & Lisensi
* **Sumber:** Diunduh dari UCI Machine Learning Repository / Kaggle.
* **Lisensi:** CC0 (Public Domain) / Open Data. Dataset ini bebas digunakan untuk keperluan akademik.

## Isi Direktori
* `breast_cancer.csv`: Dataset asli yang berisi 569 baris rekam medis pasien dengan 30 fitur geometri sel (seperti radius, tekstur, area) dan 1 kolom target diagnosis (Malignant/Benign).
* `split_uji.csv`: File yang menyimpan indeks baris dari 20% data uji (Test Data). Indeks ini dikunci dan disimpan secara fisik untuk membuktikan bahwa data uji tidak pernah bocor ke dalam fase pelatihan model (*preventing data leakage*).