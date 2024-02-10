import pandas 
import os
from sqlalchemy import create_engine
from time import time

current = os.path.dirname(os.path.realpath(__file__))


path_excel = ['ny_taxi_postgres_data/taxi+_zone_lookup.csv' , 
              'ny_taxi_postgres_data/yellow_tripdata_2021-01.csv' ]

for file in path_excel:
    # file = path_excel[1]
    df = pandas.read_csv(os.path.join(current , file))
    print(df)


    # verificar os types e nome das colunas get_schema
    print(pandas.io.sql.get_schema(df , name = 'Criar_tabela_teste'))


    #criar conexão entre pyhton e Postgres
    engine = create_engine('postgresql://root:root@localhost:5433/ny_taxi')
    engine.connect() 

    # Utilizar o pandas para iterador(for) com chunksize
    df_iter = pandas.read_csv(os.path.join(current, file) , iterator= True , chunksize= 10000)
    
    while True: 
        try:
            t_star = time()

            if file == 'ny_taxi_postgres_data/yellow_tripdata_2021-01.csv':             
                name = 'ny_yellow_taxi_data'
                df.tpep_dropoff_datetime = pandas.to_datetime(df.tpep_dropoff_datetime)
                df.tpep_pickup_datetime = pandas.to_datetime(df.tpep_pickup_datetime)
            if file == 'ny_taxi_postgres_data/taxi+_zone_lookup.csv':             
                name = 'zones'

            df = next(df_iter)
            
            df.to_sql(name= name , con=engine , if_exists='append')

            t_end = time()
            print('insert another chunk..., took %.3f second' %(t_end - t_star  ))
        except Exception as e:
            print(str(e))
            break
            


