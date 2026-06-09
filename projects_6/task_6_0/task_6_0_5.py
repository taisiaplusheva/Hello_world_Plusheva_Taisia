import pandas as pd
df = pd.read_csv('projects_6/task_6_0/wild_boars.csv')



with open('projects_6/task_6_0/percentile.txt', 'w') as fl:
    for column in df.columns:
       
        if pd.api.types.is_numeric_dtype(df[column]) and column != 'boar_id':
            column_name = column.split('_')[0]

            column_def = column.split('_')[1]

            fl.write(f"Percentile 25 (Q1): {df[column].quantile(0.25):.1f} {column_def}\n")
            fl.write(f"Median 50 (Q2): {df[column].quantile(0.50):.1f} {column_def}\n")
            fl.write(f"Percentile 75 (Q3): {df[column].quantile(0.75):.1f} {column_def}\n")
            fl.write(f"Percentile 90: {df[column].quantile(0.90):.1f} {column_def}\n")
            fl.write(f"Percentile 95: {df[column].quantile(0.95):.1f} {column_def}\n")
            fl.write(f"Max: {df[column].quantile(1.00):.1f} \n\n")
            
