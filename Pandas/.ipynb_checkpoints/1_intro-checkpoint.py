import pandas as pd

df = pd.read_csv(
    '/home/kevinxu95/Documents/Data/developer_survey_2019/survey_results_public.csv')

schema_df = pd.read_csv(
	'/home/kevinxu95/Documents/Data/developer_survey_2019/survey_results_schema.csv')

print(df.tail(10))

print(df.shape)

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

print(schema_df)