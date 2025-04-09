FROM quay.io/astronomer/astro-runtime:12.7.1

# install dbt into a virtual environment
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install setuptools && \
    pip install --no-cache-dir dbt-bigquery==1.5.3 && deactivate