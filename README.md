Billboard Top Songs Data Engineering Project 🎶 📊
========
This project features the designing and building of a complete end-to-end data engineering pipeline for the Billboard Top Songs dataset using modern tools and best practices.


About the Dataset
================
This project uses the simple [Billboard Top Songs](https://www.kaggle.com/datasets/samayashar/billboard-top-songs/data) dataset, which includes fields like songs, total streams, daily streams, genre, release year, TikTok virality, sentiment analysis of lyrics, and musical features like danceability and energy. However, this raw data alone is not readily usable for insights or decision-making.


Problem Description 
================
In today's music industry, understanding how songs perform across different genres, time periods, and platforms is essential for artists, producers, and marketers alike. Platforms like TikTok and Spotify have revolutionized how music is discovered, streamed, and shared, leading to rapid changes in what makes a song go viral.

To optimize our Dataset for analysis, there's a need for a modern data pipeline to:

- Ingest and store the data efficiently
- Clean, transform, and model the data for analytics
- Create a centralized and queryable data warehouse
- Power a dashboard for stakeholders to explore trends, anomalies, and other metrics


Building the Pipeline
================
1. Data Ingestion: Store raw data in a scalable data lake. Here we'll use Google cloud storage (GCS).

2. ETL/ELT Pipelines:
    - Move data from the lake to a structured data warehouse, BigQuery.
    - Use dbt (dbt cli) to define simple models for transforming raw data into meaningful, analytics-ready models.

3. Data Quality & Monitoring: Use Soda to implement tests and alerts for data accuracy and freshness.

4. Orchestration: Use Airflow (via Astronomer) to automate and schedule pipeline tasks.

5. Analytics & Visualization: Build an interactive dashboard using Metabase:
    - Top-performing songs over time
    - Genre trends across years
    - Year-over-year stream growth


Summary of Technologies used
================

1. [Docker](https://www.docker.com):
    Docker is a containerization platform that allows you to package applications and their dependencies into portable containers. In this project, Docker is used to containerize all components of the pipeline (dbt, Airflow, Metabase,     etc.), ensuring consistent environments across local development and deployment. It simplifies setup and makes the pipeline reproducible and scalable.

2. [Astro](https://www.astronomer.io/docs):
    Astro (by Astronomer) is a cloud-native data orchestration platform built around Apache Airflow. It simplifies Airflow deployment, monitoring, and scaling. In this project, Astro is used to deploy and manage Airflow pipelines with     a production-grade interface, providing version control, observability, and seamless integration with tools like Cosmos and dbt.

3. [Airflow](https://airflow.apache.org):
    Apache Airflow is an open-source workflow orchestration tool used to programmatically create, schedule, and monitor data workflows. In this project, Airflow is used to automate the ETL process — from ingesting raw data to GCS,         uploading to BigQuery, transforming with dbt, to quality testing — enabling full reliable pipeline automation.

4. [Terraform](https://www.terraform.io):
    Terraform is an Infrastructure as Code (IaC) tool that allows you to define and provision cloud infrastructure using declarative configuration files. In this project, Terraform is used to provision Google Cloud resources like GCS      buckets and BigQuery datasets, ensuring consistent and version-controlled infrastructure setup.

5. [Google Cloud Storage (GCS)](https://console.cloud.google.com):
    GCS is an object storage service for unstructured data. It serves as the data lake in this project, where raw Billboard datasets are initially stored. GCS provides scalable, cost-effective storage that can be accessed by Airflow       and dbt for downstream processing.

6. [BigQuery](https://console.cloud.google.com):
    BigQuery is a fully managed, serverless data warehouse by Google Cloud. In this project, it acts as the central data warehouse, where cleaned and transformed data (via dbt) is loaded. It enables fast, SQL-based analysis and            supports seamless integration with BI tools like Metabase for reporting.

7. [Soda](https://www.soda.io):
    Soda is a data quality and observability tool that helps detect data issues such as missing values, anomalies, or schema changes. In this project, Soda is integrated into the Airflow pipeline to validate data at each stage             ensuring the integrity of raw ingested data and transformed tables before they are surfaced to dashboards.

8. [DBT](https://www.getdbt.com/):
    dbt (data build tool) is used for transforming raw data in the warehouse using SQL and modular, version-controlled data models. In this project, dbt is used to transform data and make them data analysis-ready in BigQuery. The CLI      version is used and it allows tight integration with Airflow and Cosmos for automation.

9. [Cosmos](https://www.astronomer.io/cosmos):
    Cosmos is an open-source Airflow provider by Astronomer that allows you to run dbt projects natively as Airflow tasks. In this project, Cosmos dynamically converts dbt models into Airflow tasks with their dependencies preserved,       enabling fine-grained orchestration, monitoring, and retries — all while keeping the dbt DAG structure intact.

10. [Metabase](https://www.metabase.com):
    Metabase is an open-source business intelligence tool for data visualization and dashboards. In this project, Metabase connects to BigQuery to create interactive dashboards that display trends in streams, genre popularity, etc.        making the data accessible to non-technical stakeholders.


Data Pipeline
================
<img width="802" alt="Screenshot 2025-04-09 at 17 53 37" src="https://github.com/user-attachments/assets/630f5edf-75c2-4d25-adea-827dcad2f5ec" />


Steps to Reproduce Project
================

Prequisites:
- Google Cloud Account
- Terraform cli
- Astro cli

1. **Prepare Code & Environment**
   
   - Clone the project repo and navigate to the directory
   - Open in vscode for better coding management & experience
     
     ```
     git clone https://github.com/tasemgt/top-songs-de-pipeline.git
     cd top-songs-de-pipeline
     ```
2. **Google Cloud GCP**
   - Create an account in GCP
   - Create Project on gcp
   - Create service account, add ‘Storage Admin’ & ‘BigQuery Admin’ roles
   - Create access key and download. Rename file to `de-creds.json`
   - Create a folder inside the `include` folder called `gcp`in the project root folder and place the `de-creds.json` there

3. **Terraform**
   - Open `variables.tf` and replace project id with yours (Gotten from your gcp account project)
   - Replace bucket name with a name you like (This will be your cloud storage bucket)
   - Navigate to the `cd terraform` directory, in terminal terminal shell and run
   - `terraform init` To set up and install gcp provider code in terraform directory.
   - `terraform plan`: To see Bucket and Dataset (Data lake & Warehouse) to be built on gcp
   - `terraform apply`: To invoke build process

4. **Astro**
   Astronomer is a managed platform and tooling layer built around Airflow. It serves as a wrapper, deployment tool, and enterprise solution for running Airflow at scale. It is used in this project to spin up ‘docker’ containers and      manage airflow processes. To read more about [Astro](https://www.astronomer.io/docs/]) To install [Astro CLI](https://www.astronomer.io/docs/astro/cli/overview) for your OS.
   After installation:
    - Navigate to project root directory
    - Run the command `astro dev start` To lunch the airflow docker containers and start airflow.

5. **Airflow**
    - Visit `http://localhost:8080` to open Airflow web interface on the browser with credentials (admin:admin)
    - Go to Admin menu and then connections to create a new connection
    - New connection in Airflow looks like the image below
    <br>
    <img width="807" alt="Screenshot 2025-04-08 at 20 44 59" src="https://github.com/user-attachments/assets/40d3eae9-6bf3-4e99-8e27-61a67d5cecdf" />
    <br>
    <br>
    
    - Go to DAGs in the menu bar and run Music Dag pipeline.
       <br>
       <br>
    <img width="997" alt="Screenshot 2025-04-09 at 12 34 40" src="https://github.com/user-attachments/assets/6850f874-37d5-4363-ae12-b0ccdbea054e" />

6. **Metabase**
    - Visit `http://localhost:3000` to open Metabase web interface and create a new account if not present.
    - Fill in your personal details
    - Add projectID, service account `de-creds.json` file and then connect!
    - Select new and add a question to select a transformed dataset for visualization
    - Select either ‘Genre Trends’, ‘Total Artists’, and ‘Yearly Streams Trend’
    - Play around with data and make your own custom visualization.
    - Your Dashboard should look like mine below!
  
    <img width="1512" alt="Music streams Dashboard" src="https://github.com/user-attachments/assets/62983f17-ba78-45ab-8e9b-088d3dcf5590" />


Contact
=======
Connect with me on LinkedIn ❤️ : [Michael Tase](https://www.linkedin.com/in/michael-tase-4151216a)
