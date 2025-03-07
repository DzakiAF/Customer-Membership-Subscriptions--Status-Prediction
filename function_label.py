# I made this py file so i can import it to Inference.py.
# My pipeline is using FunctionTransforme, so i need to either write this function to Inference.py or import it to Inference.py

from sklearn.preprocessing import LabelEncoder

def label_encode_column(X_train):
    le = LabelEncoder()
    return X_train.apply(lambda col: le.fit_transform(col))