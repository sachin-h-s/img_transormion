from img_function import *
import streamlit as st
from PIL import Image
import cv2
import numpy as np



def main():
    st.header("Welcome to image transformation with Opencv")
    file_uploaded=st.file_uploader("please upload an image file",type=['jpg','jpeg','png'])
    if file_uploaded is not None:
        image= Image.open(file_uploaded)
        image_cv2=np.array(image)
        image_cv2=cv2.cvtColor(image_cv2,cv2.COLOR_BGR2BGRA)

        option= st.selectbox('Select the transformation you want to apply',('select','Affine','Rotation','Flipping'))
        st.write('you selected:',option)

        if option == "Select":
            pass
        elif option == "Affine":
            st.header("Input")
            st.image(image)

            st.markdown("Image after **affine transformation** :wave:")
            st.image(warpaffine(image_cv2))

        elif option == "Rotation":
            st.header("Input")
            st.image(image)

            ang=st.slider("Select the angle of rotation",min_value=0,max_value=360)
            st.write(f"Slider value: {ang} degrees")

            st.markdown("Image after **rotation** ")
            st.image(img_rotation(image_cv2,ang))

        elif option == "Flipping":
            st.header("Input")
            st.image(image)

            flip_out = st.selectbox("Select an option:", ('Select',0,1,-1))
            st.write("You selected:",flip_out)

            if flip_out == 'Select':
                pass
            else:
                st.header("Flipped image ")
                st.image(img_flipping(image_cv2, flip_out))


        else:
            pass

if __name__ == "__main__":
    main()







