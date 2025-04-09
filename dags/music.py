from datetime import datetime

# Airflow imports
from airflow.decorators import dag, task
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from airflow.models.baseoperator import chain

# Astro imports
from astro import sql as aql
from astro.files import File
from astro.sql.table import Table, Metadata
from astro.constants import FileType

# Soda imports
from include.soda.check_function import check

# Cosmos & DBT imports
from include.dbt.cosmos_config import DBT_PROJECT_CONFIG, DBT_CONFIG
from cosmos.airflow.task_group import DbtTaskGroup
from cosmos.constants import LoadMode
from cosmos.config import ProjectConfig, RenderConfig


@dag(
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=['music'],
)
def music():

    upload_csv_to_gcs = LocalFilesystemToGCSOperator(
        task_id='upload_csv_to_gcs',
        src='include/datasets/music_dataset.csv',
        dst='raw/music_dataset.csv',
        bucket='tase_music_data',
        gcp_conn_id='gcp',
        mime_type='text/csv',
    )

    # create_music_dataset = BigQueryCreateEmptyDatasetOperator(
    #     task_id='create_music_dataset',
    #     dataset_id='music_test',
    #     gcp_conn_id='gcp',
    # )

    gcs_to_bq = aql.load_file(
        task_id='gcs_to_bq',
        input_file=File(
            'gs://tase_music_data/raw/music_dataset.csv',
            conn_id='gcp',
            filetype=FileType.CSV,
        ),
        output_table=Table(
            name='raw_music_streams',
            conn_id='gcp',
            metadata=Metadata(schema='music')
        ),
        use_native_support=False,
    )

    # SODA check to verify dataset in BQ
    @task
    def check_load(scan_name='check_load', checks_subpath='sources'):
        return check(scan_name, checks_subpath, 'music')
    
    # check_load()

    # Remember to run dbt in its virtual environment like we created..
    transform = DbtTaskGroup(
        group_id='transform',
        project_config=DBT_PROJECT_CONFIG,
        profile_config=DBT_CONFIG,
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS,
            select=['path:models/transform']
        )
    )

     # SODA check to verify transformed tables
    @task
    def check_transform(scan_name='check_transform', checks_subpath='transform'):
        from include.soda.check_function import check
        return check(scan_name, checks_subpath, 'music')
    
    # check_transform()
    
    chain(
        upload_csv_to_gcs,
        gcs_to_bq,
        check_load(),
        transform,
        check_transform()
    )

music()