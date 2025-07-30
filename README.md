# 📊 CRM Analytics com Microsoft Fabric

Este projeto simula uma solução moderna de CRM Analytics utilizando a plataforma Microsoft Fabric. A solução envolve a geração de dados sintéticos e também a integração com dados reais via API pública, armazenados em Lakehouse com arquitetura Medallion, processamento e transformação com PySpark, controle de versionamento via Delta Lake, automação de pipelines e visualização interativa com Power BI.

---

## 🚀 Tecnologias Utilizadas

- [Microsoft Fabric](https://www.microsoft.com/en-us/microsoft-fabric)
- Lakehouse (Delta Lake)
- Power BI
- PySpark (via notebooks no Fabric)
- Pipelines do Fabric
- Python (com Faker e requests)
- SQL (DAX, Spark SQL)

---

## 🏛️ Arquitetura Medallion

Este projeto segue o padrão Medallion para organização de dados:

### 🥉 Bronze – Raw Layer
> Armazenamento de dados brutos, simulados e reais, sem transformações.

| Tabela               | Fonte                      | Descrição                             |
|----------------------|----------------------------|----------------------------------------|
| `bronze_clientes`    | Faker                      | Clientes fictícios                     |
| `bronze_produtos`    | Faker                      | Produtos com categorias e preços       |
| `bronze_vendas`      | Faker                      | Histórico de compras simuladas         |
| `bronze_estados_ibge`| API IBGE                   | Lista de estados brasileiros           |

---

### 🥈 Silver – Clean Layer
> Dados tratados, com schemas padronizados, tipos ajustados e joins aplicados.

| Tabela               | Descrição                          |
|----------------------|------------------------------------|
| `dim_cliente`        | Dimensão de clientes               |
| `dim_produto`        | Dimensão de produtos               |
| `dim_tempo`          | Dimensão temporal (2 anos)         |
| `dim_regional`       | Dimensão geográfica padronizada    |
| `fato_vendas`        | Fato com chaves e métricas         |

---

### 🥇 Gold – Business Layer
> Dados prontos para análise de negócio, agregações e indicadores.

| Tabela                   | Descrição                           |
|--------------------------|-------------------------------------|
| `resumo_vendas_estado`   | Total de vendas por estado          |
| `clientes_ativos`        | Ranking de clientes por volume      |
| `top_produtos`           | Produtos mais vendidos              |

---

## 🔐 Segurança

- **Acesso controlado por workspace** no Microsoft Fabric
- **Máscara de dados sensíveis**, como e-mails dos clientes
- **Separação de camadas**: acesso total só em Bronze/Silver; leitura apenas na Gold
- Pronto para uso com **monitoramento e auditoria** via Fabric ou Azure Purview

---

## 🕒 Controle de Versão de Dados (Delta Time Travel)

Este projeto utiliza Delta Lake como formato de armazenamento, permitindo versionamento automático de todas as tabelas. Isso possibilita:

- Recuperar o estado anterior de uma tabela
- Auditar transformações e histórico de carga
- Refazer análises com base em versões antigas

Exemplo de uso no notebook:

```sql
-- Consultar versão anterior da fato_vendas usando SQL
SELECT * FROM silver.fato_vendas VERSION AS OF 3
```
```PySpark:
-- Consultar versão anterior da fato_vendas usando PySpark
df_v2 = spark.read.format("delta") \
    .option("versionAsOf", 3) \
    .load("Tables/silver/fato_vendas")
```

## ⚙️ Automação com Pipelines

Todos os processos de ETL são automatizados por Pipelines do Microsoft Fabric.

🔁 Pipelines Criados

| Pipeline                   | Etapas                           |
|--------------------------|-------------------------------------|
| `etl_bronze_to_silver`   | Limpeza, casting, joins, escrita na camada Silver          |
| `etl_silver_to_gold`     | Agregações e geração de indicadores finais      |
| `api_coleta_ibge`           | Coleta e atualização de dados reais da API IBGE              |

Cada pipeline pode ser agendado para execução automática (ex: diariamente) ou manual.

---

## 📊 Dashboards no Power BI

- 🗺️ Mapa de vendas por estado (mapa e gráfico de barras)
- 📦 Produtos mais vendidos
- 👥 Clientes mais ativos
- 📉 Evolução de vendas (linha temporal)

> Os dashboards foram construídos diretamente no Power BI dentro do Fabric, com conexão nativa ao Lakehouse.

📷 Imagens estão disponíveis na pasta /imagens/dashboard.png.

---

## ⚡ Boas Práticas de Performance

- Armazenamento em Delta Lake (compactação + versionamento)
- Partitioning nas tabelas Silver e Gold (estado, data)
- Reuso de notebooks como módulos reutilizáveis
- Separação clara de responsabilidades entre camadas
- ETL incremental com controle de timestamp futuro (opcional)

---

## 📁 Estrutura do Projeto

```plaintext
crm-analytics-fabric/
├── notebooks/
│   ├── geracao_dados.ipynb
│   ├── coleta_api_ibge.ipynb
│   ├── bronze_to_silver.ipynb
│   └── silver_to_gold.ipynb
├── pipelines/
│   ├── etl_bronze_to_silver.json
│   ├── etl_silver_to_gold.json
│   └── api_coleta_ibge.json
├── modelagem/
│   └── modelo_dimensional.drawio
├── imagens/
│   └── dashboard.png
├── README.md
```
---

## 🧠 Competências Demonstrados

✔️ Modelagem dimensional (estrela)
✔️ Lakehouse Architecture
✔️ Arquitetura Medallion (Bronze → Silver → Gold)
✔️ ETL em PySpark
✔️ Delta Time Travel (versionamento de dados)
✔️ Automação com Pipelines do Fabric
✔️ Visualização com Power BI
✔️ Segurança e boas práticas de performance

---

**Autor:** Danillo Oliveira  
**LinkedIn:** https://www.linkedin.com/in/danillobsoliveira/ 
