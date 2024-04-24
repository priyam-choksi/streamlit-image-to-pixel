import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

st.title('Image to Pixels')
#sample = Image.open('sample.png')
#st.image(sample, caption='smaple image', width=400)
st.subheader('🎨This streamlit app allows you to covert any png/jpg/jpeg images into pixel art.')
st.caption('Upload your image, and this app will automatically generate a pixel art for you. Also, you can adjust color / grid with the slidebars.')

uploaded_file = st.file_uploader("Choose a image file", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
  img = Image.open(uploaded_file)
  h, w = img.size
  c = st.slider('Number of colors to use', 1, 256, 100)
  g = st.slider('Grid size', 1, min([h,w]), 50)
  img = img.convert('P', palette=Image.ADAPTIVE, colors=c)
  img=img.resize((g, int(g / h * w)),Image.BILINEAR)
  res=img.resize((500,int(500/ h * w)), Image.NEAREST)
  st.image(res, caption='Output Image', width=200)
