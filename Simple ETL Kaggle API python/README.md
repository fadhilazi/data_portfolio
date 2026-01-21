# 🔗 Simple ETL Python | Kaggle API to SQL Server

## 📌 Project Overview
This project demonstrates a simple **ETL pipeline built with Python** in VS Code. The purpose of this project is to understand what is an ETL and how to create a simple ETL pipeline from a data source into SQL Server for further use. This project showcases the development of an ETL pipeline designed to automate the lifecycle of data from ingestion to storage.

## What is ETL?
**ETL** stands for **Extract, Transform, and Load.** A foundational process in Data Engineering to move various data from various sources to a data warehouse or database.
- **Extract**: The process of retrieving raw data from a data source;
- **Transform**: The step where data is cleaned and formatted to ensure the data is "query ready";
- **Load**: The final step where the processed data is written into the target destination, such as a table in SQL Server.
<img src="Docs/Process.PNG" width="600"/>
From the image above we could understand the process of an ETL which extracts from a data source in this case Kaggle API and transform using Python, then Load into the target destination by connecting VS Code to SQL Server.

## The Pipeline Process
The primary language for scripting the logic and handling data manipulation we will be using is Python. It is an important step to know our device has been installed Python, in this case we are using VS Code for the source code editor.

### **1. Environment setup and API authentication**
First, we configure VS Code and install necessary libraries like pandas, sqlalchemy, and kaggle. We also ensure the Kaggle API credentials from this link [kaggle.json](https://www.kaggle.com/settings) are correctly placed to allow secure data retrieval. In the settings page you can scroll down until you find the menu **Legacy API Credentials** and click create Legacy API Key, this will download a file called Kaggle.json.

What you should do with the file is to move it into **Local Disk (C:)\Users\name\.kaggle** folder. This allows us to connect when Importing and authenticating Kaggle API to our editor.

### **2. Data Extraction**
```
import kaggle
kaggle.api.authenticate()
kaggle.api.dataset_download_files('atharvasoundankar/chocolate-sales', path='.', unzip=True)
```
The pipeline automates the flow of data from a Kaggle API source directly into a SQL Server database. By using the Chocolate Sales dataset [Chocolate Sales dataset](https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales).
After running the command, the dataset Chocolate Sales.csv will be downloaded into our folder.

- It is important to keep in mind if you want to change the dataset, in the command ...dataset_dowload_files('**CHANGE DATASET LINK**') <-- *Change the dataset link to the dataset you want*.
- ***Path='.'*** : is to keep the data files the same folder as your code
- ***unzip=True*** : the file extracted is in a zip File, so it is important to extract the csv file

After succesfully extracted the dataset from Kaggle API to our Editor, now comes the fun part in transforming the data.

### **3. Data Transformation (Python/Pandas)**

Once the raw data is in our environment, we use Pandas to:
- Inspect the data for inconsistencies.
- Rename columns for SQL compatibility (e.g., removing spaces).
- Format dates and currency values into standard numeric types.

### **4. Loading to SQL Server**

Finally, we establish a connection to SQL Server using an ODBC driver and sqlalchemy. The cleaned DataFrame is then pushed into a structured table, making it available for SQL queries or visualization tools like Power BI or Tableau.


This project demonstrates a streamlined ETL (Extract, Transform, Load) pipeline built with Python in VS Code. The pipeline automates the flow of data from a Kaggle API source directly into a SQL Server database. By using the Chocolate Sales dataset [Chocolate Sales dataset](https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales)
, this project illustrates how to bridge the gap between raw external data and a structured environment ready for analysis and business intelligence.


<br>
<br>Data source which is used in this project is from a Kaggle API which could be accessed here [Chocolate Sales dataset](https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales)


//- The process of retrieving raw data from a source—in this case, pulling a CSV file via the Kaggle API.//
