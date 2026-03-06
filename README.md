# 🚀 IA Generativa Pipeline ETL

Projeto desenvolvido durante o bootcamp com foco em **Python, Engenharia de Dados e IA Generativa**.

O objetivo deste projeto é construir um **pipeline ETL (Extract, Transform, Load)** consumindo dados de uma API pública e utilizando **OpenAI** para gerar conteúdos automatizados a partir dos dados extraídos.

Este projeto demonstra conceitos fundamentais de engenharia de dados como:

* Consumo de APIs REST
* Tratamento de dados em Python
* Estruturação de pipelines ETL
* Integração com modelos de IA generativa
* Organização de projetos de dados

---

# 📊 Arquitetura do Pipeline

O pipeline segue o fluxo clássico de engenharia de dados:

```
API (DummyJSON)
      ↓
Extract
      ↓
Transform
      ↓
OpenAI (geração de news)
      ↓
Load (arquivo CSV)
```

### Etapas

**Extract**

Responsável por consumir a API pública e extrair os dados dos produtos.

Fonte de dados:

https://dummyjson.com/products

---

**Transform**

Nesta etapa os dados são preparados para processamento:

* seleção de campos relevantes
* estruturação dos dados
* preparação do prompt para geração de conteúdo

---

**IA Generativa**

Utiliza a API da OpenAI para gerar **descrições curtas de produtos ("news")** automaticamente.

---

**Load**

Os dados processados são exportados para um arquivo estruturado.

Exemplo de saída:

```
data/processed/products_news.csv
```

---

# 🛠️ Tecnologias Utilizadas

* Python
* Requests
* OpenAI API
* Pandas
* Git
* GitHub

---

# 📁 Estrutura do Projeto

```
ia-generativa-pipeline-etl
│
├── extract.py
├── transform.py
├── load.py
├── main.py
│
├── data
│   ├── raw
│   └── processed
│
└── README.md
```

---


## ⚠️ Observação sobre uso da OpenAI API

Este projeto utiliza a **OpenAI API** para gerar descrições automatizadas dos produtos.

Para facilitar a execução do projeto durante o bootcamp, o pipeline foi desenvolvido de forma que **possa rodar mesmo sem uma chave da OpenAI**.

Caso o usuário não possua uma chave da API ou não queira utilizar crédito da plataforma, o pipeline continuará funcionando utilizando apenas as etapas de:

* Extract
* Transform
* Load

Nesse caso, a etapa de geração de conteúdo com IA é **simulada ou ignorada**, permitindo que o fluxo ETL seja executado normalmente.

Caso queira utilizar a OpenAI, basta configurar a variável de ambiente:

```
export OPENAI_API_KEY="sua-chave-aqui"
```

Mais informações:

https://platform.openai.com/


# ⚙️ Como executar o projeto

Clone o repositório:

```
git clone https://github.com/seu-usuario/ia-generativa-pipeline-etl.git
```

Entre na pasta do projeto:

```
cd ia-generativa-pipeline-etl
```

Crie e ative um ambiente virtual:

```
python -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```
pip install -r requirements.txt
```

Configure sua chave da OpenAI:

```
export OPENAI_API_KEY="sua-chave"
```

Execute o pipeline:

```
python main.py
```

---

# 📌 Exemplo de saída

```
Extract OK: 20 produtos
Exemplo: Essence Mascara Lash Princess
```

Arquivo gerado:

```
data/processed/products_news.csv
```

---

# 🎯 Objetivo do Projeto

Este projeto foi desenvolvido como parte do bootcamp para demonstrar habilidades em:

* Engenharia de Dados
* Automação de pipelines
* Integração com APIs
* Uso de IA generativa para enriquecimento de dados

---

# 👨‍💻 Autor

Cícero Ramalho
Estudante de Engenharia da Computação

LinkedIn:
https://linkedin.com/

GitHub:
https://github.com/

---
