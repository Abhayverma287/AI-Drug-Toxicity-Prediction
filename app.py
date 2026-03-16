import streamlit as st
from predict import predict_disease

st.title("AI Target Discovery Platform")

score = st.slider("Association Score", 0.0, 1.0)

gene_code = st.number_input("Gene Code", 0, 50)

if st.button("Predict"):

    result = predict_disease(score, gene_code)

    st.success(f"Predicted Disease: {result}")