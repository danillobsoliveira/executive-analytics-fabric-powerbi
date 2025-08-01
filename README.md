# 📊 CRM Analytics with Microsoft Fabric

This project simulates a modern CRM Analytics solution using the Microsoft Fabric platform. It involves generating synthetic data as well as integrating real-world data from a public API, storing it in a Lakehouse using the Medallion architecture, processing and transforming it with PySpark, leveraging Delta Lake versioning, automating pipelines, and building interactive dashboards with Power BI.

---

## 🚀 Technologies Used

- [Microsoft Fabric](https://www.microsoft.com/en-us/microsoft-fabric)
- Lakehouse (Delta Lake)
- Power BI
- PySpark (via Fabric notebooks)
- Pipelines do Fabric
- Python (with Faker and requests)
- SQL (DAX, Spark SQL)

---

## 🏛️ Medallion Architecture

This project follows the Medallion data architecture pattern:

### 🥉 Bronze – Raw Layer
> Storage of raw data (synthetic and real), without transformations.

| Table               | Source                      | Description                             |
|----------------------|----------------------------|----------------------------------------|
| `bronze_customer`    | Faker                      | Synthetic customer records                     |
| `bronze_products`    | Faker                      | Products with categories and pricing       |
| `bronze_sales`      | Faker                      | Simulated sales history         |
| `bronze_ibge_states`| API IBGE                   | Official list of Brazilian states           |

---

### 🥈 Silver – Clean Layer
> Cleaned data with standardized schemas, adjusted data types, and applied joins.

| Table               | Description                          |
|----------------------|------------------------------------|
| `dim_customer`        | Customer dimension               |
| `dim_product`        | Product dimension               |
| `dim_time`          | Time dimension (2 years range)         |
| `dim_geographic`       | Standardized geographic dimension    |
| `fact_sales`        | 	Fact table with keys and metrics         |

---

### 🥇 Gold – Business Layer
> Final business-ready data for aggregations and key indicators.

| Table                   | Description                           |
|--------------------------|-------------------------------------|
| `total_sales_state`   | Total sales by state          |
| `top_customers`        | Top customers by volume      |
| `top_products`           | Best-selling products              |

---

## 🔐 Security

- **Workspace-level access control** in Microsoft Fabric
- **Data masking for sensitive fields**, such as customer emails
- **Layer-based access separation**: full access to Bronze/Silver, read-only access to Gold
- Ready for **auditing and monitoring** via Fabric or Azure Purview

---

## 🕒 Data Versioning with Delta Time Travel

This project uses Delta Lake as the storage format, allowing automatic versioning of all tables. This enables:

- Restore previous versions of any table
- Audit transformations and load history
- Re-run analyses based on historical versions

Example usage in a notebook:

```sql
-- Query a previous version of the sales fact table (SQL)
SELECT * FROM silver.fato_vendas VERSION AS OF 3
```
```python
# Query a previous version using PySpark
df_v2 = spark.read.format("delta") \
    .option("versionAsOf", 3) \
    .load("Tables/silver/fact_sales")
```

## ⚙️ Pipeline Automation

All ETL processes are automated using Microsoft Fabric Pipelines.

🔁 Created Pipelines

| Pipeline                   | Steps Description                           |
|--------------------------|-------------------------------------|
| `etl_bronze_to_silver`   | Cleaning, casting, joins, write to Silver          |
| `etl_silver_to_gold`     | Aggregations and final indicators generation      |
| `api_collection_ibge`           | Real-time data collection from IBGE API              |

Each pipeline can be scheduled (e.g., daily) or triggered manually.

---

## 📊 Power BI Dashboards

- 🗺️ Sales map by state (map and bar chart)
- 📦 Top-selling products
- 👥 Most active customers
- 📉 Sales trend over time (line chart)

> Dashboards were built directly within Power BI in Fabric, using native Lakehouse connections.

📷 Dashboard screenshots are available in /imagens/dashboard.png.

---

## ⚡ Performance Best Practices

- Storage in Delta Lake (compression + versioning)
- Table partitioning in Silver and Gold layers (e.g., by state or date)
- Reusable notebook modules
- Clear separation of responsibilities across layers
- Incremental ETL with future timestamp control (optional)

---

## 📁 Project Structure

```plaintext
crm-analytics-fabric/
├── notebooks/
│   ├── geracao_dados.ipynb
│   ├── coleta_api_ibge.ipynb
│   ├── bronze_to_silver.ipynb
│   └── silver_to_gold.ipynb
├── pipelines/
│   ├── etl_bronze_to_silver.json
│   ├── etl_silver_to_gold.json
│   └── api_coleta_ibge.json
├── modelagem/
│   └── modelo_dimensional.drawio
├── imagens/
│   └── dashboard.png
├── README.md
```
---

## 🧠 Demonstrated Skills

- ✔️ Dimensional modeling (star schema)
- ✔️ Lakehouse architecture
- ✔️ Medallion architecture (Bronze → Silver → Gold)
- ✔️ ETL with PySpark
- ✔️ Delta Time Travel (data versioning)
- ✔️ Automation with Fabric Pipelines
- ✔️ Data visualization with Power BI
- ✔️ Security and performance best practices

---

**Author:** Danillo Oliveira  
**LinkedIn:** https://www.linkedin.com/in/danillobsoliveira/ 
