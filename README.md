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

![Alt text](assets/screenshot.png)(https://via.placeholder.com/800x400?text=SPK+SAW+Kelompok+7)

*Interface utama aplikasi SPK Metode SAW*

---

**Last Updated:** Februari 2, 2026
