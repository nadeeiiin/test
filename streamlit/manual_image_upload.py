import streamlit as st
from PIL import Image
from clf import predict
from pathlib import Path


def show_manual_image_upload():
    

    # Setze den absoluten Pfad des aktuellen Verzeichnisses
    dir = Path(__file__).resolve().parent

    # Pfad zur CSV-Datei 
    path_to_model = dir.parent / 'streamlit' / 'only_best_model_2025-01-04_11-05-04.pth' 
    
    
    #st.set_option('deprecation.showfileUploaderEncoding', False)

    #image uploader
    file_up = st.file_uploader("Upload an image", type="jpg")

    if file_up is not None:
        image = Image.open(file_up)
        st.image(image, caption='Uploaded Image.', use_container_width=True)
        st.write("")
        st.write("Just a second...")
        labels = predict(file_up, path_to_model, "labels.txt") #our trained model and labels

        # print out the top 5 prediction labels with scores
        for i in labels:
            st.write("Prediction (index, name)", i[0], ",   Score: ", i[1])