import pandas as pd
df = pd.read_csv('projects_6/task_6_0/wild_boars.csv')


with open('projects_6/task_6_0/mean.txt', 'w') as fl:
    fl.write(df.drop(columns='boar_id').mean(numeric_only=True).to_string())