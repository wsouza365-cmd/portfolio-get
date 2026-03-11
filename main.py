import streamlit as st
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

st.set_page_config(page_title="Portfólio GET Célio Lupparelli", layout="wide")

# Autenticação (Isso criará um link para você autorizar o acesso)
gauth = GoogleAuth()
# Tenta carregar credenciais salvas
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Se não houver credenciais, pede via código
    st.sidebar.warning("⚠️ Google Drive não conectado.")
    if st.sidebar.button("Conectar ao Google Drive"):
        auth_url = gauth.GetAuthUrl()
        st.sidebar.markdown(f"[Clique aqui para Autorizar]({auth_url})")
        code = st.sidebar.text_input("Cole o código de verificação aqui:")
        if code:
            gauth.Auth(code)
            gauth.SaveCredentialsFile("mycreds.txt")
            st.sidebar.success("Conectado!")
else:
    gauth.Authorize()
    st.sidebar.success("✅ Google Drive Conectado")

drive = GoogleDrive(gauth)

st.title("📂 Portfólio Digital: GET Célio Lupparelli")

menu = ["Capa", "Projetos", "Planejamentos", "Galeria", "Mural 2026"]
escolha = st.sidebar.selectbox("Navegação:", menu)

if escolha != "Capa" and escolha != "Mural 2026":
    st.header(f"Upload para: {escolha}")
    periodo = st.selectbox("Bimestre:", ["1º", "2º", "3º", "4º"])
    arquivos = st.file_uploader("Selecione os arquivos", accept_multiple_files=True)
    
    if st.button("🚀 Salvar no Google Drive"):
        if arquivos:
            for arq in arquivos:
                # Cria o arquivo no Drive
                gfile = drive.CreateFile({'title': f"{escolha}_{periodo}_{arq.name}"})
                gfile.SetContentFile(arq.name) # Envia o arquivo
                gfile.Upload()
                st.success(f"Arquivo '{arq.name}' salvo com sucesso!")
        else:
            st.error("Selecione um arquivo primeiro.")
