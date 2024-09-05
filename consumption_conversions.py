import pandas as pd

def convert_units(row):
    fuelType = row["Fuel_Type_Id"]
    
    # One billion cubic feet = 1.036 trillion BTU
    # Fuel_Type_Id = 1
    if fuelType == 1:
        row['Consumption'] = row['Consumption'] * 1.036
        row['Units'] = 'Trillion BTU'
        return row
        
    # Thousand barrels per Day fisrt multiply by days in the year 365, 1,000 barrels = 5,684,000,000 BTU
    # Fuel_Type_Id = 2
    elif fuelType == 2:
        row['Consumption'] = (row['Consumption'] * 365) * 0.005684
        row['Units'] = 'Trillion BTU'
        return row
    
    # Thousand Short tons = 18,820,000,000 BTU
    # Fuel_Type_Id = 3
    elif fuelType == 3:
        row['Consumption'] = row['Consumption'] * 0.01882
        row['Units'] = 'Trillion BTU'
        return row
        
    # Million pounds of uranium oxide, multiply by 17.3 to get Trillion BTU
    # Fuel_Type_Id = 9
    elif fuelType == 9:
        row['Consumption'] = row['Consumption']  * 17.3
        row['Units'] = 'Trillion BTU'
        return row
    
    else:
        return row


if __name__ == '__main__':
    df = pd.read_csv('Energy_Consumption.csv')

    converted_df = df.apply(convert_units, axis = 1)
    converted_df['Consumption'] = converted_df['Consumption'].round(2)
    converted_df.to_csv('Converted_Energy_Consumption.csv', index = False)


