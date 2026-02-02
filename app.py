import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="SPK Metode SAW - Kelompok 7", layout="wide")

st.markdown("""
    <style>
    /* Modern Background Gradient */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #e9ecef 100%);
        font-family: 'Segoe UI', 'Roboto', sans-serif;
        scroll-behavior: smooth;
    }
    
    /* Header Styling */
    .stTitle {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    
    /* Subheader Styling */
    .stSubheader {
        color: #495057;
        font-weight: 600;
        letter-spacing: -0.3px;
    }
    
    /* Modern Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.2em;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 700;
        border: none;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        font-size: 16px;
        letter-spacing: 0.5px;
        cursor: pointer;
    }
    
    .stButton>button:hover {
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
        transform: translateY(-2px);
    }
    
    .stButton>button:active {
        transform: translateY(0px);
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        border-radius: 10px;
        border: 1px solid #e9ecef;
        padding: 12px 16px;
        font-weight: 600;
        color: #2c3e50;
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, #e9ecef 0%, #f8f9fa 100%);
        border-color: #667eea;
        transform: translateX(2px);
    }
    
    /* Data Editor Styling */
    .stDataEditor {
        border-radius: 12px;
        border: 1px solid #e9ecef;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .stDataEditor:hover {
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
        border-color: #667eea;
    }
    
    /* Table Styling */
    .stTable {
        background-color: white;
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    }
    
    /* Info/Success/Error Box */
    .stAlert {
        border-radius: 10px;
        border-left: 4px solid #667eea;
        animation: slideInUp 0.3s ease;
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] button {
        border-radius: 8px 8px 0 0;
        font-weight: 600;
        transition: all 0.3s ease;
        color: #495057;
    }
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
    }
    
    .stTabs [data-baseweb="tab-list"] button:hover {
        background: linear-gradient(135deg, #f0f3ff 0%, #f5f1ff 100%);
        color: #667eea;
    }
    
    /* Divider */
    hr {
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        border: none;
        height: 2px;
        margin: 2em 0;
    }
    
    /* Caption Styling */
    .stCaption {
        color: #868e96;
        font-size: 13px;
        text-align: center;
        margin-top: 2em;
    }
    
    /* Custom Cards for sections */
    .custom-card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
        border: 1px solid #e9ecef;
        margin: 16px 0;
        transition: all 0.3s ease;
    }
    
    .custom-card:hover {
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    }
    
    /* Input Styling */
    [data-baseweb="input"] {
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
    }
    
    [data-baseweb="input"]:focus {
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    /* Select Box */
    [data-baseweb="select"] {
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
    }
    
    /* Number Input */
    [data-baseweb="base-input"] {
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
    }
    
    /* Smooth transitions for all interactive elements */
    * {
        transition: background-color 0.2s ease, color 0.2s ease, transform 0.2s ease;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; margin-bottom: 30px;'>
    <h1 style='font-size: 2.8em; margin: 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800;'>
        🧠 Sistem Pendukung Keputusan - Metode SAW
    </h1>
    <p style='color: #495057; font-size: 1.1em; margin-top: 10px; font-weight: 500;'>
        Simple Additive Weighting (Versi Dinamis & Terintegrasi)
    </p>
</div>
""", unsafe_allow_html=True)

# --- 1. DATA DEFAULT (Disesuaikan dengan permintaan Anda) ---
if 'kriteria' not in st.session_state:
    st.session_state.kriteria = pd.DataFrame([
        {"Nama": "Penguasaan Aspek Teknis", "Bobot": 30, "Tipe": "Benefit"},
        {"Nama": "Pengalaman Kerja", "Bobot": 25, "Tipe": "Benefit"},
        {"Nama": "Interpersonal Skill", "Bobot": 20, "Tipe": "Benefit"},
        {"Nama": "Usia", "Bobot": 15, "Tipe": "Cost"},
        {"Nama": "Status Perkawinan", "Bobot": 10, "Tipe": "Cost"}
    ])

if 'alternatif' not in st.session_state:
    # Struktur awal disesuaikan agar langsung terbaca oleh tabel editor
    st.session_state.alternatif = pd.DataFrame([
        {'Alternatif': 'Enrico', 'Penguasaan Aspek Teknis': 8, 'Pengalaman Kerja': 5, 'Interpersonal Skill': 7, 'Usia': 30, 'Status Perkawinan': 8},
        {'Alternatif': 'Yuna', 'Penguasaan Aspek Teknis': 7, 'Pengalaman Kerja': 4, 'Interpersonal Skill': 8, 'Usia': 28, 'Status Perkawinan': 10},
        {'Alternatif': 'Vicky', 'Penguasaan Aspek Teknis': 9, 'Pengalaman Kerja': 6, 'Interpersonal Skill': 8, 'Usia': 27, 'Status Perkawinan': 10},
        {'Alternatif': 'Tantri', 'Penguasaan Aspek Teknis': 6, 'Pengalaman Kerja': 3, 'Interpersonal Skill': 6, 'Usia': 35, 'Status Perkawinan': 5},
    ])

# --- 2. INPUT KRITERIA ---
with st.expander("🛠️ 1. Konfigurasi Kriteria", expanded=True):
    st.markdown("""<style>
    .section-header {
        color: #2c3e50;
        font-weight: 700;
        margin-bottom: 10px;
    }
    </style>""", unsafe_allow_html=True)
    edited_kriteria = st.data_editor(
        st.session_state.kriteria, 
        num_rows="dynamic", 
        use_container_width=True,
        column_config={
            "Tipe": st.column_config.SelectboxColumn("Tipe", options=["Benefit", "Cost"], required=True),
            "Bobot": st.column_config.NumberColumn("Bobot (%)", min_value=0, max_value=100)
        },
        key="editor_k"
    )
    st.info("💡 **Tipe Kriteria:** Benefit (Makin besar makin baik) | Cost (Makin kecil makin baik)")

# --- 3. INPUT ALTERNATIF & NILAI ---
with st.expander("📝 2. Matriks Kecocokan Alternatif (X)", expanded=True):
    # Proteksi kolom Nama
    if "Nama" in edited_kriteria.columns:
        list_kriteria = edited_kriteria["Nama"].dropna().tolist()
    else:
        list_kriteria = []
        st.error("Kolom 'Nama' pada tabel kriteria tidak ditemukan!")

    cols_needed = ["Alternatif"] + list_kriteria
    df_alt_base = st.session_state.alternatif

    # Tambahkan kolom baru jika ada penambahan kriteria secara dinamis
    for col in list_kriteria:
        if col not in df_alt_base.columns:
            df_alt_base[col] = 0.0
            
    # Pastikan hanya menampilkan kolom yang valid
    existing_cols = [c for c in cols_needed if c in df_alt_base.columns]
    
    edited_alternatif = st.data_editor(
        df_alt_base[existing_cols], 
        num_rows="dynamic", 
        use_container_width=True,
        key="editor_a"
    )

# --- 4. LOGIKA PERHITUNGAN SAW ---


if st.button("🚀 Jalankan Kalkulasi SAW"):
    if edited_kriteria.empty or edited_alternatif.empty:
        st.error("Data kriteria atau alternatif tidak boleh kosong!")
    else:
        try:
            # a. Persiapan Data
            df_x = edited_alternatif.set_index("Alternatif").astype(float)
            weights = edited_kriteria.set_index("Nama")["Bobot"].astype(float)
            normalized_weights = weights / weights.sum()
            
            # b. Normalisasi (Matriks R)
            df_r = df_x.copy()
            for _, row in edited_kriteria.iterrows():
                k_nama = row["Nama"]
                k_tipe = str(row["Tipe"]).lower()
                
                if k_tipe == "benefit":
                    df_r[k_nama] = df_x[k_nama] / df_x[k_nama].max()
                else:
                    df_r[k_nama] = df_x[k_nama].min() / df_x[k_nama]
            
            # c. Perhitungan Preferensi (V)
            df_p = df_r.mul(normalized_weights, axis=1)
            skor_akhir = df_p.sum(axis=1).round(4)
            
            # d. Ranking
            ranking = skor_akhir.reset_index()
            ranking.columns = ["Alternatif", "Skor Akhir (V)"]
            ranking = ranking.sort_values(by="Skor Akhir (V)", ascending=False).reset_index(drop=True)
            ranking.index += 1

            # --- DISPLAY HASIL ---
            st.divider()
            
            tab1, tab2, tab3 = st.tabs(["🏆 Hasil Ranking", "📊 Visualisasi", "🔢 Detail Matriks"])
            
            with tab1:
                st.markdown("<h3 style='color: #2c3e50; font-weight: 700;'>🏆 Ranking Final</h3>", unsafe_allow_html=True)
                
                def highlight_winner(s):
                    return ['background: linear-gradient(135deg, #c6f6d5 0%, #a8e6c1 100%); font-weight: bold; border-radius: 8px;' 
                            if i == 0 else 'background-color: #f8f9fa; border-radius: 4px;' for i in range(len(s))]
                
                st.dataframe(ranking.style.apply(highlight_winner, subset=["Alternatif", "Skor Akhir (V)"])
                            .format({"Skor Akhir (V)": "{:.4f}"})
                            .set_properties(**{'text-align': 'center', 'padding': '10px'}),
                            use_container_width=True)
                
                winner = ranking.iloc[0]['Alternatif']
                winner_score = ranking.iloc[0]['Skor Akhir (V)']
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%); 
                border-left: 5px solid #28a745; border-radius: 8px; padding: 16px; margin: 16px 0;'>
                    <h4 style='color: #155724; margin: 0 0 8px 0;'>✅ Hasil Terbaik</h4>
                    <p style='color: #155724; margin: 0; font-size: 1.2em; font-weight: 600;'>
                        <strong>{winner}</strong> dengan skor <strong>{winner_score:.4f}</strong>
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                # Download CSV
                csv = ranking.to_csv(index=False).encode('utf-8')
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.download_button("📥 Download CSV", data=csv, file_name="hasil_saw.csv", mime="text/csv")

            with tab2:
                st.markdown("<h3 style='color: #2c3e50; font-weight: 700;'>📊 Perbandingan Skor Akhir</h3>", unsafe_allow_html=True)
                fig, ax = plt.subplots(figsize=(12, 6), facecolor='white')
                colors = ['#28a745' if i == 0 else '#667eea' for i in range(len(ranking))]
                bars = ax.bar(ranking["Alternatif"], ranking["Skor Akhir (V)"], color=colors, edgecolor='#e9ecef', linewidth=2)
                
                # Styling
                ax.set_ylabel("Skor V", fontsize=12, fontweight=600, color='#2c3e50')
                ax.set_xlabel("Alternatif", fontsize=12, fontweight=600, color='#2c3e50')
                ax.set_ylim(0, max(ranking["Skor Akhir (V)"]) * 1.15)
                ax.grid(axis='y', alpha=0.2, linestyle='--', color='#667eea')
                ax.set_axisbelow(True)
                
                # Add value labels on bars
                for i, (bar, value) in enumerate(zip(bars, ranking["Skor Akhir (V)"])):
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                           f'{value:.4f}', ha='center', va='bottom', fontweight=600, fontsize=10)
                
                plt.tight_layout()
                st.pyplot(fig)

            with tab3:
                st.markdown("<h3 style='color: #2c3e50; font-weight: 700;'>🔢 Detail Matriks Perhitungan</h3>", unsafe_allow_html=True)
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("<h4 style='color: #495057; font-weight: 600;'>📐 Matriks Normalisasi (R)</h4>", unsafe_allow_html=True)
                    st.dataframe(df_r.style.highlight_max(axis=0, color="#fff3cd")
                                .format(precision=4)
                                .set_properties(**{'text-align': 'center', 'padding': '8px'}),
                                use_container_width=True)
                with col_b:
                    st.markdown("<h4 style='color: #495057; font-weight: 600;'>⚖️ Matriks Preferensi (P)</h4>", unsafe_allow_html=True)
                    st.dataframe(df_p.style.format(precision=4)
                                .set_properties(**{'text-align': 'center', 'padding': '8px'}),
                                use_container_width=True)

        except Exception as e:
            st.error(f"Terjadi kesalahan perhitungan: {e}")

st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; margin-top: 40px;'>
    <p style='color: #868e96; font-size: 0.95em; margin: 0;'>
        © 2026 | Dibuat Oleh <span style='font-weight: 600; color: #495057;'>Kelompok 7</span> - Sistem Pendukung Keputusan
    </p>
    <p style='color: #adb5bd; font-size: 0.85em; margin: 8px 0 0 0;'>
        Metode Simple Additive Weighting (SAW) - Decision Support System
    </p>
</div>
""", unsafe_allow_html=True)