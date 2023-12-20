import streamlit as st
import os

st.title('DENTAL')
col1, col2 = st.columns(2)

# Lista de imagens na pasta 'dados/endo'
list_img = os.listdir('dados/endo')

# Seletor para escolher uma imagem da lista
select = st.selectbox('Selecione uma imagem:', list_img)

with col1:
    st.header("Imagem Selecionada")
    img_path = os.path.join('dados/endo', select)
    st.image(img_path, caption=select, use_column_width=True)

# A coluna col2 está vazia neste exemplo
with col2:
    pass
