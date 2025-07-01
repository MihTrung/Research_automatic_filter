import pandas as pd
import datetime
import re
from langdetect import detect

def formToDayOfYear(df, nameCol, outputCol='Day of year'):
    defaultYear = datetime.datetime.now().year

    def dayParse(value):
        if pd.isnull(value) or str(value).strip() == '':
            return 0  

        s = str(value).strip().upper()

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
    sorted_df = df.sort_values(by=[title_col, year_col, day_col], ascending=[True, True, True])
    
    #* remove duplicate rows (only keep the newest)
    dedup_df = sorted_df.drop_duplicates(subset=[title_col], keep='first')
    
    #* count the nums of removed rows
    removed_count = len(df) - len(dedup_df)
    num_reseach = len(dedup_df)

    return dedup_df.reset_index(drop=True), removed_count, num_reseach

def remove_short_research(df, page_col='Number of Pages', min_pages=5):
    filtered_df = df[df[page_col] >= min_pages].copy()
    removed_count = len(df) - len(filtered_df)
    num_research = len(filtered_df)

    return filtered_df.reset_index(drop=True), removed_count, num_research

def remove_inferior_research (df, time_cited = 'Times Cited, All Databases', year_col='Publication Year'):

    current_year = datetime.datetime.now().year
    #* Keep the superior research
    mask = (((current_year - df[year_col] < 1) | (df[time_cited] > 5)))
    filtered_df = df[mask].copy()
    removed_count = len(df) - len(filtered_df)
    num_research = len(filtered_df)

    return filtered_df.reset_index(drop=True), removed_count, num_research

def get_eng_research (df, abstract = 'Abstract'):

    def is_english(text):
        try:
            return detect(str(text)) == 'en'
        except:
            return False

    #* keep english research
    mask = df[abstract].apply(is_english)
    filtered_df = df[mask].copy()
    get_count = len(filtered_df)

    return filtered_df.reset_index(drop=True), get_count

def remove_review_or_survey_research(df, abstract='Abstract'):
    #* remove research has "review" or "survey"
    def is_review_or_survey(text):
        if pd.isnull(text):
            return False
        text_lower = str(text).lower()
        return ('review' in text_lower) or ('survey' in text_lower)

    mask = ~df[abstract].apply(is_review_or_survey)
    filtered_df = df[mask].copy()
    removed_count = len(df) - len(filtered_df)
    num_research = len(filtered_df)
    return filtered_df.reset_index(drop=True), removed_count, num_research
