import pandas as pd
import pyarrow.parquet as pq
import os
import argparse
from time import time 

from sqlalchemy import create_engine

CHUNK_SIZE = 100000

def upload_data(df, table_name, engine, chunk_size=CHUNK_SIZE):
    start_time = time()
    num_rows = df.shape[0]
    for i in range(0, num_rows, chunk_size):
        end_i = min(i + chunk_size, num_rows)
        df_chunk = df.iloc[i:end_i]
        batch_start = time()
        df_chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
        batch_time = time() - batch_start
        print(f"Inserted rows {i} to {end_i} into {table_name}. Time taken: {batch_time:.2f} seconds.")
    total_time = time() - start_time
    print(f"Finished uploading {num_rows} rows to {table_name} in {total_time:.2f} seconds.")

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet"
    url = params.url if params.url else url

    boolean_csv = True

    if url.endswith('.csv.gz'):
        filename = 'output.csv.gz'
    elif url.endswith('parquet'):
        filename = 'output.parquet'
        boolean_csv = False
    else:
        filename = 'output.csv'

    # todo: remove url later
    os.system(f'wget -c -O {filename} {url}') # different from video

    data_file = f'{filename}'
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()
    if boolean_csv:
        df = pd.read_csv(data_file)
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    else:
        table = pq.read_table(data_file, use_pandas_metadata=True)
        df = table.to_pandas(timestamp_as_object=False)
        
    df.head(n=0).to_sql(name=f'{table_name}', con=engine, if_exists='replace', index=False)
    upload_data(df, table_name=f'{table_name}', engine=engine, chunk_size=CHUNK_SIZE)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ingest Parquet data into PostgreSQL")
    parser.add_argument('--user', type=str, help='PostgreSQL username', required=True)
    parser.add_argument('--password', type=str, help='PostgreSQL password', required=True)
    parser.add_argument('--host', type=str, help='PostgreSQL host', default='localhost')
    parser.add_argument('--port', type=str, help='PostgreSQL port', default='5432')
    parser.add_argument('--db', type=str, help='PostgreSQL database name', required=True)
    parser.add_argument('--table_name', type=str, help='Target table name in the database', required=True)
    parser.add_argument('--url', type=str, help='URL of the data file', default=None)
    args = parser.parse_args()
    main(args)

