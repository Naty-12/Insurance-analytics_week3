import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    df = df[df['TotalClaims'] > 0].copy()  # Add parentheses here to call the method
    return df

def save_clean_data(df, output_filepath):
    df.to_csv(output_filepath, index=False)
