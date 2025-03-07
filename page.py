import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

def run():
    st.markdown('# MILESTONE 2')
    st.markdown('# By : Dzaki Ahmad Fardian')
    st.image('https://www.thealternativeboard.com/hubfs/bigstock-Consumer-Behavior-147822161%20%281%29.jpg')

    st.markdown('''
                # About this Project
                In this project, I created five classification models using the following algorithms: KNN, SVM, Decision Tree, Random Forest, and XGBoost. 
                The purpose of these models is to predict whether or not a customer will become a subscriber (membership). 
                Then, I evaluated each model to identify the best one. 
                ''')

    # dataframe
    st.write('# Dataset')
    st.write('Below is the dataset i used in this project.')
    df = pd.read_csv('shopping_behavior_updated.csv')
    df.drop(['Customer ID'], axis=1, inplace=True)
    df.drop(['Location'], axis=1, inplace=True)
    st.dataframe(df, hide_index=True)


    st.write('# Exploratory Data Analysis')

    # Select Box
    st.write('# Selectbox')

    # for loop for excluding Subscription Status
    list_col = []
    for col in df.columns:
        if col != "Subscription Status":
            list_col.append(col)

    # set variable 'columns' that contain selectbox.
    # select box will have items from 'list_col' from above loop.  
    columns = st.selectbox('Select which columns you want to visualize', list_col)

    st.write('Visialization')
    # final visualization
    fig = plt.figure(figsize=(10,5))
    sns.histplot(data=df, x=columns, bins=20, hue='Subscription Status')
    st.pyplot(fig)
