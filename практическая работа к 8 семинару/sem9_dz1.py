import pandas as pd
df = pd.read_csv('california_housing_train.csv')
filtered_df=df[(df['population']>=0)&(df['population']<=5000)]
avg=filtered_df['median_house_value'].mean()