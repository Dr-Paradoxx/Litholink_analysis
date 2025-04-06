import pandas as pd
import os

def load_excel_data(filepath: str) -> dict:
    """
    Loads the Excel file and returns a dictionary with each sheet as a DataFrame.
    """
    sheets = pd.read_excel(filepath, sheet_name=None, engine='openpyxl')
    return sheets

def clean_litholink_main(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the Litholink_main sheet.
    - Selects important variables: Ca24, SSCaP, Ca24kg, Ca24Cr24, Cit24, Serum_Ca, Age, BMI.
    - Additional cleaning steps can be added as needed.
    """
    cols = ['Stone_Category', 'pH_category', 'Ca24', 'SSCaP', 'Ca24kg', 'Ca24Cr24', 'Cit24', 'Serum_Ca', 'Age', 'BMI']
    df_clean = df[cols].copy()
    df_clean = df_clean.dropna()
    return df_clean

def clean_variability_study(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the Variability Study sheet.
    - Filters for same day sample pairs.
    - Selects variables: Ca24, SSCaP, Ca24kg, Ca24Cr24, Cit24, Serum_Ca, pH.
    """
    df_clean = df[df['Same day sample pairs'] == 1].copy()
    cols = ['Stone_Category', 'Ca24', 'SSCaP', 'Ca24kg', 'Ca24Cr24', 'Cit24', 'Serum_Ca', 'pH']
    df_clean = df_clean[cols]
    df_clean = df_clean.dropna()
    return df_clean

def save_processed_data(df: pd.DataFrame, filename: str, folder: str = 'data/processed'):
    """
    Saves a DataFrame to CSV in the processed folder.
    """
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    df.to_csv(filepath, index=False)
