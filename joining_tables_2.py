import pandas as pd

# Load data from CSV files into DataFrames
fuel_types_df = pd.read_csv('fuel_types.csv')
coal_details_df = pd.read_csv('coal_details.csv')
petroleum_details_df = pd.read_csv('petroleum_details.csv')
biofuel_details_df = pd.read_csv('biofuel_details.csv')
energy_details_df = pd.read_csv('energy_details.csv')

# Print column names for debugging
print("Fuel Types columns:", fuel_types_df.columns)
print("Coal Details columns:", coal_details_df.columns)
print("Petroleum Details columns:", petroleum_details_df.columns)
print("Biofuel Details columns:", biofuel_details_df.columns)
print("Energy Details columns:", energy_details_df.columns)

# Merge Coal Details with Fuel Types
coal_with_fuel_types_df = pd.merge(coal_details_df, fuel_types_df, 
                                   left_on='Fuel_Type_Id', 
                                   right_on='Id', 
                                   suffixes=('_coal', '_fuel_types'))

# Merge Petroleum Details with Fuel Types
petroleum_with_fuel_types_df = pd.merge(petroleum_details_df, fuel_types_df, 
                                        left_on='Fuel_Type_Id', 
                                        right_on='Id', 
                                        suffixes=('_petroleum', '_fuel_types'))

# Merge Biofuel Details with Fuel Types
biofuel_with_fuel_types_df = pd.merge(biofuel_details_df, fuel_types_df, 
                                      left_on='Fuel_Type_Id', 
                                      right_on='Id', 
                                      suffixes=('_biofuel', '_fuel_types'))

# Merge Energy Details with Fuel Types
energy_with_fuel_types_df = pd.merge(energy_details_df, fuel_types_df, 
                                     left_on='Fuel_Type_Id', 
                                     right_on='Id', 
                                     suffixes=('_energy', '_fuel_types'))

# Optionally, save the merged dataframes to CSV
coal_with_fuel_types_df.to_csv('coal_with_fuel_types.csv', index=False)
petroleum_with_fuel_types_df.to_csv('petroleum_with_fuel_types.csv', index=False)
biofuel_with_fuel_types_df.to_csv('biofuel_with_fuel_types.csv', index=False)
energy_with_fuel_types_df.to_csv('energy_with_fuel_types.csv', index=False)