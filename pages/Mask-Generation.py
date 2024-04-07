import streamlit as st
from PIL import Image , ImageFilter
from utils import *

st.title("Mask Generation")

#Generate_Mask


image= st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])








if(image):
    with st.spinner("Generation mask.."):
        image = Image.open(image)
        result= Generate_Mask(image)
        st.image(image)
        #for i in range(8):
        bg_mask=result[0]['mask']
        gen= Image.composite(image,Image.new('RGB',image.size,0),bg_mask)
        st.image(gen)
        blur = gen.filter(ImageFilter.GaussianBlur(20))
        st.image(blur)
