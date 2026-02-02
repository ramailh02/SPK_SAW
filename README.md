# SPK Metode SAW - Kelompok 7

Aplikasi Sistem Pendukung Keputusan (SPK) menggunakan metode **Simple Additive Weighting (SAW)** yang dibangun dengan Streamlit.

## 📋 Daftar Isi
- [Tentang Proyek](#tentang-proyek)
- [Fitur](#fitur)
- [Instalasi](#instalasi)
- [Cara Penggunaan](#cara-penggunaan)
- [Struktur Proyek](#struktur-proyek)
- [Teknologi](#teknologi)
- [Tim](#tim)

## 📖 Tentang Proyek

Aplikasi ini adalah implementasi sistem pendukung keputusan berbasis web yang menggunakan metode SAW (Simple Additive Weighting). SAW adalah salah satu metode Multi-Criteria Decision Making (MCDM) yang menggabungkan beberapa kriteria untuk membantu dalam pengambilan keputusan.

## ✨ Fitur

- 🎯 Interface yang modern dan responsif
- 📊 Analisis data multi-kriteria
- 🔢 Perhitungan otomatis metode SAW
- 📈 Visualisasi hasil dalam bentuk grafik
- 🎨 Desain yang menarik dengan gradient styling
- 💾 Input data yang fleksibel

## 🚀 Instalasi

### Prerequisites
- Python 3.8 atau lebih tinggi
- pip (Python package manager)

### Langkah Instalasi

1. Clone repository
```bash
git clone https://github.com/ramailh02/SPK_SAW.git
cd SAW_KEL7
```

2. Buat virtual environment (opsional tapi direkomendasikan)
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# atau
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## 💻 Cara Penggunaan

1. Jalankan aplikasi
```bash
streamlit run app.py
```

2. Aplikasi akan membuka di browser default Anda (biasanya http://localhost:8501)

3. Ikuti langkah-langkah pada aplikasi untuk:
   - Input data alternatif dan kriteria
   - Tentukan bobot setiap kriteria
   - Pilih jenis kriteria (benefit/cost)
   - Lihat hasil perhitungan SAW
   - Analisis visualisasi data

## 📁 Struktur Proyek

```
SAW_KEL7/
├── app.py              # File utama aplikasi
├── README.md           # Dokumentasi ini
└── .git/               # Git repository
```

## 📊 Diagram Alur Metode SAW

![Diagram Alur](https://via.placeholder.com/800x300?text=Diagram+Alur+SAW)

## 🛠️ Teknologi

- **Streamlit** - Framework untuk membuat web app interaktif
- **Pandas** - Data manipulation dan analisis
- **NumPy** - Komputasi numerik
- **Matplotlib** - Visualisasi data dan grafik

## 👥 Tim

**Kelompok 7** - Implementasi Sistem Pendukung Keputusan Metode SAW

## 📝 Lisensi

Proyek ini bersifat edukatif dan dikembangkan untuk tujuan pembelajaran.

## 📸 Screenshot

<img width="1819" height="797" alt="Screenshot 2026-01-22 145015" src="https://github.com/user-attachments/assets/14e9b33a-0ada-4a50-b8ed-f05d79134898" />
<img width="1805" height="478" alt="Screenshot 2026-01-22 145103" src="https://github.com/user-attachments/assets/44493f1e-36fc-40b6-a94b-450a629d07ed" />
<img width="1730" height="723" alt="Screenshot 2026-01-22 145128" src="https://github.com/user-attachments/assets/2dabb497-3b61-42d5-852c-2843aeb51a80" />
<img width="1756" height="740" alt="Screenshot 2026-01-22 145149" src="https://github.com/user-attachments/assets/3b9a7f54-e575-42d8-b1fd-6f687814cc1c" />

*Interface utama aplikasi SPK Metode SAW*

---

**Last Updated:** Februari 2, 2026

