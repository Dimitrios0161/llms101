from pandasai.llm.local_llm import LocalLLM
import streamlit as st
from pandasai.connectors import GoogleBigQueryConnector
from pandasai import SmartDataframe

bigquery_connector = GoogleBigQueryConnector(
    config={
        "credentials_path" : "./llms-426021-2c79e3cbf537.json",
        "database" : "llms",
        "table" : "international_results_pr",
        "projectID" : "llms-426021",
    }
)
model = LocalLLM(
    api_base="http://localhost:11434/v1",
    model="mannix/defog-llama3-sqlcoder-8b:latest"
)

st.title("Random-Football-Stats SQL")

df_connector = SmartDataframe(bigquery_connector,config={'llm':model})

prompt=st.text_input('Enter prompt:')

if st.button('Generate'):
    if prompt:
        with st.spinner('Generating response..'):
            st.write(df_connector.chat(prompt))



