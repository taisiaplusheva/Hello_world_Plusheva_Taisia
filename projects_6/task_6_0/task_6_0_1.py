import pandas as pd
df = pd.read_csv('projects_6/task_6_0/wild_boars.csv')
print(df['tusk_length_cm'].max())
print(df['tusk_length_cm'].min())
