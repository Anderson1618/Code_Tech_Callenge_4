import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import datetime
from prophet import Prophet

st.set_page_config(layout='wide')
st.title('Os segredos por trás do preço do petróleo 🛢')
st.header('Como funciona a cotação do petróleo?')

st.write('A cotação do petróleo é definida por seu preço, em um determinado momento no mercado onde está sendo negociado. Desse modo, a cotação do petróleo é o resultado da oferta e demanda da commodity no mercado internacional. Nesse caso, a unidade de medida utilizada é de dólares por barril de petróleo.Dessa forma, o preço do barril de petróleo nada mais é do que o valor combinado por aqueles que desejam vender, por aqueles que desejam comprar. Ou seja, é o preço de equilíbrio que satisfaz a oferta e demanda do mercado.Importante ressaltar que, de forma geral, ao negociar barris de petróleo, usa-se a cotação do preço no final do pregão de mercado, informando qual foi a cotação do dia aos investidores.')
st.write('Adicionalmente, aspectos geopolíticos podem exercer uma função de destaque na flutuação dos valores do petróleo. Conflitos em zonas-chave de produção, incidentes políticos e turbulências em nações exportadoras proeminentes podem instigar incertezas nos mercados e influenciar os custos. Mais ainda, considerações ecológicas, avanços tecnológicos em fontes de energia renovável e políticas governamentais ligadas à mudança para fontes energéticas mais ecologicamente viáveis também têm o potencial de afetar as perspectivas de longo prazo do mercado petrolífero, exercendo um impacto mais prolongado nos valores.')
st.divider()

url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'
table_id = 'grd_DXMainTable'
df = pd.read_html(url, attrs={'id': table_id}, encoding='utf-8', header=0)[0]
df.rename(columns={'Data': 'data', 'Preço - petróleo bruto - Brent (FOB)': 'preco'}, inplace=True)
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
df['preco'] = pd.to_numeric(df['preco'].astype(str).str.replace(',', '.'), errors='coerce') / 100

col1, col2 = st.columns(2)

with col1:
    st.subheader("Tabela histórica de Preço")
    st.dataframe(df)

with col2:

     st.subheader("Evolução dos países com maiores reservas de pretóleo do mundo (1990 a 2023)")
     st.video("https://www.youtube.com/watch?v=IK6PAP7Sj7s")

st.divider()

st.subheader("Série histórica - Preço petróleo")
df_mean_by_year = df.groupby(df['data'].dt.year).mean(numeric_only=False)
fig_mean_by_year = px.line(df_mean_by_year, x=df_mean_by_year.index, y=df_mean_by_year.columns[1:],
                                    labels={'value': 'Média do Preço do Petróleo (USD)', 
                                    'index': 'Ano'})

fig_mean_by_year.add_vline(x=2008, line_dash="dash", line_color="green", annotation_text="2008", annotation_position="top left")
fig_mean_by_year.add_vline(x=2022, line_dash="dash", line_color="green", annotation_text="2022", annotation_position="top left")

st.plotly_chart(fig_mean_by_year, use_container_width=True)

col1, col3 = st.columns(2)


col1,col3 = st.columns(2)
with col1:

    st.markdown(":red[2008]")
    st.write('Em 2008, o valor do petróleo atingiu seu ponto mais alto, registrando um aumento significativo que nunca havia sido alcançado anteriormente. Esse aumento notável pode ser atribuído ao contexto econômico global, onde eventos econômicos complexos e questões geopolíticas desempenharam papéis fundamentais.')
    st.write('Além disso, este ano marcou também a crise econômica global mais severa desde a Segunda Guerra Mundial. Devido à crise financeira e à recessão que diminuíram a demanda por petróleo, o preço do barril despencou para US$ 33,36 em 24 de dezembro.')
    st.write(' ')
    subcol1, subcol2 = st.columns(2)
    

with col3:
    st.markdown(":red[2022]")
    st.write('A disseminação do COVID-19 provocou quedas sucessivas no preço do petróleo. Na base de qualquer atividade produtiva, o setor de energia é sensível aos efeitos da pandemia na economia.')
    st.write('Os preços do petróleo e de seus derivados tiveram grande apreciação na primeira metade do ano de 2022, principalmente em função do conflito em andamento entre Rússia e Ucrânia, mas também devido ao crescimento da demanda global acima dos valores que eram projetados. No mercado doméstico, os preços de combustíveis tiveram altas significativas. O óleo diesel de baixo teor de enxofre (S-10) teve o maior aumento, de 42%, enquanto a gasolina teve alta de 8%, e o gás liquefeito de petróleo (GLP) subiu 10%, em valores médios.')
    st.caption(' \n')
    st.caption(' \n')
    st.write(' ')
    subcol1, subcol2 = st.columns(2)

st.divider()

st.subheader("Análise temporal do preço - 1987 até 2024")  
st.write('O gráfico interativo permite uma análise detalhada da variação diária ao longo dos anos. é interessante para entendermos como o preço do petróleo flutuou em um determinado período extratificando insights reçevantes para tomadas de decisão.')
st.write('Ao selecionar um ano de interesse, podem visualizar como o mercado reagiu a eventos geopolíticos, mudanças na oferta e demanda, ou outros fatores econômicos.')


selected_year = st.selectbox("Ano:", df['data'].dt.year.unique())
df_selected_year = df[df['data'].dt.year == selected_year]
fig = px.line(df_selected_year, x='data', y='preco', title=f"Preço do Petróleo em {selected_year}",
              labels={'Preco': 'Preço do Petróleo (USD)', 'data': 'data'})
fig.update_xaxes(title_text='Data')
fig.update_yaxes(title_text='Preço do Petróleo (USD)')
st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Principais eventos que afetaram o preço do petróleo")
st.header('Anos 90')

col1, col2 = st.columns([2, 1])
with col1:
    df_guerra_golfo = df[(df['data'] >= '1990-08-01') & (df['data'] <= '1990-08-31')]
    fig = px.line(df_guerra_golfo, x='data', y='preco', title='Variação do Preço do Petróleo durante a Guerra do Golfo',
              labels={'preco': 'Preço do Petróleo (USD)', 'data': 'Data'})
    fig.add_trace(go.Scatter(x=df_guerra_golfo['data'], y=df_guerra_golfo['preco'], showlegend=False))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write('Em 1990, o Iraque invade o Kuwait – que participou na Guerra Irã-Iraque, com isso o preço do barril, que no início da Guerra do Golfo, era cotado a US$ 22.25, teve um aumento de cerca de 25%.')
    st.write('')

col1, col2 = st.columns([2, 1])
with col1:
    df_crise_asia = df[(df['data'] >= '1997-01-01') & (df['data'] <= '1999-01-01')]
    fig = px.line( df_crise_asia, x='data', y='preco', title='Variação do Preço do Petróleo durante a crise financeira na ásia (1997-1998)',
              labels={'preco': 'Preço do Petróleo (USD)', 'data': 'Data'})
    fig.add_trace(go.Scatter(x=df_crise_asia['data'], y=df_crise_asia['preco'], showlegend=False))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write('Com a redução da demanda asiática, os preços globais do petróleo caíram. No auge da crise, os preços do petróleo Brent caíram de cerca de 20 dlares por barril em 1997 para menos de 10 dólares por barril no final de 1998')
    st.write('')

st.header('Anos 2000')
col1, col2 = st.columns([2, 1])
with col1: 
    df_setembro_2001 = df[(df['data'] >= '2001-09-01') & (df['data'] <= '2001-09-30')]
    fig_setembro_2001 = px.line(df_setembro_2001, x='data', y='preco', title='Variação do Preço do Petróleo em Setembro de 2001',
                            labels={'preco': 'Preço do Petróleo (USD)', 'data': 'Data'})
    fig_setembro_2001.add_trace(go.Scatter(x=df_setembro_2001['data'], y=df_setembro_2001['preco'], showlegend=False))
    st.plotly_chart(fig_setembro_2001, use_container_width=True)
with col2:
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write('Em 11 setembro de 2001 em pleno ataque terrorista aos Estados Unidos o barril Brent era cotado a 29.12 dólares, diminuindo a 25.57 dólares uma semana depois. No final do mês de setembro registra uma queda de cerca de 25%.')

col1, col2 = st.columns([2, 1])
with col1: 
    df_asia = df[(df['data'] >= '2008-01-01') & (df['data'] <= '2008-12-31')]
    fig_asia = px.line(df_asia, x='data', y='preco', title='Crescimento da Demanda da China e Índia',
                            labels={'preco': 'Preço do Petróleo (USD)', 'data': 'Data'})
    fig_asia.add_trace(go.Scatter(x=df_asia['data'], y=df_asia['preco'], showlegend=False))
    st.plotly_chart(fig_asia, use_container_width=True)

with col2:
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write('Em 2008, os preços do petróleo atingiram um pico histórico, chegando a cerca de 147 dólares por barril, refletindo a forte demanda global impulsionada principalmente pelo crescimento da China e da Índia.')
    
st.header('Anos 2010')
col1, col2 = st.columns([2, 1])
with col1: 
    df_eua = df[(df['data'] >= '2014-01-01') & (df['data'] <= '2016-12-31')]
    fig_eua = px.line(df_eua, x='data', y='preco', title='Queda dos Preços do Petróleo (2014-2016)',
                            labels={'preco': 'Preço do Petróleo (USD)', 'data': 'Data'})
    fig_eua.add_trace(go.Scatter(x=df_eua['data'], y=df_eua['preco'], showlegend=False))
    st.plotly_chart(fig_eua, use_container_width=True)

with col2:
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write('Excesso de oferta devido à produção de xisto nos EUA e desaceleração da economia global.')
    st.write('Resultado: Preços do petróleo caíram de cerca de 100 dólares para menos de 30 dólares por barril.')

st.header('Anos 2020')
col1, col2 = st.columns([2, 1])
with col1: 
    df_russia_ucrania = df[(df['data'] >= '2022-02-24') & (df['data'] <= '2022-03-03')]
    fig_russia_ucrania = px.line(df_russia_ucrania, x='data', y='preco', title='Variação do Preço do Petróleo no conflito Rússia-Ucrânia',
                            labels={'preco': 'Preço do Petróleo (USD)', 'data': 'Data'})
    fig_russia_ucrania.add_trace(go.Scatter(x=df_russia_ucrania['data'], y=df_russia_ucrania['preco'], showlegend=False))
    st.plotly_chart(fig_russia_ucrania, use_container_width=True)

with col2:
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write('No conflito entre Rússia e Ucrânia, houve crescimento do dia 24 de fevereiro a 3 de março de 2022 foi de 19.21%, com barris cotados em 118.11 dólares. Após cerca de 3 meses, os preços caíram.')


st.divider()

st.subheader("Maiores exportadores de petróleo do mundo")  

st.caption("Produção de petróleo diária.")
dados_paises = {
    "País": ["EUA", "Arábia Saudita", "Rússia", "Canadá", "Iraque", 
             "China", "Emirados Árabes Unidos", "Irã", "Brasil"],
    "Produção de Petróleo (barris por dia)": [16.6e6, 11e6, 10.9e6, 5.4e6, 4.1e6, 4e6, 3.7e6, 3.6e6, 3e6],
    "% do Total": [18.5, 12.2, 12.2, 6.0, 4.6, 4.4, 4.1, 4.0, 3.3]
}

df_producao_paises = pd.DataFrame(dados_paises)
selected_countries = st.multiselect("Selecione os países", df_producao_paises['País'].unique(), default=df_producao_paises['País'].unique())
df_selected_countries = df_producao_paises[df_producao_paises['País'].isin(selected_countries)]
color_scheme = ['#ec5353'] * len(selected_countries)
fig_countries = px.bar(df_selected_countries, x="País", y="Produção de Petróleo (barris por dia)",
                       color="% do Total", title="Maiores exportadores de petróleo do mundo",
                       labels={"Produção de Petróleo(barris por dia)": "Produção de Petróleo (barris por dia)", "% do Total": "Percentual do Total"})
st.plotly_chart(fig_countries, use_container_width=True)


st.divider()
st.subheader("Análise - Top 5 maiores exportadores")

st.write('De acordo com os dados dos países exportadores de petróleo de 2023, as exportações aumentaram 0,8% em relação ao ano anterior, atrás da superfície agitou-se um mar de dinâmicas em mudança. Embora tenha registado uma expansão de 2,3%, a procura ficou aquém das expectativas originais, destacando factores adversos como o aumento da eficiência energética e a crescente adopção de veículos eléctricos. ')

conteudo_eua = """
**1. Estados Unidos:**
Com uma estimativa aproximada de 11.567.000 barris por dia, os Estados Unidos é o principal produtor mundial de petróleo, como têm sido durante muitos anos.
"""

conteudo_arabia_saudita = """
**2. Arábia Saudita:**
A Arábia Saudita continua a ser o líder incontestado entre os gigantes exportadores de petróleo. Com enormes reservas de petróleo e tecnologias de extracção de ponta.
"""

conteudo_russia = """
**3. Rússia:**
A Rússia é o maior país do mundo em área terrestre e também é um importante produtor de petróleo.
"""

conteudo_canada = """
**4. Canadá:**
O país solidificou a sua posição como um importante exportador de petróleo. As areias betuminosas e as reservas convencionais do Canadá contribuem principalmente para o mercado global de petróleo.
"""

conteudo_iraque = """
**5. Iraque:**
Localizado no centro do Médio Oriente, é um exportador de petróleo resiliente. Apesar de problemas como a instabilidade política e a guerra regional, o Iraque continua a ser um dos 10 principais países exportadores de petróleo.
"""


st.markdown(conteudo_eua, unsafe_allow_html=True)
st.markdown(conteudo_arabia_saudita, unsafe_allow_html=True)
st.markdown(conteudo_russia, unsafe_allow_html=True)
st.markdown(conteudo_canada, unsafe_allow_html=True)
st.markdown(conteudo_iraque, unsafe_allow_html=True)

st.divider()

st.subheader('Previsão')

df.rename(columns={'data': 'ds', 'preco': 'y'}, inplace=True)

data_atual = df['ds'].max()
data_futuro = data_atual + datetime.timedelta(days=180)
futuro = pd.date_range(start=data_atual, end=data_futuro, freq='D')
futuro = pd.DataFrame({'ds': futuro})
df_prophet = pd.concat([df, futuro], ignore_index=True)

train_data = df_prophet[df_prophet['ds'] < '2022-01-01']
test_data = df_prophet[df_prophet['ds'] >= '2022-01-01']

model = Prophet()
model.fit(train_data)

future = model.make_future_dataframe(periods=180)
forecast = model.predict(future)

fig = px.line(forecast, x='ds', y=['yhat', 'yhat_lower', 'yhat_upper'], title='Previsão do Preço do Petróleo (Brent) para os Próximos 6 meses', 
              color_discrete_map={'yhat': 'green', 'yhat_lower': 'purple', 'yhat_upper': 'blue'})
fig.add_scatter(x=df_prophet['ds'], y=df_prophet['y'], mode='lines', name='Observado', line=dict(color='grey'))
fig.update_xaxes(title_text='Data')
fig.update_yaxes(title_text='Preço do Petróleo')

fig.for_each_trace(lambda t: t.update(name=t.name.replace('yhat', 'Previsão').replace('yhat_lower', 'Limite mínimo').replace('yhat_upper', 'Limite máximo')))
st.plotly_chart(fig, use_container_width=True)

comparison_data = pd.merge(test_data[['ds', 'y']], forecast[['ds', 'yhat']], on='ds', how='inner')
accuracy_percentage = (1 - (comparison_data['y'] - comparison_data['yhat']).abs().sum() / comparison_data['y'].sum()) * 100
st.write(f'Acurácia: {accuracy_percentage:.2f}%')

st.divider()

st.subheader('Próximos 6 meses')

modelo_prophet = Prophet(interval_width=0.75) 
modelo_prophet.fit(df_prophet)
previsao = modelo_prophet.predict(futuro)

fig = go.Figure()
fig.add_trace(go.Scatter(x=previsao['ds'], y=previsao['yhat'], mode='lines', name='Preço Previsto', line=dict(color='green')))

fig.add_trace(go.Scatter(x=previsao['ds'], y=previsao['yhat_lower'], fill='tonexty', mode='lines', line=dict(width=0), name='Intervalo de Confiança'))
fig.add_trace(go.Scatter(x=previsao['ds'], y=previsao['yhat_upper'], fill='tonexty', fillcolor='rgba(0,100,80,0.2)', mode='lines', line=dict(width=0), name=''))

fig.update_xaxes(title_text='Data')
fig.update_yaxes(title_text='Previsão do Preço do Petróleo')

st.plotly_chart(fig, use_container_width=True)
