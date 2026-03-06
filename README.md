# Pipeline ETL com Python e API

Projeto desenvolvido para praticar conceitos de **ETL (Extract, Transform, Load)** utilizando Python, pandas e consumo de API REST.

## Fonte de dados

API pública:  
https://dummyjson.com/products

## Etapas do Pipeline

### Extract
Consumo da API para obter produtos.

### Transform
Conversão dos dados em DataFrame e seleção das colunas relevantes:

- id
- title
- category
- price
- discountPercentage
- rating

### Load
Os dados transformados são exportados para:
data/processed/products_transformed.csv


## Integração com IA

Foi implementada uma função para geração de descrições de produtos utilizando a API da OpenAI.

Durante os testes, a execução retornou erro **429 (quota exceeded)** devido à ausência de crédito na API.

A estrutura da integração foi mantida no código para demonstrar o fluxo completo do pipeline.