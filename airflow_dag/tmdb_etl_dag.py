from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd
from sqlalchemy import create_engine

# Configurações da API do TMDB
TMDB_API_KEY = 'TMDB_API_KEY'
BASE_URL = 'https://api.themoviedb.org/3'

# Configurações do Banco de Dados
DATABASE_URI = 'DATABASE_URI'

def extrair_dados_tmdb(categoria):
    """Extrai dados da API do TMDB."""
    try:
        url = f'{BASE_URL}/movie/{categoria}?api_key={TMDB_API_KEY}&language=pt-BR'
        response = requests.get(url)
        response.raise_for_status()  # Lança exceção para status de erro
        dados = response.json()['results']
        return dados
    except requests.exceptions.RequestException as e:
        print(f"Erro ao extrair dados: {e}")
        return None

def transformar_dados(dados):
    """Transforma os dados extraídos."""
    if dados:
        df = pd.DataFrame(dados)
        # Adicione suas transformações aqui
        return df
    return None

def carregar_dados_banco(df, tabela):
    """Carrega os dados transformados no banco de dados."""
    if df is not None:
        try:
            engine = create_engine(DATABASE_URI)
            df.to_sql(tabela, engine, if_exists='replace', index=False)
            print(f"Dados carregados com sucesso na tabela {tabela}.")
        except Exception as e:
            print(f"Erro ao carregar dados no banco: {e}")

with DAG(
    dag_id='tmdb_etl_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,  # Executar manualmente
    catchup=False,
) as dag:
    extrair_popular = PythonOperator(
        task_id='extrair_popular',
        python_callable=extrair_dados_tmdb,
        op_kwargs={'categoria': 'popular'},
    )

    transformar_popular = PythonOperator(
        task_id='transformar_popular',
        python_callable=transformar_dados,
        op_args=[extrair_popular.output],
    )

    carregar_popular = PythonOperator(
        task_id='carregar_popular',
        python_callable=carregar_dados_banco,
        op_args=[transformar_popular.output, 'filmes_populares'],
    )

    extrair_top_rated = PythonOperator(
        task_id='extrair_top_rated',
        python_callable=extrair_dados_tmdb,
        op_kwargs={'categoria': 'top_rated'},
    )

    transformar_top_rated = PythonOperator(
        task_id='transformar_top_rated',
        python_callable=transformar_dados,
        op_args=[extrair_top_rated.output],
    )

    carregar_top_rated = PythonOperator(
        task_id='carregar_top_rated',
        python_callable=carregar_dados_banco,
        op_args=[transformar_top_rated.output, 'filmes_melhor_avaliados'],
    )

    extrair_popular >> transformar_popular >> carregar_popular
    extrair_top_rated >> transformar_top_rated >> carregar_top_rated