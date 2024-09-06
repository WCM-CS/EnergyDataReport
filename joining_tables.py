import pandas as pd

consumption_df = pd.read_csv('Converted_Energy_Consumption.csv')
fuel_types_df = pd.read_csv('Fuel_Types.csv')
merged_df = pd.merge(consumption_df, fuel_types_df, left_on='Fuel_Type_Id', right_on='Id', suffixes=('_consumption', '_fuel_types'))


merged_df.to_csv('merged_df_m1.csv', index = False)

