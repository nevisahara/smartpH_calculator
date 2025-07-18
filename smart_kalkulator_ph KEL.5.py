import streamlit as st
import math

# Konfigurasi halaman
st.set_page_config(page_title="Smart Kalkulator pH", layout="centered")

# Tema warna hitam dengan font putih
st.markdown("""
    <style>
    body, .stApp {
        background-color: #537895;
        color: white;
    }
    h1, h2, h3, h4, h5, h6, p, label, .stTextInput, .stSelectbox, .stNumberInput, .stMarkdown, .stButton, .stRadio > div {
        color: white !important;
    }
    .stButton > button {
        background-color: #1e3a8a;
        color: white;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# CSS: Ubah warna font radio di sidebar jadi hitam
st.markdown("""
    <style>
    .stRadio > div > label, .stRadio > div div {
        color: black !important;
        font-weight: bold;
    }

    [data-testid="stSidebar"] {
        background-color: #f0f0f0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigasi
menu = st.sidebar.radio("Navigasi", ["Beranda", "Hitung pH", "Tentang Aplikasi"])

# Sidebar Navigasi
menu = st.sidebar.radio("Navigasi", ["Beranda", "Hitung pH", "Tentang Aplikasi"])

if menu == "Beranda":
    st.title("Selamat Datang di Smart Kalkulator pH")

    # Menampilkan gambar dengan ukuran custom (HTML)
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://cdn.pixabay.com/photo/2013/07/13/13/48/chemistry-161575_640.png" 
                 alt="Ilustrasi Kimia" 
                 width="250">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Informasi pembuat
    st.markdown("""
    ### Dibuat Oleh:
    - Amar Evan Gading (2460321)  
    - Diandra Namira Zahfa (2460360)  
    - Lutfhia Salwani Fatonah (2460410)  
    - Nevi Sahara (2460471)  
    - Taufan Aliafi (2460525)
    """)

elif menu == "Hitung pH":
    st.header("🔬 Kalkulator pH Larutan")

    jenis = st.selectbox("Pilih Jenis Larutan:", ["Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Lemah"])
    konsentrasi = st.number_input("Masukkan konsentrasi (M):", min_value=0.0, step=0.001, format="%.3f")

    if jenis in ["Asam Lemah", "Basa Lemah"]:
        konstanta = st.number_input(f"Masukkan {'Ka' if 'Asam' in jenis else 'Kb'}:", min_value=0.0, format="%.2e")

    if st.button("Hitung pH"):
        try:
            if jenis == "Asam Kuat":
                ph = -math.log10(konsentrasi)
                penjelasan = "Asam kuat terionisasi sempurna sehingga [H⁺] = konsentrasi asam."
            elif jenis == "Basa Kuat":
                poh = -math.log10(konsentrasi)
                ph = 14 - poh
                penjelasan = "Basa kuat terionisasi sempurna sehingga [OH⁻] = konsentrasi basa."
            elif jenis == "Asam Lemah":
                h = math.sqrt(konstanta * konsentrasi)
                ph = -math.log10(h)
                penjelasan = "Asam lemah hanya terionisasi sebagian. Rumus: pH = -log(√(Ka × [HA]))"
            elif jenis == "Basa Lemah":
                oh = math.sqrt(konstanta * konsentrasi)
                poh = -math.log10(oh)
                ph = 14 - poh
                penjelasan = "Basa lemah hanya terionisasi sebagian. Rumus: pH = 14 - log(√(Kb × [B]))"

            st.success(f"Hasil pH: {ph:.2f}")
            st.info(penjelasan)

        except Exception as e:
            st.error("Terjadi kesalahan perhitungan. Pastikan data valid.")

elif menu == "Tentang Aplikasi":
    st.header("📘 Tentang Aplikasi")
    
    st.markdown("""
    ### 1. Apa itu pH?
    pH adalah ukuran konsentrasi ion hidrogen (H⁺) dalam larutan. Skala pH berkisar dari 0 sampai 14:
    - pH < 7: larutan bersifat asam  
    - pH = 7: larutan netral  
    - pH > 7: larutan bersifat basa

    ### 2. Rumus pH yang Digunakan:
    - Asam Kuat: *pH = -log[H⁺]*  
    - Basa Kuat: *pH = 14 - (-log[OH⁻])*  
    - Asam Lemah: *pH = -log(√(Ka × [HA]))*  
    - Basa Lemah: *pH = 14 - log(√(Kb × [B]))*

    ### 3. Contoh Soal:
    *Hitung pH dari larutan HCl 0.01 M (Asam Kuat)*  
    - Rumus: pH = -log [H⁺] = -log(0.01) = 2.00

    *Hitung pH dari NH₃ 0.1 M, Kb = 1.8 × 10⁻⁵ (Basa Lemah)*  
    - [OH⁻] = √(Kb × [B]) = √(1.8e-5 × 0.1) ≈ 1.34×10⁻³  
    - pOH = -log(1.34e-3) ≈ 2.87  
    - pH = 14 - 2.87 = 11.13
    """)
