import streamlit as st

# Configuração Visual
st.set_page_config(page_title="Portfólio GET Célio Lupparelli", layout="wide")

st.title("📂 Colaboratório: Portfólio Digital 2026")
st.subheader("GET Professor Célio Lupparelli")

# Menu Lateral Organizado
menu = ["Capa", "Projetos", "Planejamentos", "Galeria por Período", "Mural Retrospectiva 2026"]
escolha = st.sidebar.selectbox("Navegação:", menu)

if escolha == "Capa":
    st.info("Bem-vindo, Professor Wagner! Selecione uma pasta ao lado para organizar seus documentos e mídias.")
    st.image("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=500", caption="Tecnologia e Inovação no GET")

elif escolha == "Mural Retrospectiva 2026":
    st.header("🎨 Mural Sintetizado do Ano")
    st.write("Aqui aparecerão apenas os destaques selecionados de cada bimestre.")
    # Espaço para as fotos de destaque
    col1, col2 = st.columns(2)
    with col1: st.write("📸 Destaques 1º Semestre")
    with col2: st.write("📸 Destaques 2º Semestre")

else:
    st.header(f"Seção: {escolha}")
    
    # Sistema de Upload
    periodo = st.selectbox("Selecione o Período da Aula:", ["1º Bimestre", "2º Bimestre", "3º Bimestre", "4º Bimestre"])
    destaque = st.checkbox("⭐ Marcar como destaque para o Mural Final?")
    
    arquivo = st.file_uploader("Arraste fotos, vídeos ou PDFs aqui", accept_multiple_files=True)
    
    if st.button("Confirmar Envio"):
        if arquivo:
            st.success(f"Arquivos enviados com sucesso para a pasta {escolha} ({periodo})!")
        else:
            st.warning("Por favor, selecione um arquivo.")
