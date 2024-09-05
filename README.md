# Energy Data Consumption Report

OVERVIEW

This project involves manually extracting data from the EIA regarding energy consumption per fuel type in the USA, along with data from Wikipedia on energy density and specific energy.

The project's limitations and those of the data pipeline are related to the EIA API, which lacks historical data, with reports available only from 1973 despite existing data from 1950 as indicated in their PDF reports. While automating the pipeline using their API was a possibility, web scraping their site would have been more complex due to the need to convert and parse multiple PDF files into HTML, making it more time-consuming than manual extraction. However, after gathering historical data manually, using the API to automate future updates could facilitate the collection and importation of consumption metrics into the database.

The data for certain fuel types may be reported in different metrics, such as BTU, thousand barrels per day, or billion cubic feet. Additionally, data may be reported annually or monthly. To ensure consistency for the dashboard, I converted monthly reports to annual figures by multiplying by 12 and standardized various metrics to a common unit of measurement.

During the data processing phase before analytics, I loaded the transformed consumption data into a Spark DataFrame and trained a linear regression model to generate predictive analytics, which were then loaded into a separate database table. This approach provides deeper insights into various forms of energy and their consumption trajectories.

The limitations of the regression model include the exclusion of external variables. Factors such as current trends, stock prices, and global events can influence energy consumption trajectories, potentially rendering predictions less accurate. To address this, future upgrades to the model could incorporate external factors relevant to the domain, resulting in a more dynamic and potentially accurate prediction output. However, this is outside the scope of this project.

The Energy_Details table is designed for standardized fuel types. For types like coal and petroleum, where consumption is aggregated across various subtypes, separate detail tables break down the specifics of energy density and specific energy for each subtype.


FEATURES

Step 1
- Gathering data from the EIA for total annual consumption for specific fuel types. Also gathering data for fuel type such as energy density and specific energy, account for unique tables for petroleum and coal.
- The non-renewable fuel types being included are Petroleum, Natural Gas, Coal.
- The Renewable energy fuel types being included are Solar, Wind, Hyodroelectric, Wood and Biofuels, thus excluding both waste and geothermal.
- The nuclear energy fuiel is focused on uranium, since only uranium-235 and Plutionium-239 are used in the mass production of energy bu uranium is far more prevelant due to its natural abundance, ease of use, and existing infrastructure.

Step 2
- Importing the data gathered from the sources into a python script as csv files.
- Loading them into dataframes and commiting transformation on their metrics for consistant and accurant annual consumption metrics.
- Training a Spark linear reression model to output predictive analytics for the final table in the database.
- Configure docker containers, network, and volume to host MySQL database and phpmyadmin.
- Load the data into their correspodning tables in the MySQL DB, hosted in a Docker container for ease of use and portability.

Step 3
- Sync the tableasu dashboard appliaction to the MysSql container.
- Create vizualization in the tableau dashbaord.

MySQL Entity Relationship Diagram:
It may seem like a star schema where the Fuel_Types table acts as the fact table with surrounding dimension tables, but this isn’t accurate. The Fuel_Types table does not contain foreign keys to other tables, so it is not a fact table. The actual fact tables are the Energy_Consumption and Predicted_Consumption tables, which store foreign keys referencing the Fuel_Types table.

The Fuel_Types table serves as the main dimension table. The detail tables, such as Coal_Details, Petroleum_Details, Energy_Details, and Biofuel_Details, are normalized extensions of the Fuel_Types table. These detail tables provide additional information for specific fuel types, including fuel subtypes and corresponding energy density or specific energy, where applicable. For many renewable resources, these metrics are not relevant and, therefore, are not included.

![Screenshot 2024-09-04 at 11 32 34 PM](https://github.com/user-attachments/assets/d119e7be-ff1b-4eee-98ae-9a75e1419a01)





Data Vizualizations:
The predictive analytcal vizualization groups the consumption by fuel category thus allowing up to view total projections for categories being non-renewable, renewable, and nuclear. Granted certain elements of each categeory are exlcuded from the report, but while most prominent were added.
