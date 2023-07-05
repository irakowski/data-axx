# Databricks notebook source
# MAGIC %md
# MAGIC Databricks notebooks provide a number of utility commands for configuring and interactiving with  the environment: dbutils docs
# MAGIC

# COMMAND ----------

dbutils.help()

# COMMAND ----------

# List out directories of files from Python cell
dbutils.fs.ls('/databricks-datasets/')

# COMMAND ----------

# MAGIC %md
# MAGIC https://docs.databricks.com/dbfs/databricks-datasets.html?searchString=&from=0&sortby=_score&orderBy=desc&pageNo=1&aggregations=%5B%5D&uid=7dc8d13f-90bb-11e9-98a5-06d762ad9a62&resultsPerPage=10&exactPhrase=&withOneOrMore=&withoutTheWords=&pageSize=10&language=en&state=1&suCaseCreate=false#sample-datasets
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## display()
# MAGIC
# MAGIC When running SQL queries from cells, results will always be displayed in a rendered tabular format. When we have tabular data returned by a Python cell, we can call `display` to get the same tupe of preview.
# MAGIC
# MAGIC Wrapping previous call with `display`
# MAGIC

# COMMAND ----------

display(dbutils.fs.ls('/databricks-datasets/'))

# COMMAND ----------

# MAGIC %md
# MAGIC
