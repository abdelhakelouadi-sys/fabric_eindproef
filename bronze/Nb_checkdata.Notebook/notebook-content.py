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
# MAGIC 
# MAGIC 
# MAGIC Select cl.*
# MAGIC from Location_Silver.customerlocation cl;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC DESCRIBE TABLE lh_gold_exercises.Location.DimLocation;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC INSERT OVERWRITE TABLE
# MAGIC Product.dimproduct
# MAGIC Select product_sk,
# MAGIC start_date as valid_from,
# MAGIC end_date  as valid_to,
# MAGIC current_flag as is_current,
# MAGIC CURRENT_TIMESTAMP as gold_load_timestamp,
# MAGIC ProductID,
# MAGIC ProductName,
# MAGIC ProductNumber,
# MAGIC Color,
# MAGIC ProductLine,
# MAGIC case when ProducLine = 'R' then 'Road'
# MAGIC when ProducLine = 'M' then 'Mountain'
# MAGIC when ProducLine = 'T' then 'Touring'
# MAGIC when ProducLine = 'S' then 'Standard'
# MAGIC else ''
# MAGIC end as ProductLine_Label,
# MAGIC class,
# MAGIC case class when 'H' then 'High'
# MAGIC when 'M' then 'Medium'
# MAGIC when 'L' then 'Low'
# MAGIC end as Class_Label,
# MAGIC Style,
# MAGIC case Style when 'U' then 'Universal'
# MAGIC when 'W' then 'Womens'
# MAGIC when 'M' then 'Mens'
# MAGIC end as Style_Label,
# MAGIC ListPrice,
# MAGIC StandarCost,
# MAGIC SubcategoryName,
# MAGIC CategoryName
# MAGIC From lh_silver_exercises.Product.product


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
