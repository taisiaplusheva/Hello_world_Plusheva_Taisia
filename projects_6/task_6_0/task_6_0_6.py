import pandas as pd
df = pd.read_csv('projects_6/task_6_0/wild_boars.csv')

q1 = df.groupby('gender')['length_cm'].quantile(0.25)
q3 = df.groupby('gender')['length_cm'].quantile(0.75)

iqr_by_gender = q3 - q1

with open('projects_6/task_6_0/iqr.txt', 'w') as file:
    for gender, iqr in iqr_by_gender.items():
        file.write(f'{gender}: {iqr:.2f}\n')

# q1 = df['weight_kg'].quantile(0.25)
# q3 = df['weight_kg'].quantile(0.75)
# iqr = q3 - q1

# print(f"Q1 (25%): {q1:.1f} kg")
# print(f"Q3 (75%): {q3:.1f} kg")
# print(f"IQR: {iqr:.1f} kg")

# import pandas as pd
# df = pd.read_csv('wild_boars.csv')

# average_weight = df.groupby('gender')['weight_kg'].mean()
# print(f"Boars average male weight is {average_weight['Male']:.2f} kilos")