# 📊 CRM Analytics com Microsoft Fabric

Este projeto tem como objetivo simular uma solução completa de CRM Analytics utilizando arquitetura moderna de dados baseada no Microsoft Fabric. Inclui geração de dados sintéticos, ingestão em Lakehouse, transformação com PySpark, arquitetura Medallion, visualização com Power BI e práticas de segurança e performance.

---

## 🚀 Tecnologias Utilizadas

- [Microsoft Fabric](https://www.microsoft.com/en-us/microsoft-fabric)
- Lakehouse (Delta Lake)
- Power BI
- PySpark (via notebooks no Fabric)
- Python (com Faker)
- SQL (DAX, Spark SQL)

---

## 🏛️ Arquitetura Medallion

Este projeto segue o padrão Medallion para organização de dados:

### 🥉 Bronze – Raw Layer
> Dados brutos gerados com Faker, sem tratamento ou limpeza.

| Tabela               | Descrição                   |
|----------------------|-----------------------------|
| `bronze_clientes`    | Dados brutos de clientes     |
| `bronze_produtos`    | Produtos simulados           |
| `bronze_vendas`      | Histórico cru de vendas      |

---

### 🥈 Silver – Clean Layer
> Dados limpos, com joins e normalizações aplicadas.

| Tabela               | Descrição                          |
|----------------------|------------------------------------|
| `dim_cliente`        | Dimensão de clientes limpa         |
| `dim_produto`        | Dimensão de produtos               |
| `dim_tempo`          | Datas do período de análise        |
| `fato_vendas`        | Fato com chaves e medidas          |

---

### 🥇 Gold – Business Layer
> Dados prontos para análise e dashboards.

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

## ⚡ Boas Práticas de Performance

- Escrita em **formato Delta Lake** (otimizado para leitura incremental)
- Uso de **partitioning** nas tabelas Silver e Gold (por estado ou por data)
- Carga organizada em camadas para **reduzir retrabalho**
- Uso de **notebooks modulares e reutilizáveis** para manter organização

---

## 📊 Dashboards no Power BI

- Vendas por estado (mapa e gráfico de barras)
- Produtos mais vendidos
- Clientes mais ativos
- Evolução de vendas por data

> Os dashboards foram construídos diretamente no Power BI dentro do Fabric, com conexão nativa ao Lakehouse.

---

## 📁 Estrutura do Projeto

crm-analytics-fabric/
├── notebooks/
│ ├── geracao_dados.ipynb
│ ├── bronze_to_silver.ipynb
│ └── silver_to_gold.ipynb
├── modelagem/
│ └── modelo_dimensional.drawio
├── imagens/
│ └── dashboard.png
├── README.md


---

## 🧠 Aprendizados Demonstrados

- Modelagem dimensional (estrela)
- Lakehouse architecture
- Medallion (Bronze, Silver, Gold)
- ETL com PySpark
- Visualização com Power BI
- Boas práticas de dados: segurança, performance, governança

---

## 🧩 Próximos Passos

- [ ] Implementar dados reais via API (ou datasets públicos)
- [ ] Adicionar versionamento de dados (Delta Time Travel)
- [ ] Automatizar ETL com Pipelines no Fabric

---

**Autor:** Danillo Oliveira  
**LinkedIn:** https://www.linkedin.com/in/danillobsoliveira/ 
