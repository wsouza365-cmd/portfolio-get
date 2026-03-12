import streamlit as st
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

st.title("📂 Colaboratório: Portfólio Digital 2026")
st.subheader("GET Professor Célio Lupparelli")

# Configuração de Autenticação
gauth = GoogleAuth()

# Tenta carregar credenciais salvas
if os.path.exists('mycreds.txt'):
    gauth.LoadCredentialsFile("mycreds.txt")

if gauth.credentials is None:
    # Configura para autenticação via link (Web)
    auth_url = gauth.GetAuthUrl()
    st.warning("⚠️ Google Drive não conectado.")
    st.write(f"1. [Clique aqui para Autorizar]({auth_url})")
    
    code = st.text_input("2. Cole o código de autorização aqui:")
    if code:
        gauth.Auth(code)
        gauth.SaveCredentialsFile("mycreds.txt")
        st.success("✅ Conectado com sucesso! Atualize a página.")
else:
    gauth.Authorize()
    drive = GoogleDrive(gauth)
    st.success("✅ Google Drive Conectado!")

    # Área de Upload
    arquivo = st.file_uploader("Escolha uma foto ou projeto:", type=['png', 'jpg', 'pdf'])
    if arquivo:
        file_drive = drive.CreateFile({'title': arquivo.name})
        file_drive.SetContentFile(arquivo.name) # Nota: Em produção real, salvaria o buffer
        # file_drive.Upload()
        st.info(f"Arquivo {arquivo.name} pronto para ser enviado!")
