import pandas as pd

def clean_dataset(file_path, output_path):
    print("--- Starting File Cleaning Process ---")
    

    df = pd.read_csv(file_path)
    initial_rows = len(df)
    print(f"Original row count: {initial_rows}")

   )
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    print("✓ Column names standardized (lowercased & underscores added)")

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

   
    df.to_csv(output_path, index=False)
    print(f"--- Success! Clean file saved to '{output_path}' ---")
    print(f"Final row count: {final_rows}")


if __name__ == "__main__":
    clean_dataset('sample_dirty_data.csv', 'cleaned_output_v2.csv')
