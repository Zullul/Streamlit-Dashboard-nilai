import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Nilai Siswa", layout="wide")

# Title
st.title("📊 Dashboard Nilai Siswa")

# Sidebar - Input Data Siswa
st.sidebar.header("📝 Input Data Siswa")
nama = st.sidebar.text_input("Nama Siswa")
nilai = st.sidebar.number_input("Nilai", min_value=0, max_value=100, step=1)

# Tombol untuk tambah data
if "data_siswa" not in st.session_state:
    st.session_state["data_siswa"] = pd.DataFrame(columns=["Nama", "Nilai"])

if st.sidebar.button("➕ Tambahkan"):
    if nama:
        st.session_state.data_siswa = pd.concat([
            st.session_state.data_siswa,
            pd.DataFrame([[nama, nilai]], columns=["Nama", "Nilai"])
        ], ignore_index=True)
        st.sidebar.success(f"Data '{nama}' ditambahkan!")

# Tampilkan tabel
st.subheader("📋 Data Siswa")
st.dataframe(st.session_state.data_siswa, use_container_width=True)

# Analisis
if not st.session_state.data_siswa.empty:
    df = st.session_state.data_siswa
    rata2 = df["Nilai"].mean()
    nilai_max = df["Nilai"].max()
    nilai_min = df["Nilai"].min()
    siswa_tertinggi = df[df["Nilai"] == nilai_max]["Nama"].values[0]
    siswa_terendah = df[df["Nilai"] == nilai_min]["Nama"].values[0]

    st.markdown("### 📈 Statistik Nilai")
    col1, col2, col3 = st.columns(3)
    col1.metric("🎯 Rata-rata", f"{rata2:.2f}")
    col2.metric("🏅 Nilai Tertinggi", f"{nilai_max} ({siswa_tertinggi})")
    col3.metric("📉 Nilai Terendah", f"{nilai_min} ({siswa_terendah})")

    # Grafik
    st.markdown("### 📊 Grafik Nilai")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(df["Nama"], df["Nilai"], color="skyblue")
    ax.set_xlabel("Nama")
    ax.set_ylabel("Nilai")
    ax.set_title("Grafik Nilai Siswa")
    st.pyplot(fig)

else:
    st.info("Masukkan data siswa untuk mulai analisis.")
