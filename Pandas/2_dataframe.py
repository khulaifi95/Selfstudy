import pandas as pd

df = pd.read_csv(
    '/home/kevinxu95/Documents/Data/developer_survey_2019/survey_results_public.csv')

print(df.columns)

print(df['Hobbyist'])

print(df.Hobbyist)

print(df.loc[0:2, 'Hobbyist':'Employment'])

print(df.iloc[0:2, 0:2])