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
# MAGIC CREATE SCHEMA IF NOT EXISTS Sales;
# MAGIC 
# MAGIC 
# MAGIC CREATE TABLE lh_gold_exercises.Sales.FactSales
# MAGIC (
# MAGIC     -- Surrogaatsleutel
# MAGIC     sales_sk            STRING,
# MAGIC 
# MAGIC     -- Foreign keys naar dimensies
# MAGIC     date_sk             INT,            -- yyyymmdd → DimDate
# MAGIC     product_sk          STRING,         -- → DimProduct (historische versie op moment van bestelling)
# MAGIC     customer_loc_sk     STRING,         -- → DimLocation (historische versie op moment van bestelling)
# MAGIC 
# MAGIC     -- Natuurlijke sleutels
# MAGIC     SalesOrderID        INT,
# MAGIC     SalesOrderDetailID  INT,
# MAGIC 
# MAGIC     -- Gold metadata
# MAGIC     gold_load_timestamp TIMESTAMP,
# MAGIC 
# MAGIC     -- Order-niveau maatregelen
# MAGIC     OrderDate           DATE,
# MAGIC     CustomerID          INT,
# MAGIC     Status              INT,
# MAGIC     SubTotal            DECIMAL(18,4),
# MAGIC     TaxAmt              DECIMAL(18,4),
# MAGIC     Freight             DECIMAL(18,4),
# MAGIC     TotalDue            DECIMAL(18,4),
# MAGIC 
# MAGIC     -- Regel-niveau maatregelen
# MAGIC     ProductID           INT,
# MAGIC     OrderQty            INT,
# MAGIC     UnitPrice           DECIMAL(18,4),
# MAGIC     UnitPriceDiscount   DECIMAL(18,4),
# MAGIC     LineTotal           DECIMAL(18,4),  -- = OrderQty * UnitPrice * (1 - UnitPriceDiscount)
# MAGIC     StandardCost        DECIMAL(18,4),  -- kostprijs uit DimProduct (geldig op moment van verkoop)
# MAGIC     Margin              DECIMAL(18,4),  -- LineTotal - (OrderQty * StandardCost)
# MAGIC     MarginPct           DECIMAL(10,4)   -- Margin / LineTotal (gerealiseerde marge na korting)
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
