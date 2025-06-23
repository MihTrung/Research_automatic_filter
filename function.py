import pandas as pd
import datetime
import re
from IPython.display import display

def formToDayOfYear(df, nameCol, outputCol='Day of year'):
    defaultYear = datetime.datetime.now().year

    def dayParse(value):
        if pd.isnull(value) or str(value).strip() == '':
            return 0  # Trường hợp giá trị rỗng hoặc null → trả về 0

        s = str(value).strip().upper()

        # Nếu chỉ có tên tháng như "JAN", "FEB" → thêm ngày = 1
        if re.fullmatch(r'[A-Z]{3}', s):
            s += ' 1'

        try:
            dt = pd.to_datetime(f"{s} {defaultYear}", format="%b %d %Y", errors='coerce')
            if pd.isnull(dt):
                return 0
            return dt.dayofyear
        except:
            return 0

    df = df.copy()
    df[outputCol] = df[nameCol].apply(dayParse)
    return df

def remove_duplicate_title(df, title_col='Article Title', year_col='Publication Year', day_col='Day of year'):
    
    #* sort the df in sequence title -> year -> day
    sorted_df = df.sort_values(by=[title_col, year_col, day_col], ascending=[True, False, False])
    
    #* remove duplicate rows (only keep the newest)
    dedup_df = sorted_df.drop_duplicates(subset=[title_col], keep='first')
    
    #* count the nums of removed rows
    removed_count = len(df) - len(dedup_df)
    
    return dedup_df.reset_index(drop=True), removed_count