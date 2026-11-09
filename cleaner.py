import os
import pandas as pd

def load_file(file_path):
    """Loads CSV or Excel files dynamically based on extension."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext == '.csv':
        return pd.read_csv(file_path)
    elif ext in ['.xlsx', '.xls']:
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format: '{ext}'")

def save_file(df, output_path):
    """Saves DataFrame to CSV or Excel depending on output path extension."""
    _, ext = os.path.splitext(output_path)
    ext = ext.lower()

    if ext == '.csv':
        df.to_csv(output_path, index=False)
    elif ext in ['.xlsx', '.xls']:
        df.to_excel(output_path, index=False)
    else:
        raise ValueError(f"Unsupported output format: '{ext}'")

def clean_data(df, drop_dups=True, clean_headers=True, fill_nums=True):
    """Applies customizable data cleaning steps."""
    cleaned_df = df.copy()

    # Step 1: Standardize column headers
    if clean_headers:
        cleaned_df.columns = cleaned_df.columns.str.strip().str.lower().str.replace(' ', '_')
        print(" -> Column headers standardized.")

    # Step 2: Trim extra spaces in text fields
    text_cols = cleaned_df.select_dtypes(include=['object']).columns
    for col in text_cols:
        cleaned_df[col] = cleaned_df[col].astype(str).str.strip()
    print(" -> Whitespace trimmed from text columns.")

    # Step 3: Handle missing numerical values
    if fill_nums:
        numeric_cols = cleaned_df.select_dtypes(include=['number']).columns
        cleaned_df[numeric_cols] = cleaned_df[numeric_cols].fillna(0)
        print(" -> Missing numerical values filled with 0.")

    # Step 4: Remove duplicate rows
    if drop_dups:
        initial_rows = len(cleaned_df)
        cleaned_df = cleaned_df.drop_duplicates()
        removed = initial_rows - len(cleaned_df)
        print(f" -> Removed {removed} duplicate row(s).")

    return cleaned_df

def run_interactive_cleaner():
    """Interactive command-line interface for the file cleaner."""
    print("========================================")
    print("   SMART FILE CLEANER - VERSION 0.4    ")
    print("========================================\n")

    input_path = input("Enter path to input file (CSV/Excel): ").strip('"')
    if not os.path.exists(input_path):
        print("Error: File path does not exist.")
        return

    try:
        df = load_file(input_path)
        print(f"File loaded successfully! ({len(df)} initial rows)\n")
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    # User options
    print("Select Cleaning Options (y/n):")
    clean_headers = input("Standardize column names? (y/n): ").strip().lower() == 'y'
    fill_nums = input("Fill missing numeric values with 0? (y/n): ").strip().lower() == 'y'
    drop_dups = input("Remove duplicate rows? (y/n): ").strip().lower() == 'y'

    output_path = input("\nEnter output file name/path (e.g., cleaned_data.xlsx): ").strip('"')

    print("\nProcessing...")
    cleaned_df = clean_data(df, drop_dups=drop_dups, clean_headers=clean_headers, fill_nums=fill_nums)

    try:
        save_file(cleaned_df, output_path)
        print(f"\nSuccess! Cleaned file saved to '{output_path}' ({len(cleaned_df)} final rows).")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    run_interactive_cleaner()
