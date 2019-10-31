source: https://github.com/commoncrawl/cc-index-table

# Query the table in Amazon Athena

First, the table needs to be imported into Amazon Athena. In the Athena Query Editor:

- create a database ccindex: CREATE DATABASE ccindex and make sure that it's selected as "DATABASE"
- edit the "create table" statement (flat or nested) and add the correct table name and path to the Parquet/ORC data on s3://. Execute the "create table" query.
- make Athena recognize the data partitions on s3://: MSCK REPAIR TABLE ccindex (do not forget to adapt the table name). This step needs to be repeated every time new data partitions - have been added.