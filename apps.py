# Bibliotecas para a WEB API
from helper_functions import *
from database import *
import streamlit.components.v1 as components
import plotly.express as px

def Home():
    st.title('RiverSensor')

    df = pd.read_parquet('./Data/FicTix.parquet')
    df['date'] = df.Data.dt.date

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric('Dia com Maior Movimentação Média', 'Sexta-feira')
    c2.metric('Dia com Maior Pico de Movimentação', 'Segunda-feira')
    c3.metric('Movimentação Média por Dia', int(pd.DataFrame(df.groupby('day').Contagem.sum()).reset_index().Contagem[0] /100))
    c4.metric('Movimentação Média por Semana', int((pd.DataFrame(df.groupby('day').Contagem.sum()).reset_index().Contagem[0]* 6)/100))
    c5.metric('Taxa de Conversão', '12.06%')


    contagem_ts = pd.DataFrame(df.groupby(['Data', 'Sensor']).Contagem.sum().reset_index())
    contagem_ts['Movimentação no Totem'] = 0.45*contagem_ts.Contagem
    contagem_ts['Movimentação no Corredor'] = contagem_ts.Contagem
    bar = px.bar(contagem_ts, x='Data', y = ['Movimentação no Totem', 'Movimentação no Corredor'], title='Evolução da Movimentação por Zona de Impacto', height = 550)
    bar.update_traces(
                      marker_line_width = 0,
                      selector=dict(type="bar"))

    bar.update_layout(bargap=0,
                      bargroupgap = 0,
                      )
    st.plotly_chart(bar, use_container_width=True)

    conversao = {
        'Zona de Impacto' : ['Movimentação no Corredor', 'Movimentação no Totem'],
        'Contagem de Pessoas': [6708, 556]
    }
    bar = px.bar(conversao, x = 'Zona de Impacto', y = 'Contagem de Pessoas', title='Movimentação Total por Zona de Impacto', height = 550)
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
