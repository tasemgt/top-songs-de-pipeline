Billboard Top Songs Data Engineering Project 🎶 📊
========
This is the project submission for the [DE Zoomcamp 2025](https://github.com/DataTalksClub/data-engineering-zoomcamp). It features the designing and building of a complete end-to-end data engineering pipeline for the Billboard Top Songs dataset using modern tools and best practices.


About the Dataset
================
This project leverages a comprehensive [Billboard Top Songs](https://www.kaggle.com/datasets/samayashar/billboard-top-songs/data) dataset, which includes metrics like total streams, daily streams, genre, release year, TikTok virality, sentiment analysis of lyrics, and musical features like danceability and energy. However, this raw data alone is not readily usable for insights or decision-making.


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












Deploy Your Project Locally
===========================

1. Start Airflow on your local machine by running 'astro dev start'.

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

2. Verify that all 4 Docker containers were created by running 'docker ps'.

Note: Running 'astro dev start' will start your project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432. If you already have either of those ports allocated, you can either [stop your existing Docker containers or change the port](https://www.astronomer.io/docs/astro/cli/troubleshoot-locally#ports-are-not-available-for-my-local-airflow-webserver).

3. Access the Airflow UI for your local Airflow project. To do so, go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.

You should also be able to access your Postgres Database at 'localhost:5432/postgres'.

Deploy Your Project to Astronomer
=================================

If you have an Astronomer account, pushing code to a Deployment on Astronomer is simple. For deploying instructions, refer to Astronomer documentation: https://www.astronomer.io/docs/astro/deploy-code/

Contact
=======

The Astronomer CLI is maintained with love by the Astronomer team. To report a bug or suggest a change, reach out to our support.
