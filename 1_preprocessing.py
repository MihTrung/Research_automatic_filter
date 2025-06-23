import pandas as pd
from pathlib import Path
from function import formToDayOfYear, remove_duplicate_title

input_path = Path(__file__).parent / "input" / "Raw_data.csv"

df = pd.read_csv(input_path, encoding='latin1')

#! excluse usless columns
filter_df = df[[
        'DOI', 'Language', 'Article Title', 'Abstract', 'Times Cited, All Databases', 'Publication Year', 'Publication Date', 'Number of Pages'
     ]]

#! normalize day columns
filter_df = formToDayOfYear(filter_df, 'Publication Date')

#! remove duplicate research
filter_df, removed_count = remove_duplicate_title(filter_df)
print(f'I removed {removed_count} duplicated research!')

