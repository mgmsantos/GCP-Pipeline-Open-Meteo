# Google Cloud Platform - Pipeline ETL Open-Meteo

## Sobre o Projeto
Este projeto consiste na construção de um pipeline de dados (ETL) *serverless* e automatizado na Google Cloud Platform (GCP). O objetivo é extrair diariamente dados climáticos (temperatura máxima, mínima e precipitação) da região de São Carlos/SP (ou qualquer município) em escala diária, criando um histórico consolidado que serve de base para análises, modelagens em contextos de *Business Intelligence*.


## Arquitetura na Nuvem
A arquitetura foi desenhada com foco em eficiência, baixo custo (cota gratuita) e segurança:

1. **Orquestração (Cloud Scheduler):** Gatilho configurado via *Cron* para rodar diariamente às 06h00.
2. **Processamento (Cloud Run):** Script em Python que consome a API da Open-Meteo, transforma o JSON num DataFrame Pandas, limpa e padroniza as colunas.
3. **Armazenamento (BigQuery):** Data Warehouse que recebe o *Append* diário dos dados limpos de forma automática.
4. **Visualização (Power BI):** Conexão nativa via SQL ao BigQuery para criação de dashboards interativos.

![Pipeline ETL Google Cloud](<img width="1280" height="961" alt="pipeline" src="https://github.com/user-attachments/assets/4a18fbdf-6135-44c9-92fb-0e52ce28ad2b" />)

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3+ (`pandas`, `requests`, `google-cloud-bigquery`)
* **Google Cloud:** Cloud Run, Cloud Scheduler, BigQuery, IAM (Billing Alerts)

## Conecte-se Comigo

*Siga os links abaixo para saber mais sobre minha trajetória profissional e me contatar:*

<div> 
  <a href="mailto:miguel.gms31@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
  <a href="https://www.linkedin.com/in/miguelgms31/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
  <a href="http://lattes.cnpq.br/2943203054995050" target="_blank"><img src="https://img.shields.io/badge/-Lattes-%230077B5?style=for-the-badge&logo=google-scholar&logoColor=white" target="_blank"></a>
</div>

---
