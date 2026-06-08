# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "43faa9a0-6c16-4da5-b775-2b9686c6b751",
# META       "default_lakehouse_name": "lh_silver_exercises",
# META       "default_lakehouse_workspace_id": "207014b0-6859-4102-9acc-9aafb600dfc6",
# META       "known_lakehouses": [
# META         {
# META           "id": "a4610c95-0122-4f30-9a17-639f2aace34b"
# META         },
# META         {
# META           "id": "43faa9a0-6c16-4da5-b775-2b9686c6b751"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# =============================================================
# STAP 1: Silver tabellen registreren als temp views (nodig voor beperking temp view + shortcut)
# =============================================================
spark.table("Sales.SalesOrderDetail").createOrReplaceTempView("silver_sales")
spark.table("Product.Product").createOrReplaceTempView("silver_product")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- =============================================================
# MAGIC -- STAP 2: Gold staging berekenen
# MAGIC --
# MAGIC -- date_sk: silver gebruikt yyyymmddHH (uurlijk), gold gebruikt
# MAGIC -- yyyymmdd (dag-niveau). We delen door 100 met integer-deling.
# MAGIC -- OrderDate in AW heeft geen tijdcomponent → uur is altijd 0,
# MAGIC -- dus: date_sk silver = yyyymmdd00 → / 100 = yyyymmdd.
# MAGIC --
# MAGIC -- StandardCost en Margin: we joinen op product_sk (niet op ProductID)
# MAGIC -- zodat we de kostprijs ophalen die geldig was op het moment van
# MAGIC -- de verkoop — dezelfde SCD2-versie als in de silver fact.
# MAGIC -- =============================================================
# MAGIC CREATE OR REPLACE TEMP VIEW stg_fact_sales AS
# MAGIC SELECT
# MAGIC     uuid()                                                          AS sales_sk,
# MAGIC     CAST(s.date_sk / 100 AS INT)                                   AS date_sk,
# MAGIC     s.product_sk,
# MAGIC     s.customer_loc_sk,
# MAGIC     s.SalesOrderID,
# MAGIC     s.SalesOrderDetailID,
# MAGIC     CAST(s.OrderDate AS DATE)                                      AS OrderDate,
# MAGIC     s.CustomerID,
# MAGIC     s.Status,
# MAGIC     s.SubTotal,
# MAGIC     s.TaxAmt,
# MAGIC     s.Freight,
# MAGIC     s.TotalDue,
# MAGIC     s.ProductID,
# MAGIC     s.OrderQty,
# MAGIC     s.UnitPrice,
# MAGIC     s.UnitPriceDiscount,
# MAGIC     s.LineTotal,
# MAGIC     p.StandardCost,
# MAGIC     s.LineTotal - (s.OrderQty * p.StandardCost)                    AS Margin,
# MAGIC     CASE
# MAGIC         WHEN s.LineTotal > 0
# MAGIC         THEN CAST((s.LineTotal - (s.OrderQty * p.StandardCost)) / s.LineTotal AS DECIMAL(10,4))
# MAGIC         ELSE NULL
# MAGIC     END                                                         AS MarginPct
# MAGIC FROM silver_sales s
# MAGIC LEFT JOIN silver_product p
# MAGIC     ON s.product_sk = p.product_sk;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- =============================================================
# MAGIC -- STAP 3: Wegschrijven naar FactSales (volledige herlaad)
# MAGIC -- Silver beheert de incrementaliteit en deduplicatie.
# MAGIC -- Gold leest altijd de volledige silver fact en herlaadt.
# MAGIC -- =============================================================
# MAGIC INSERT OVERWRITE lh_gold_exercises.Sales.FactSales
# MAGIC SELECT
# MAGIC     sales_sk,
# MAGIC     date_sk,
# MAGIC     product_sk,
# MAGIC     customer_loc_sk,
# MAGIC     SalesOrderID,
# MAGIC     SalesOrderDetailID,
# MAGIC     current_timestamp()     AS gold_load_timestamp,
# MAGIC     OrderDate,
# MAGIC     CustomerID,
# MAGIC     Status,
# MAGIC     SubTotal,
# MAGIC     TaxAmt,
# MAGIC     Freight,
# MAGIC     TotalDue,
# MAGIC     ProductID,
# MAGIC     OrderQty,
# MAGIC     UnitPrice,
# MAGIC     UnitPriceDiscount,
# MAGIC     LineTotal,
# MAGIC     StandardCost,
# MAGIC     Margin,
# MAGIC     MarginPct
# MAGIC FROM stg_fact_sales;

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
