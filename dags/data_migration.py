from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

dag_params = {
    'dag_id': 'migration_dag',
    'start_date': datetime(2022, 5, 23),
    'schedule_interval': '@once',
}


def _migration_data():
    # Define the source hook using the PostgresHook class
    src_hook = PostgresHook(postgres_conn_id='source_db')
    src_conn = src_hook.get_conn()

    #Use cursor to execute SQL query
    cursor = src_conn.cursor()
    cursor.execute("SELECT * FROM orders")

    # Define the destination hook using the PostgresHook class
    dst_hook = PostgresHook(postgres_conn_id="target_db")
    # Use insert statement to insert data into the target table
    dst_hook.insert_rows(table='orders', rows=cursor)


with DAG(**dag_params, catchup=False) as dag:

    start = DummyOperator(task_id='start', dag=dag)

    migration = PythonOperator(
        task_id='migration_task',
        python_callable=_migration_data,
        dag=dag
    )

    start >> migration


