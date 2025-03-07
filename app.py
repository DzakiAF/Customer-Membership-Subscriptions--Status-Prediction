import streamlit as st
import page
import predict
from predict import label_encode_column

with st.sidebar:
    st.title('Navigation')
    navigation = st.selectbox("Page", ["EDA", "Predict Customer Membership"])

if navigation == "EDA":
    page.run()
else:
    predict.run()