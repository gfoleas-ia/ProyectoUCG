import streamlit as st
st.title("proyecto final Casa Grande")
st.sidebar.title("Parametros")
st.image("Python_logo")
import libreria_funciones as lf
uploaded_files = st.file_uploader(
    "Upload data", accept_multiple_files=True, type="csv"
)
for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write(df)
  
