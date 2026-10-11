import functions_framework
import requests
import pandas as pd
from google.cloud import bigquery

@functions_framework.http
def extrair_clima(request):
    # 1. Vai buscar os dados de Temperatura e Chuva de São Carlos do dia anterior
    url = "https://api.open-meteo.com/v1/forecast?latitude=-22.0174&longitude=-47.8860&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&past_days=1&forecast_days=0&timezone=America%2FSao_Paulo"
    
    response = requests.get(url).json()
    daily_data = response.get('daily', {})
    
    # 2. Organiza os dados numa tabela
    df = pd.DataFrame(daily_data)
    df.rename(columns={
        'time': 'data', 
        'temperature_2m_max': 'temp_max', 
        'temperature_2m_min': 'temp_min', 
        'precipitation_sum': 'chuva'
    }, inplace=True)
    df['data'] = pd.to_datetime(df['data']).dt.date
    
    # 3. Liga-se ao BigQuery e cria tudo automaticamente no Google Cloud
    client = bigquery.Client()
    project_id = client.project
    
    # Cria a base de dados se não existir
    dataset_id = f"{project_id}.dataset_clima"
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "us-central1"
    client.create_dataset(dataset, exists_ok=True)
    
    # Guarda os dados
    table_id = f"{dataset_id}.historico_diario"
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND",
        autodetect=True # Cria as colunas sozinho
    )
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()
    
    return "Dados guardados com sucesso!", 200
