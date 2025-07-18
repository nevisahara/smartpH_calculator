
import streamlit as st
import math

# Konfigurasi halaman
st.set_page_config(page_title="Smart Kalkulator pH", layout="centered", page_icon="🧪")

# Tema CSS hijau
st.markdown("""
    <style>
        body {
            background-color: #3D8D7A;
            color: #FBFFE4;
        }
        .stApp {
            background-color: #3D8D7A;
        }
        h1, h2, h3, h4, h5 {
            color: #FBFFE4;
        }
        .sidebar .sidebar-content {
            background-color: #3D8D7A;
        }
    </style>
""", unsafe_allow_html=True)

# Navigasi
menu = st.sidebar.selectbox("Navigasi", ["Beranda", "Hitung pH", "Tentang Aplikasi"])

if menu == "Beranda":
    st.title("Selamat Datang di Smart Kalkulator pH")
    st.markdown("### Dibuat oleh:")
    st.markdown("- Amar Evan Gading (2460321)  \n- Diandra Namira Zahfa (2460360)  \n- Lutfhia Salwani Fatonah (2460410)  \n- Nevi Sahara (2460471)  \n- Taufan Aliafi (2460525)")

elif menu == "Hitung pH":
    st.title("Kalkulator pH Larutan")

    jenis = st.selectbox("Pilih Jenis Larutan", ["Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Lemah"])
    konsentrasi = st.number_input("Masukkan konsentrasi (mol/L)", min_value=0.0, format="%.4f")

    if jenis in ["Asam Lemah", "Basa Lemah"]:
        konstanta = st.number_input(f"Masukkan nilai {'Ka' if jenis == 'Asam Lemah' else 'Kb'}", min_value=1e-10, format="%.2e")

    if st.button("Hitung"):
        if jenis == "Asam Kuat":
            ph = -math.log10(konsentrasi) if konsentrasi > 0 else 7
            info = "Asam kuat terionisasi sempurna, sehingga [H⁺] = konsentrasi larutan."
        elif jenis == "Asam Lemah":
            h = (konstanta * konsentrasi) ** 0.5
            ph = -math.log10(h)
            info = "Asam lemah hanya terionisasi sebagian, dihitung dengan rumus akar(Ka × [HA])."
        elif jenis == "Basa Kuat":
            poh = -math.log10(konsentrasi) if konsentrasi > 0 else 7
            ph = 14 - poh
            info = "Basa kuat terionisasi sempurna, sehingga [OH⁻] = konsentrasi larutan."
        elif jenis == "Basa Lemah":
            oh = (konstanta * konsentrasi) ** 0.5
            poh = -math.log10(oh)
            ph = 14 - poh
            info = "Basa lemah hanya terionisasi sebagian, dihitung dengan rumus akar(Kb × [B])."

        st.success(f"pH larutan {jenis} adalah {ph:.2f}")
        st.info(info)

elif menu == "Tentang Aplikasi":
    st.title("Tentang Aplikasi")
    st.markdown("""
    **Apa itu pH?**  
    pH adalah ukuran konsentrasi ion hidrogen (H⁺) dalam larutan. Skala pH berkisar dari 0 (sangat asam) hingga 14 (sangat basa), dengan pH 7 bersifat netral.

    **Rumus-rumus yang digunakan:**  
    - Asam kuat: `pH = -log[H⁺]`  
    - Asam lemah: `pH = -log(√(Ka × [HA]))`  
    - Basa kuat: `pOH = -log[OH⁻]` lalu `pH = 14 - pOH`  
    - Basa lemah: `pOH = -log(√(Kb × [B]))` lalu `pH = 14 - pOH`
    """)
