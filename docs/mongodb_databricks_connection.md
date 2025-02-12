# MongoDB-Databricks Connection Setup

This guide provides step-by-step instructions to set up a cluster in Databricks, connect it with MongoDB, and execute your PySpark code.

---

## Databricks Setup

### 1. Create a New Cluster

1. **Navigate to the Clusters Tab**:
   - Open Databricks and go to the **Clusters** tab.

2. **Create a Cluster**:
   - Click **Create Cluster**.
   - Name the cluster as **Project**.

3. **Install Required Libraries**:
   - Under **Libraries**:
     - **For PyPI**:
       - Install the following packages:
         - `pymongo`
         - `pyspark`
     - **For Maven**:
       - Install the MongoDB Spark Connector with the following coordinates:
         ```plaintext
         org.mongodb.spark:mongo-spark-connector_2.12:3.0.1
         ```

4. **Launch the Cluster**:
   - Click **Launch** to start your cluster.

---

### 2. Attach and Run PySpark Code in a Notebook

1. **Create a New Notebook**:
   - Go to the **Workspace** tab in Databricks.
   - Click **Create** > **Notebook**.
   
2. **Attach Cluster**:
   - Select **Project** (your cluster) from the **Cluster** dropdown menu at the top of the notebook.

3. **Add and Run Code**:
   - Paste your PySpark code into the notebook cells.
   - Run each cell to execute your code.

---

## MongoDB Setup

### 1. Start Your MongoDB Cluster

1. **Log into MongoDB Atlas**:
   - Go to [MongoDB Atlas](https://cloud.mongodb.com/) and log in.

2. **Navigate to Clusters**:
   - Open your project and go to **Clusters**.
   - Ensure your cluster is started and running.

---

### 2. Set Up Network Access

1. **Go to Network Access**:
   - In MongoDB Atlas, navigate to **Network Access** in the left sidebar.

2. **Add IP Address**:
   - Click **Add IP Address**.
   - To allow access from any IP address, enter `0.0.0.0/0`.
   - Save the changes.

---


