# Energy Data Consumption Report

OVERVIEW
- This project includes data manual extraction from the EIA for energy comsumption per fuel type in the USA along with data from Wiki regarding energy density and specific energy.
- The limitations of this project and the data pipeline relate to the EIA API due to its lack or historical data, stopping reports at 1973 despite their existing from 1950 as listed on their PDF reports. BEsides from using thier API to automae the pipeline I could have web scraped their cite, but webscraping a PDF involved convverting it to HTML and parsing through three files rather than one per document thus making it more time consuming than manual extraction of data. Though after gathering historical data manually using their API to configure future aditions could allow for the consumption metrics to be gathered and improted to the database with ease.
- The data for certain fuel types may be in different metrics such as BTU, thousand barrels per day, or billion cubic feet. Additionally, depending on the specific report, the data may relate to annual or monthly consumption. Therefore, during the data processing phase before analytics, I multiplied monthly reports by 12 to get annual consumption and converted various metrics to find a common unit of measurement. This ensures the dashboard has a consistent metric for easy comparisons.
- In the data processing phase before analytics, I loaded the existing consumption data (post-transformation) into a Spark DataFrame and trained a linear regression model to output predictive analytical data, which is then loaded into a separate table in the database. This provides greater insight into the various forms of energy and their trajectories.
- The limitations of this regression models consists of the external variables ecluded from the model. Things such as current trends, stock prices, and world events could influence the trajactory of energy consumption thus resulting in these predictiosn to become irrelevant. To prevent this future upgraded to the model such as allowing it to be inclufenced by external factors relative to the domain would allow for a more dynamic and portentaiily accurate preictin output, however, that it outside of the scope of this project.
- The Energy details table is for standardized fuel types while types such as coal and petroleum where their consumption aggregated across various subtypes haave their own details table to break down the speciify denisty and specific energy of their sub types.


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

<img width="994" alt="Screenshot 2024-09-04 at 7 40 24 PM" src="https://github.com/user-attachments/assets/526c5aa7-76d9-4e42-8495-a932ddfd3274">





Data Vizualizations:
The predictive analytcal vizualization groups the consumption by fuel category thus allowing up to view total projections for categories being non-renewable, renewable, and nuclear. Granted certain elements of each categeory are exlcuded from the report, but while most prominent were added.
