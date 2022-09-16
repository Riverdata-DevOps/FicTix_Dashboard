# Bibliotecas para a WEB API
from helper_functions import *
from database import *
import streamlit.components.v1 as components
import plotly.express as px

def Home():
    st.title('RiverSensor')

    df = pd.read_parquet('./Data/FicTix.parquet')
    df['date'] = df.Data.dt.date

    c1, c2, c3, c4 = st.columns(4)
    c1.metric('Sensor1', df[df.Sensor=='v10'].Contagem.sum())
    c2.metric('Sensor2', df[df.Sensor=='v11'].Contagem.sum())
    c3.metric('Sensor3', df[df.Sensor=='v13'].Contagem.sum())
    c4.metric('Contagem de Pessoas Total', df.Contagem.sum())
    bar = px.bar(pd.DataFrame(df.groupby(['Data', 'Sensor']).Contagem.sum().reset_index()), x='Data', y = 'Contagem', title='Evolução da Movimentação nos Totens', height = 550)
    bar.update_traces(
                      marker_line_width = 0,
                      selector=dict(type="bar"))

    bar.update_layout(bargap=0,
                      bargroupgap = 0,
                      )
    st.plotly_chart(bar, use_container_width=True)

    bar = px.bar(pd.DataFrame(df.groupby(['date', 'Sensor']).Contagem.sum().reset_index()), x='date', y = 'Contagem', title='Evolução Diária da Movimentação nos Totens por Sensor', height = 550, color='Sensor')
    st.plotly_chart(bar, use_container_width=True)

    bar = px.bar(pd.DataFrame(df.groupby(['hour', 'Sensor']).Contagem.mean().reset_index()), x='hour', y = 'Contagem', title='Movimentação Média por Horário por Sensor', height = 550, color='Sensor')
    bar.update_traces(
        marker_line_width = 0,
        selector=dict(type="bar"))

    bar.update_layout(bargap=0,
                      bargroupgap = 0,
                      )
    st.plotly_chart(bar, use_container_width=True)

    bar = px.bar(pd.DataFrame(df.groupby('Sensor').Contagem.sum().reset_index()), x='Sensor', y = 'Contagem', title='Movimentação por Sensor', height = 550, color='Sensor')
    st.plotly_chart(bar, use_container_width=True)

    bar = px.bar(pd.DataFrame(df.groupby('weekday').Contagem.mean().reset_index()), x='weekday', y = 'Contagem', title='Movimentação Média por dia da Semana', height = 550)
    st.plotly_chart(bar, use_container_width=True)

def vazio():
    st.empty()
