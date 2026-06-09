import pandas as pd
df = pd.read_csv('projects_6/task_6_0/wild_boars.csv')

numeric_df = df.select_dtypes(include='number').drop(columns='boar_id')

with open('projects_6/task_6_0/task_7_result.txt', 'w') as file:
    for column in numeric_df.columns:
        variance = numeric_df[column].var()
        std = numeric_df[column].std()
        variation_coeff = std / numeric_df[column].mean() * 100

        file.write(
            f'{column}: variance = {variance:.2f}, '
            f'std = {std:.2f}, '
            f'variation coefficient = {variation_coeff:.2f}%\n'
        )