# TMDB Movie Dashboard

Este projeto tem como objetivo criar um **Dashboard de Análise de Dados de Filmes**, usando dados coletados da API **The Movie Database (TMDB)**. A coleta de dados será feita por meio de um pipeline ETL utilizando **Apache Airflow**, e a análise será realizada em um banco de dados PostgreSQL.

### Funcionalidades

- **Coleta de Dados**: A API TMDB é usada para coletar informações de filmes, como título, classificação, e gênero.
- **Transformação de Dados**: Usando Airflow, os dados serão processados e transformados para gerar insights, como médias de classificações de filmes por gênero ou ano.
- **Visualização**: Gráficos interativos serão gerados utilizando **Plotly** ou **Dash**, para exibir análises de dados como rankings de filmes e tendências.

