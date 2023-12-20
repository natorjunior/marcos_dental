import streamlit as st
import os
st.set_page_config(layout='wide')

st.title('DENTAL')
col1, col2 = st.columns(2)

with col1:
    list_img = os.listdir('dados/endo')
    select = st.selectbox('Selecione uma imagem:', list_img)
    if select:
        st.header("endo")
        img_path = os.path.join('dados/endo', select)
        st.image(img_path, caption=select, use_column_width=True)

# A coluna col2 está vazia neste exemplo
with col2:
    list_img = os.listdir('dados/outros')
    select = st.selectbox('Selecione (Outros):', list_img)
    if select:
        st.header("Outros")
        img_path = os.path.join('dados/outros', select)
        st.image(img_path, caption=select, use_column_width=True)
