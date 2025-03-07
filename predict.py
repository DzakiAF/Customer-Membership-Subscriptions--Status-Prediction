import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# function for label encode as parameter for FunctionTransformer.
def label_encode_column(X_train):
    le = LabelEncoder()
    return X_train.apply(lambda col: le.fit_transform(col))

def run():
    # load model
    with open('best_model_dt.pkl', 'rb') as file_1:
        model = pickle.load(file_1)

    st.title('Subscriber Potential Prediction')

    # Form for prediction input value
    with st.form('Form'):
        st.write('Form Data Customer')
        age = st.number_input(label ="Age",
                            help ="Input customer's Age",
                            step=1, value=26, placeholder="Eg: 26")
        gender = st.text_input(label="gender",
                            help ="Input Customer's Gender",
                            placeholder="Male/Female", value='Male')
        item_purchased = st.selectbox("Select Item Purchased", ['Blouse', 'Sweater', 'Jeans', 'Sandals', 'Sneakers', 'Shirt',
                                            'Shorts', 'Coat', 'Handbag', 'Shoes', 'Dress', 'Skirt',
                                            'Sunglasses', 'Pants', 'Jacket', 'Hoodie', 'Jewelry', 'T-shirt',
                                            'Scarf', 'Hat', 'Socks', 'Backpack', 'Belt', 'Boots', 'Gloves'])
        category = st.selectbox("Select Item Purchased", ['Clothing', 'Footwear', 'Outerwear', 'Accessories'])
        purhase_amount = st.number_input(label="Purchase Amount (In USD)",
                            help ="Input Purchase Amount",
                            min_value=1, max_value=999,
                            value=13, placeholder="Eg: 5")
        size = st.select_slider(label = "Product Size",
                                options = ['S', 'M','L', 'XL'],
                                help = "Choose Product Size")
        color = st.selectbox('Select Color', ['Gray', 'Maroon', 'Turquoise', 'White', 'Charcoal', 'Silver',
                            'Pink', 'Purple', 'Olive', 'Gold', 'Violet', 'Teal', 'Lavender',
                            'Black', 'Green', 'Peach', 'Red', 'Cyan', 'Brown', 'Beige',
                            'Orange', 'Indigo', 'Yellow', 'Magenta', 'Blue'])
        season = st.selectbox("Select Season", ['Winter', 'Spring', 'Summer', 'Fall'])
        review = st.number_input(label="Review Rating",
                                    help="Input Review Rating",
                                    step=1., value=4.2, placeholder="Eg:2.7",format="%.1f")
        ship = st.selectbox("Select Shipping Type", ['Express', 'Free Shipping', 'Next Day Air', 'Standard',
                                        '2-Day Shipping', 'Store Pickup'])
        discount = st.select_slider(label = "Discount Applied",
                                options = ['No', 'Yes'],
                                help = "Using Discount?")
        promo = st.select_slider(label = "Promo Code Applied",
                                options = ['No', 'Yes'],
                                help = "Using Promo Code?")
        prev_purchase = st.number_input(label="Previous Purchase Amount (IN USD)",
                            help ="Input Previous Purchase Amount",
                            min_value=1, max_value=999,
                            value=8, placeholder="Eg: 5")
        payment = st.selectbox("Select Payment Method", ['Venmo', 'Cash', 'Credit Card', 'PayPal', 'Bank Transfer',
                                                        'Debit Card'])
        freq_purchase = st.selectbox("Select Frequency Purchases", ['Fortnightly', 'Weekly', 'Annually', 'Quarterly',
                                    'Bi-Weekly', 'Monthly', 'Every 3 Months'])
        submit_button = st.form_submit_button("Submit")
    st.write('end of form')

    # dataframe for prediction
    dict = {
    'Age':age,
    'Gender':gender,
    'Item Purchased':item_purchased,
    'Category': category,
    'Purchase Amount': purhase_amount,
    'Size': size,
    'Color': color,
    'Season':season,
    'Review Rating':review,
    'Shipping Type':ship,
    'Discount Applied': discount,
    'Promo Code Used': promo,
    'Previous Purchases':prev_purchase,
    'Payment Method': payment,
    'Frequency of Purchases':freq_purchase
    }

    df = pd.DataFrame([dict])
    st.dataframe(df, hide_index=True)

    # Prediction
    result = model.predict(df)

    # if statement for result value = Susbcribe or Not Subscribe
    # Instead of 0 or 1
    subs =""
    if result == 0:
        subs="Not Subscribe"
    else:
        subs="Subscribe"

    st.write('# Prediction Result : This Customer is ', subs)