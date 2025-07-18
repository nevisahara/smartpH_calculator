import streamlit as st
import math

# Konfigurasi halaman
st.set_page_config(page_title="Smart Kalkulator pH", layout="centered")

# CSS untuk tema hitam dengan teks putih
st.markdown("""
<style>
body {
    background-color: #000000;
    color: white;
}

[data-testid="stAppViewContainer"] > .main {
    background-color: #000000;
    color: white;
}

h1, h2, h3, h4, h5, h6, p, span {
    color: white;
}

.stButton > button {
    background-color: #1e3a8a;
    color: white;
    border-radius: 8px;
}

.stSelectbox, .stNumberInput {
    background-color: #1e1e1e;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Sidebar Navigasi
menu = st.sidebar.radio("Navigasi", ["Beranda", "Hitung pH", "Tentang Aplikasi"])

if menu == "Beranda":
    st.title("Selamat Datang di Smart Kalkulator pH")
    st.image("https://cdn.pixabay.com/photo/2017/09/21/15/11/laboratory-2778756_960_720.jpg", use_column_width=True)
    st.markdown("""
    ### Oleh:
    - Amar Evan Gading (2460321)  
    - Diandra Namira Zahfa (2460360)  
    - Lutfhia Salwani Fatonah (2460410)  
    - Nevi Sahara (2460471)  
    - Taufan Aliafi (2460525)
    """)

elif menu == "Hitung pH":
    st.header("🔬 Kalkulator pH Larutan")
    st.image("https://cdn.pixabay.com/photo/2016/03/31/18/33/acid-1295136_960_720.png", use_column_width=True)

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
    st.image("https://cdn.pixabay.com/photo/2017/03/21/15/39/test-2165766_960_720.jpg", use_column_width=True)

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

    ### Contoh Soal:
    Hitung pH larutan HCl 0.01 M!

    *Penyelesaian:*
    Karena HCl adalah asam kuat → [H⁺] = 0.01 M  
    pH = -log(0.01) = 2.00
    """)
