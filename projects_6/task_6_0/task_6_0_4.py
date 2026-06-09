import pandas as pd
df = pd.read_csv('projects_6/task_6_0/wild_boars.csv')

with open('projects_6/task_6_0/mode.txt', 'w') as fl:
    mode_weight = df.drop(columns='boar_id').mode().to_string()
    fl.write(mode_weight)
