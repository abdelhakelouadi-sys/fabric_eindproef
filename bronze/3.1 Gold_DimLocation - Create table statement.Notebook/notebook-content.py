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
# MAGIC CREATE SCHEMA IF NOT EXISTS Location;
# MAGIC 
# MAGIC 
# MAGIC CREATE TABLE lh_gold_exercises.Location.DimLocation
# MAGIC (
# MAGIC     -- Surrogaatsleutel — overgenomen van silver (alle SCD2-versies bewaard)
# MAGIC     customer_loc_sk     STRING,
# MAGIC 
# MAGIC     -- SCD2 geldigheidsperiode
# MAGIC     valid_from          DATE,           -- = start_date uit silver
# MAGIC     valid_to            DATE,           -- = end_date uit silver (NULL = huidige versie)
# MAGIC     is_current          BOOLEAN,        -- true = huidige versie
# MAGIC 
# MAGIC     -- Gold metadata
# MAGIC     gold_load_timestamp TIMESTAMP,
# MAGIC 
# MAGIC     -- Klant
# MAGIC     CustomerID          INT,
# MAGIC 
# MAGIC     -- Adres
# MAGIC     City                STRING,
# MAGIC     PostalCode          STRING,
# MAGIC 
# MAGIC     -- Regio / land
# MAGIC     StateProvinceName   STRING,
# MAGIC     CountryRegionCode   STRING,         -- bv. 'DE', 'US', 'FR'
# MAGIC     CountryName         STRING,
# MAGIC 
# MAGIC     -- Weerkoppeling
# MAGIC     -- OpenWeatherCity is de join-sleutel naar FactWeather.
# MAGIC     -- Meerdere klanten per stad zijn mogelijk → many-to-many in Power BI.
# MAGIC     OpenWeatherCity     STRING,
# MAGIC     Latitude            STRING,
# MAGIC     Longitude           STRING
# MAGIC )
# MAGIC USING DELTA;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE SCHEMA IF NOT EXISTS Silver;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
