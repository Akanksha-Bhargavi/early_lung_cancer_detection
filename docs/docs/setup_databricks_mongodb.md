
# Databricks and MongoDB Atlas Setup Guide

## Databricks

1. **Create a New Cluster**
   - Go to the Clusters tab in Databricks.
   - Click **Create Cluster** and name it `Project`.
   - Under **Libraries**:
     - For **PyPI**, install the following packages:
       - `pymongo`
       - `pyspark`
     - For **Maven**, install the following MongoDB Spark Connector:
       - `org.mongodb.spark:mongo-spark-connector_2.12:3.0.1`
   - Launch the cluster.

2. **Attach and Run Your PySpark Code in a Notebook**
   - Create a new notebook in Databricks.
   - Attach the `Project` cluster to this notebook by selecting it from the dropdown at the top.
   - Paste your PySpark code into the notebook cells.
   - Run each cell to execute your code.

## MongoDB Atlas

1. **Start Your MongoDB Cluster**
   - Log into your MongoDB Atlas account.
   - Navigate to your Clusters and ensure your cluster is started and running.

2. **Set Up Network Access**
   - Go to **Network Access** in MongoDB Atlas.
   - Click **Add IP Address**.
   - To allow access from anywhere, enter `0.0.0.0/0` and save the change.
   
3. **Retrieve MongoDB Connection String**
   - Go to **Database Access** and ensure you have a user created with the required permissions.
   - Copy the MongoDB connection string to use in your PySpark code.
   
> **Note:** Ensure your connection string has the username and password filled in for seamless integration with Databricks.
