from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from autogluon.tabular import TabularPredictor

DATA_PATH = "/tmp/demo.csv"

def generate_data():
    df = pd.DataFrame({
        "x1": [1, 2, 3, 4, 5],
        "x2": [5, 4, 3, 2, 1],
        "y":  [0, 1, 0, 1, 0]
    })
    df.to_csv(DATA_PATH, index=False)
    print(f"Generated data saved to {DATA_PATH}")

def train_automl():
    data = pd.read_csv(DATA_PATH)
    predictor = TabularPredictor(label="y").fit(
        data,
        time_limit=30,
        presets="best_quality"
    )
    leaderboard_res = predictor.leaderboard()
    print(leaderboard_res)

with DAG(
    dag_id="automl_autogluon_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
):
    generate = PythonOperator(
        task_id="generate_data",
        python_callable=generate_data
    )

    train = PythonOperator(
        task_id="train_automl_model",
        python_callable=train_automl
    )

    generate >> train
