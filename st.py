import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.vgg19 import preprocess_input
from tensorflow.keras.preprocessing import image
import os
import numpy as np

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
                loaded_model = tf.keras.models.load_model('test1_vgg19_0_75.h5')
                img = image.load_img(img_path, target_size=(512, 512))
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                img_array = preprocess_input(img_array)
                pred = loaded_model.predict(img_array)
                #st.write(pred)
                if not np.argmax(pred):
                    st.success('endo (previsao da IA)', icon="✅")
                else:
                    st.error('outros (previsao da IA)', icon="🚨")
                st.image(img_path, caption=select, use_column_width=True)
                

    with col2:
        list_img = os.listdir('dados/outros')
        select = st.selectbox('Selecione (Outros):', list_img)
        if select:
            st.header("Outros")
            img_path = os.path.join('dados/outros', select)
            loaded_model = tf.keras.models.load_model('test1_vgg19_0_75.h5')
            img = image.load_img(img_path, target_size=(512, 512))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)
            pred = loaded_model.predict(img_array)
            #st.write(pred)
            if not np.argmax(pred):
                st.success('endo (previsao da IA)', icon="✅")
            else:
                st.error('outros (previsao da IA)', icon="🚨")
            st.image(img_path, caption=select, use_column_width=True)
elif side_sel == 'DENTEX':
    st.title('PARCIAL DENTEX')
