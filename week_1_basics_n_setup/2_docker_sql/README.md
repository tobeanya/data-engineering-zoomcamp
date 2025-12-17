docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13

# check with docker process is runnning
docker ps -a


to remove folder by docker process:
# verify the container using the mount
docker ps -a --filter "name=quirky_tu" --format "table {{.ID}}\t{{.Names}}\t{{.Status}}"

# stop and remove the container that's holding the mount
docker stop quirky_tu
docker rm quirky_tu

# remove ACLs, set ownership to your user, then delete the folder
sudo setfacl -bR ny_taxi_postgres_data || true
sudo chown -R $(id -u):$(id -g) ny_taxi_postgres_data
rm -rf ny_taxi_postgres_data

if folder is empty, run command
sudo chmod a+rwx ny_taxi_postgres_data

// access postgres db
pgcli -h localhost -p 5432 -u root -d ny_taxi

mkdir -p data
wget -c -O data/yellow_tripdata_2025-01.parquet "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet"

taxi-zone look up
"https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"

yellow trip dictionary
https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf

# describe table in postgres
\d yellow_taxi_data

# run pgadmin
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  dpage/pgadmin4

  # remove all docker containers
  docker ps -aq | xargs -r docker rm -f

  # run docker postgres and pgadmin with network

  docker network create -d bridge pg-network

  docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13

  docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pg-admin \
  dpage/pgadmin4

  URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet" 

  python ingest_data.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_data \
    --url=${URL}

### build with docker instead
  docker build -t taxi_ingest:v001 .

  URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet" 

  docker run -it \
    --network=pg-network \
  taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_data \
    --url=${URL}