# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "a4610c95-0122-4f30-9a17-639f2aace34b",
# META       "default_lakehouse_name": "lh_gold_exercises",
# META       "default_lakehouse_workspace_id": "a2fdb813-2aa4-43d0-b43b-4958f086dca4",
# META       "known_lakehouses": [
# META         {
# META           "id": "a4610c95-0122-4f30-9a17-639f2aace34b"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE SCHEMA IF NOT EXISTS Weather;
# MAGIC 
# MAGIC 
# MAGIC CREATE TABLE lh_gold_exercises.Weather.FactWeather
# MAGIC (
# MAGIC     -- Surrogaatsleutel
# MAGIC     weather_sk          STRING,
# MAGIC 
# MAGIC     -- Foreign keys naar dimensies
# MAGIC     date_sk             INT,            -- yyyymmdd → DimDate
# MAGIC 
# MAGIC     -- Weerkoppeling naar DimLocation
# MAGIC     -- In Power BI: DimLocation.OpenWeatherCity = FactWeather.openweather_city
# MAGIC     -- (many-to-many via bi-directionele filtering)
# MAGIC     openweather_city    STRING,
# MAGIC 
# MAGIC     -- Gold metadata
# MAGIC     gold_load_timestamp TIMESTAMP,
# MAGIC 
# MAGIC     -- Temperatuur — geaggregeerd over uurlijkse snapshots
# MAGIC     -- avg_temp: representatief daggemiddelde
# MAGIC     -- min_temp: koudste snapshot van de dag
# MAGIC     -- max_temp: warmste snapshot van de dag
# MAGIC     -- (NIET de temp_min/temp_max uit de API: die zijn gebied-gemiddelden,
# MAGIC     --  geen echte dagmin/-max. MIN/MAX over de 24 snapshots is correcter.)
# MAGIC     avg_temp            DECIMAL(5,2),   -- °C
# MAGIC     min_temp            DECIMAL(5,2),   -- °C
# MAGIC     max_temp            DECIMAL(5,2),   -- °C
# MAGIC     avg_feels_like      DECIMAL(5,2),   -- °C
# MAGIC 
# MAGIC     -- Atmosfeer
# MAGIC     avg_humidity        DECIMAL(5,2),   -- %
# MAGIC     avg_pressure        DECIMAL(7,2),   -- hPa
# MAGIC 
# MAGIC     -- Wind
# MAGIC     avg_wind_speed      DECIMAL(5,2),   -- m/s — daggemiddelde
# MAGIC     max_wind_speed      DECIMAL(5,2),   -- m/s — pieksnelheid
# MAGIC 
# MAGIC     -- Bewolking
# MAGIC     avg_cloud_cover     DECIMAL(5,2),   -- % bewolking
# MAGIC 
# MAGIC     -- Neerslag
# MAGIC     -- rainy_hours: aantal snapshots met weather_main = 'Rain' (max 24)
# MAGIC     --   → onderscheid tussen 2h regen vs 12h regen
# MAGIC     -- had_rain: binaire vlag voor eenvoudige filtering
# MAGIC     rainy_hours         INT,
# MAGIC     had_rain            BOOLEAN,
# MAGIC 
# MAGIC     -- Meest voorkomende weersconditie van de dag
# MAGIC     dominant_condition  STRING,         -- bv. 'Clear', 'Clouds', 'Rain'
# MAGIC 
# MAGIC     -- Datakwaliteit: aantal beschikbare snapshots (ideaal = 24)
# MAGIC     snapshot_count      INT
# MAGIC )
# MAGIC USING DELTA;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
