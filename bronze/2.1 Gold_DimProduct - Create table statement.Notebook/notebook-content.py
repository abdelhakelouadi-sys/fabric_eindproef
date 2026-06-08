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
# MAGIC CREATE SCHEMA IF NOT EXISTS Product;
# MAGIC 
# MAGIC 
# MAGIC CREATE TABLE lh_gold_exercises.Product.DimProduct
# MAGIC (
# MAGIC     -- Surrogaatsleutel — overgenomen van silver (alle SCD2-versies bewaard)
# MAGIC     product_sk          STRING,
# MAGIC 
# MAGIC     -- SCD2 geldigheidsperiode
# MAGIC     valid_from          DATE,           -- = start_date uit silver
# MAGIC     valid_to            DATE,           -- = end_date uit silver (NULL = huidige versie)
# MAGIC     is_current          BOOLEAN,        -- true = huidige versie
# MAGIC 
# MAGIC     -- Gold metadata
# MAGIC     gold_load_timestamp TIMESTAMP,
# MAGIC 
# MAGIC     -- Product
# MAGIC     ProductID           INT,
# MAGIC     ProductName         STRING,
# MAGIC     ProductNumber       STRING,
# MAGIC     Color               STRING,
# MAGIC     ProductLine         STRING,         -- bv. 'R'
# MAGIC     ProductLine_Label   STRING,         -- bv. 'Road'
# MAGIC     Class               STRING,         -- bv. 'H'
# MAGIC     Class_Label         STRING,         -- bv. 'High'
# MAGIC     Style               STRING,         -- bv. 'U'
# MAGIC     Style_Label         STRING,         -- bv. 'Universal'
# MAGIC 
# MAGIC     -- Prijs (geldig in deze SCD2-versie)
# MAGIC     ListPrice           DECIMAL(18,4),
# MAGIC     StandardCost        DECIMAL(18,4),
# MAGIC 
# MAGIC     -- Hiërarchie
# MAGIC     SubcategoryName     STRING,
# MAGIC     CategoryName        STRING
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
