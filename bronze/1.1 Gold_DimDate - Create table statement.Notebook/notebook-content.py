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
# MAGIC -- LET OP: vervang de lakehouse UUIDs in de noteeeeeeeeeebook metadata nadat
# MAGIC -- lh_gold_exercises aangemaakt is in de Gold workspace.
# MAGIC 
# MAGIC CREATE SCHEMA IF NOT EXISTS Date;
# MAGIC 
# MAGIC 
# MAGIC CREATE TABLE lh_gold_exercises.Date.DimDate
# MAGIC (
# MAGIC     -- Primaire sleutel (dag-niveau, yyyymmdd)
# MAGIC     date_sk             INT,            -- bv. 20250330aaaaa
# MAGIC 
# MAGIC     -- Datum
# MAGIC     date                DATE,           -- bv. 2025-03-30
# MAGIC 
# MAGIC     -- Jaar / kwartaal / maand
# MAGIC     year                INT,
# MAGIC     quarter             INT,            -- 1–4
# MAGIC     month               INT,            -- 1–12
# MAGIC     month_name          STRING,         -- bv. 'March'
# MAGIC 
# MAGIC     -- Week / dag
# MAGIC     week_of_year        INT,
# MAGIC     day_of_month        INT,            -- 1–31
# MAGIC     day_of_week         INT,            -- 1 = zondag, 7 = zaterdag (Spark standaard)
# MAGIC     day_name            STRING,         -- bv. 'Sunday'
# MAGIC 
# MAGIC     -- Vlaggen
# MAGIC     is_weekend          INT,            -- 1 = weekend, 0 = weekdag
# MAGIC     is_leap_year        INT,            -- 1 = schrikkeljaar, 0 = geen
# MAGIC 
# MAGIC     -- Metadata
# MAGIC     gold_load_timestamp TIMESTAMP,      -- tijdstip van de gold load
# MAGIC 
# MAGIC     -- Berekende velden (oefening)
# MAGIC     quarter_name        STRING,         -- bv. 'Q1'
# MAGIC     year_month          STRING,         -- bv. '2025-03'
# MAGIC     month_short_name    STRING,         -- bv. 'Mar'
# MAGIC     is_weekday          INT,            -- 1 = weekdag, 0 = weekend
# MAGIC     is_month_end        INT,            -- 1 = laatste dag van de maand
# MAGIC     days_in_month       INT             -- aantal dagen in de maand
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
