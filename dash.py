pip install streamlit
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime
from prophet import Prophet
import streamlit as st

# Configuração inicial do Streamlit
st.set_page_config(layout='wide')
st.title('O Preço do Petróleo 🛢️📈')
st.header('Análise da influência geopolítica e demanda global')

st.write('O preço é influenciado por uma série de fatores complexos e inter-relacionados. Em primeiro lugar, a :red[oferta] e :red[demanda] desempenham um papel crucial. Eventos que afetam a produção, como decisões da [Organização dos Países Exportadores de Petróleo (OPEP)](https://pt.wikipedia.org/wiki/Organiza%C3%A7%C3%A3o_dos_Pa%C3%ADses_Exportadores_de_Petr%C3%B3leo) ou interrupções nas operações de grandes produtores, podem impactar significativamente a oferta global. Por outro lado, a demanda por petróleo está intimamente ligada às condições econômicas globais, com flutuações na atividade industrial e no consumo de energia tendo um impacto direto.')
st.write('Além disso, fatores geopolíticos podem desempenhar um papel significativo na volatilidade dos preços do petróleo. Tensões em regiões-chave de produção, eventos políticos e instabilidades em grandes países exportadores podem gerar incerteza nos mercados e influenciar os preços. Além disso, considerações ambientais, avanços tecnológicos em energias renováveis e políticas governamentais relacionadas à transição para fontes de energia mais limpas também podem afetar as perspectivas de longo prazo do mercado de petróleo, impactando os preços de forma mais sustentada.')

st.divider()

# Carregamento e manipulação dos dados
url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'
table_id = 'grd_DXMainTable'
df = pd.read_html(url, attrs={'id': table_id}, encoding='utf-8', header=0)[0]
df.rename(columns={'Data': 'data', 'Preço - petróleo bruto - Brent (FOB)': 'preco'}, inplace=True)
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
df['preco'] = pd.to_numeric(df['preco'].astype(str).str.replace(',', '.'), errors='coerce') / 100

col1, col2 = st.columns(2)

with col1:
    st.subheader("Dados de referência")
    st.dataframe(df)

with col2:
    max_price_row = df.loc[df['preco'].idxmax()]
    st.subheader("Valor Máximo do Preço e Ano Correspondente:")
    st.write(f"Data: {max_price_row['data'].strftime('%d/%m/%Y')}, Preço Máximo: {max_price_row['preco']}")

    st.divider()

    min_price_row = df.loc[df['preco'].idxmin()]
    st.subheader("Valor Mínimo do Preço e Ano Correspondente:")
    st.write(f"Data: {min_price_row['data'].strftime('%d/%m/%Y')}, Preço Mínimo: {min_price_row['preco']}")

st.divider()

st.subheader("Média Anual do Preço do Petróleo")  
df_mean_by_year = df.groupby(df['data'].dt.year).mean(numeric_only=False)
fig_mean_by_year = px.line(df_mean_by_year, x=df_mean_by_year.index, y=df_mean_by_year.columns[1:],
                                    labels={'value': 'Média do Preço do Petróleo (USD)', 
                                    'index': 'Ano'})
st.plotly_chart(fig_mean_by_year, use_container_width=True)
st.caption('A linha representa a média anual do preço do barril de petróleo ao longo do tempo. Variações notáveis podem ser resultado de eventos geopolíticos, flutuações na oferta e demanda, ou fatores econômicos globais.')

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(":red[2008]")
    st.write('No ano de 2008, o preço do petróleo atingiu seu maior patamar, marcando uma significativa alta que nunca havia sido alcançada até então.')
    st.write('Este aumento expressivo pode ser contextualizado no cenário global da economia, onde eventos econômicos complexos e dinâmicas geopolíticas desempenharam papéis cruciais.')
    st.write('Além disso, este ano também marcou a crise econômica mundial mais séria desde a Segunda Guerra Mundial')
    st.write('Por causa da crise financeira e da recessão que freou a demanda por petróleo, o barril desabou até os US$ 33,36 em 24 de dezembro.')
    st.write(' ')
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        df_2008 = df[df['data'].dt.year == 2008]
        max_price_2008 = df_2008.loc[df_2008['preco'].idxmax()]
        st.write("Valor Máximo em 2008")
        st.caption(f"Data: {max_price_2008['data'].strftime('%d/%m/%Y')}") 
        st.caption(f"Preço Máximo: {max_price_2008['preco']}")
    with subcol2:
        min_price_2008 = df_2008.loc[df_2008['preco'].idxmin()]
        st.write("Valor Mínimo em 2008:")
        st.caption(f"Data: {min_price_2008['data'].strftime('%d/%m/%Y')}")
        st.caption(f"Preço Mínimo: {min_price_2008['preco']}")
    
with col2:
    st.markdown(":red[2016]")
    st.write('A demanda por petróleo caiu por causa do ritmo mais lento de crescimento das economias dos países grandes consumidores, como Estados Unidos, China, Japão e os países ricos da Europa.')
    st.write('Os Estados Unidos, o segundo maior importador global, conseguiram reduzir sua dependência do Oriente Médio e aumentar seus estoques de petróleo por meio de uma abordagem diversificada. ')
    st.write('Aumentando sua produção de petróleo de 10 para 14 milhões de barris por dia, tornaram-se o maior produtor mundial, ultrapassando a Rússia e a Arábia Saudita.')
    st.caption(' \n')
    st.write(' ')
    st.write(' ')
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        df_2016 = df[df['data'].dt.year == 2016]
        max_price_2016 = df_2016.loc[df_2016['preco'].idxmax()]
        st.write("Valor Máximo em 2016")
        st.caption(f"Data: {max_price_2016['data'].strftime('%d/%m/%Y')}") 
        st.caption(f"Preço Máximo: {max_price_2016['preco']}")
    with subcol2:
        min_price_2016 = df_2016.loc[df_2016['preco'].idxmin()]
        st.write("Valor Mínimo em 2016")
        st.caption(f"Data: {min_price_2016['data'].strftime('%d/%m/%Y')}")
        st.caption(f"Preço Mínimo: {min_price_2016['preco']}")

with col3:
    st.markdown(":red[2022]")
    st.write('A disseminação do COVID-19 provocou quedas sucessivas no preço do petróleo. Na base de qualquer atividade produtiva, o setor de energia é sensível aos efeitos da pandemia na economia.')
    st.write('Apesar dos ganhos, preços ficaram longe dos mais de US$ 120 por barril registrados durante o pico da crise da guerra da Ucrânia')
    st.write('As reservas globais de petróleo subiram ao seu maior nível histórico em 2022, a 1.564,44 bilhões de barris, informou a Organização dos Países Exportadores de Petróleo (Opep), em seu Boletim Estatístico Anual de 2023.')
    st.caption(' \n')
    st.caption(' \n')
    st.write(' ')
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        df_2022 = df[df['data'].dt.year == 2022]
        max_price_2022 = df_2022.loc[df_2022['preco'].idxmax()]
        st.write("Valor Máximo em 2022")
        st.caption(f"Data: {max_price_2022['data'].strftime('%d/%m/%Y')}") 
        st.caption(f"Preço Máximo: {max_price_2022['preco']}")
    with subcol2:
        min_price_2022 = df_2022.loc[df_2022['preco'].idxmin()]
        st.write("Valor Mínimo em 2022")
        st.caption(f"Data: {min_price_2022['data'].strftime('%d/%m/%Y')}")
        st.caption(f"Preço Mínimo: {min_price_2022['preco']}")

st.divider()

# Configurar o modelo Prophet
model = Prophet()

# Treinamento do modelo
df_prophet = df.rename(columns={'data': 'ds', 'preco': 'y'})
model.fit(df_prophet)

# Fazendo a previsão para os próximos 365 dias
future_dates = model.make_future_dataframe(periods=365)
forecast = model.predict(future_dates)

# Gráfico de previsão
fig_forecast = go.Figure()
fig_forecast.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], name='Previsão'))
fig_forecast.add_trace(go.Scatter(x=df['data'], y=df['preco'], name='Dados Históricos'))
fig_forecast.update_layout(title='Previsão de Preços do Petróleo para os Próximos 365 Dias',
                           xaxis_title='Data', yaxis_title='Preço do Petróleo (USD)')
st.plotly_chart(fig_forecast, use_container_width=True)
