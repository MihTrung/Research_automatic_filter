import pandas as pd
from pathlib import Path
from function import formToDayOfYear, remove_duplicate_title, remove_short_research, remove_inferior_research, get_eng_research, remove_review_or_survey_research

input_path = Path(__file__).parent / "input" / "Raw_data.csv"

df = pd.read_csv(input_path, encoding='latin1')

#! excluse usless columns
filter_df = df[[
        'DOI', 'Language', 'Article Title', 'Abstract', 'Times Cited, All Databases', 'Publication Year', 'Publication Date', 'Number of Pages'
     ]]

#! normalize day columns
filter_df = formToDayOfYear(filter_df, 'Publication Date')

#! remove duplicate researchs
filter_df, removedDuplicateCount, numResearchAfterDedup = remove_duplicate_title(filter_df)
print(f'I removed {removedDuplicateCount} duplicate research!')
print(f'Now it has {numResearchAfterDedup} research!')
print("-"*10)

#! remove short researchs
filter_df, removeShortResearchCount, numResearchAfterRemoveShort = remove_short_research(filter_df)
print(f'I removed {removeShortResearchCount} short researchs !!')
print(f'Now it has {numResearchAfterRemoveShort} researchs !!!')
print("-"*10)

#! remove inferior researchs
filter_df, removeInferiorResearchCount, numResearchAfterRemoveInferior = remove_inferior_research(filter_df)
print(f'I removed {removeInferiorResearchCount} inferior researchs !!')
print(f'Now it has {numResearchAfterRemoveInferior} researchs !!!')
print("-"*10)

#! get ENG researchs
filter_df, numEngCount = get_eng_research(filter_df)
print(f'I get {numEngCount} English researchs !!')
print(f'Now it has {numEngCount} researchs !!!')
print("-"*10)

#! remove survey or review researchs
filter_df, removeSurveyOrReviewResearch, numResearchAfterRemoveSurveyOrReview = remove_review_or_survey_research(filter_df)
print(f'I removed {removeSurveyOrReviewResearch} survey and review researchs !!')
print(f'Now it has {numResearchAfterRemoveSurveyOrReview} researchs !!!')
print("-"*20)

print('Done!')