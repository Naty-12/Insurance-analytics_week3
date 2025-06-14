import pandas as pd
import numpy as np

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    df = df[df['TotalClaims'] > 0].copy() 
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')
    df['TransactionYear'] = df['TransactionMonth'].dt.year
    df['RegistrationYear'] = pd.to_numeric(df['RegistrationYear'], errors='coerce')
    df['Vehicle_age'] = df['TransactionYear'] - df['RegistrationYear'] 
    df['Log_TotalClaims'] = np.log(df['TotalClaims'])# Add parentheses here to call the method
    return df

def save_clean_data(df, output_filepath):
    df.to_csv(output_filepath, index=False)
