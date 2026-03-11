import streamlit as st

st.set_page_config(page_title="Portfólio GET Célio Lupparelli", layout="wide")

st.title("📂 Colaboratório: Portfólio Digital 2026")
st.subheader("GET Professor Célio Lupparelli")

menu = ["Capa", "Projetos", "Planejamentos", "Galeria por Período", "Mural Retrospectiva 2026"]
escolha = st.sidebar.selectbox("Navegação:", menu)

if escolha == "Capa":
    st.info("Bem-vindo, Professor Wagner! Selecione uma pasta ao lado para organizar seus documentos.")
    st.image("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=500")

elif escolha == "Mural Retrospectiva 2026":
    st.header("🎨 Mural de Destaques do Ano")
    st.write("Fotos marcadas como destaque aparecerão aqui.")

else:
    st.header(f"Seção: {escolha}")
    periodo = st.selectbox("Período:", ["1º Bim", "2º Bim", "3º Bim", "4º Bim"])
    destaque = st.checkbox("⭐ Destaque para o Mural Final?")
    arquivo = st.file_uploader("Subir arquivos", accept_multiple_files=True)
    if st.button("Confirmar Envio"):
        st.success("Arquivo recebido!")
