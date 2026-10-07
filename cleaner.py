import os
import pandas as pd

def load_file(file_path):
    """Loads CSV or Excel files based on file extension."""
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == '.csv':
        return pd.read_csv(file_path)
    elif ext in ['.xlsx', '.xls']:
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format: '{ext}'. Please use .csv or .xlsx")

def save_file(df, output_path):
    """Saves DataFrame to CSV or Excel based on output path extension."""
    ext = os.path.splitext(output_path)[1].lower()
    
    if ext == '.csv':
        df.to_csv(output_path, index=False)
    elif ext in ['.xlsx', '.xls']:
        df.to_excel(output_path, index=False)
    else:
        raise ValueError(f"Unsupported output format: '{ext}'")

def clean_dataset(file_path, output_path):
    print(f"--- Starting Cleaning Process for: {file_path} ---")
 
    df = load_file(file_path)
    initial_rows = len(df)
    print(f"Original row count: {initial_rows}")

    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    print("✓ Column names standardized")


    text_cols = df.select_dtypes(include=['object']).columns
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip()
    print("✓ Extra whitespace removed from text cells")

    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)
    df[text_cols] = df[text_cols].fillna("N/A")
    print("✓ Missing values handled (Numeric -> 0, Text -> 'N/A')")

    df = df.drop_duplicates()
    final_rows = len(df)
    removed_duplicates = initial_rows - final_rows
    print(f"✓ Removed {removed_duplicates} duplicate row(s)")

    save_file(df, output_path)
    print(f"--- Success! Clean file saved to '{output_path}' ---")
    print(f"Final row count: {final_rows}")

if __name__ == "__main__":
    clean_dataset('sample_dirty_data.csv', 'cleaned_output_v3.csv')
