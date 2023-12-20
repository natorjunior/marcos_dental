import streamlit as st
import os
st.set_page_config(layout='wide')

st.title('Endodontia (projeto)')

side_sel = st.sidebar.selectbox('Selecione a página:',['ENDO/OUTROS','DENTEX'])

if side_sel == 'ENDO/OUTROS':
    col1, col2 = st.columns(2)

    with col1:
        list_img = os.listdir('dados/endo')
        select = st.selectbox('Selecione (Endo):', list_img)
        if select:
            st.header("endo")
            radio_end_marc = st.sidebar.radio('Endodontia',['Normal','Marcacao (IA)'],horizontal=False)
            if radio_end_marc =='Normal':
                img_path = os.path.join('dados/endo', select)
                st.image(img_path, caption=select, use_column_width=True)

    with col2:
        list_img = os.listdir('dados/outros')
        select = st.selectbox('Selecione (Outros):', list_img)
        if select:
            st.header("Outros")
            img_path = os.path.join('dados/outros', select)
            st.image(img_path, caption=select, use_column_width=True)
elif side_sel == 'DENTEX':
    st.title('PARCIAL DENTEX')
