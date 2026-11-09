import os
import pandas as pd


def clean_headers(df):
  """Standardizes column names: lowercase, stripped, spaces replaced with underscores."""
  df.columns = (
      df.columns.astype(str).str.strip().str.lower().str.replace(' ', '_')
  )
  return df


def fill_nums(df):
  """Fills missing numeric values with 0."""
  numeric_cols = df.select_dtypes(include=['number']).columns
  df[numeric_cols] = df[numeric_cols].fillna(0)
  return df


def main():
  print('--- Smart File Cleaner (v0.5) ---')
  file_path = input('Enter path to input file (CSV/Excel): ').strip()

  # Validate file existence
  if not os.path.exists(file_path):
    print(f"[Error] The file '{file_path}' does not exist. Please check the path.")
    return

  # Load file based on extension
  try:
    if file_path.endswith('.csv'):
      df = pd.read_csv(file_path)
    elif file_path.endswith(('.xlsx', '.xls')):
      df = pd.read_excel(file_path)
    else:
      print('[Error] Unsupported file format. Please use .csv, .xlsx, or .xls')
      return
  except Exception as e:
    print(f'[Error] Could not read file: {e}')
    return

  # Track initial metrics for the audit report
  initial_row_count = len(df)
  initial_col_count = len(df.columns)

  print(f'\nSuccessfully loaded {initial_row_count} rows and {initial_col_count} columns.')

  # Interactive Toggles
  do_strip = input('Strip whitespace from text? (y/n): ').strip().lower()
  do_headers = input('Standardize column headers? (y/n): ').strip().lower()
  do_fill = input('Fill missing numeric values with 0? (y/n): ').strip().lower()
  do_dupes = input('Remove duplicate rows? (y/n): ').strip().lower()

  # Apply cleaning steps based on user choices
  if do_strip == 'y':
    # Strip whitespace from all string/object columns
    text_cols = df.select_dtypes(include=['object']).columns
    for col in text_cols:
      df[col] = df[col].astype(str).str.strip()

  if do_headers == 'y':
    df = clean_headers(df)

  if do_fill == 'y':
    df = fill_nums(df)

  duplicates_removed = 0
  if do_dupes == 'y':
    before_dupe_count = len(df)
    df = df.drop_duplicates()
    duplicates_removed = before_dupe_count - len(df)

  # Track final metrics
  final_row_count = len(df)

  # Save the cleaned file
  output_path = 'cleaned_' + os.path.basename(file_path)
  if output_path.endswith(('.xlsx', '.xls')):
    df.to_excel(output_path, index=False)
  else:
    output_path = 'cleaned_output.csv'
    df.to_csv(output_path, index=False)

  # --- VERSION 0.5: AUDIT SUMMARY REPORT ---
  print('\n' + '=' * 40)
  print('📊 DATA CLEANING AUDIT REPORT')
  print('=' * 40)
  print(f'• Initial Row Count:       {initial_row_count}')
  print(f'• Final Row Count:         {final_row_count}')
  print(f'• Duplicate Rows Removed:  {duplicates_removed}')
  print(f'• Headers Standardized:    {"Yes" if do_headers == "y" else "No"}')
  print(f'• Missing Numbers Filled:  {"Yes" if do_fill == "y" else "No"}')
  print(f'• Whitespace Stripped:     {"Yes" if do_strip == "y" else "No"}')
  print('-' * 40)
  print(f'✅ Success! Cleaned file saved as: {output_path}')
  print('=' * 40)


if __name__ == '__main__':
  main()
