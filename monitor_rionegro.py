import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Monitoramento do Rio Negro",)

st.markdown('''
# **Monitoramento do Rio Negro**
As medições diárias da Cota do Rio Negro no Porto de Manaus compõem a série
histórica mais longa de toda a Amazônia, com registros dos períodos de Enchentes
e Vazantes na cidade desde 1902. Atualmente, a Cheia de 2021 já ultrapassou
as insuperáveis Cheias de 1953, 2009 e 2012. Pela primeira vez, Manaus viu e sentiu
o Rio Negro atingir a marca de 30 metros.

<div style="padding: 15px; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px; color: #a94442; background-color: #f2dede; border-color: #ebccd1;">
Das 10 maiores Cheias em Manaus desde o início das medições, 6 ocorreram desde 2009.
Com a intensificação do Ciclo Hidrológico na Amazônia
(<a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/grl.50377">Gloor <i>et al</i>., 2013 </a>),
junto com aumento da variabilidade do El Niño-Oscilação Sul
(<a href="https://www.nature.com/articles/s41586-018-0776-9">Cai <i>et al</i>., 2018 </a>)
e o atual rumo das Mudanças Climáticas Globais
(<a href="https://www.ipcc.ch/report/ar5/wg1/">IPCC AR5, 2013</a>),
a população do Amazonas vai precisar conviver com cada vez mais eventos extremos no Estado.
</div>

É por isso que este app foi criado: para informar e auxiliar a população do Amazonas
com uma maneira **rápida**, **fácil** e **interativa**
de visualizar diariamente o nível do Rio Negro. Todos os dados mostrados nos
gráficos abaixo foram medidos
pelo [Porto de Manaus](https://www.portodemanaus.com.br/?pagina=nivel-do-rio-negro-hoje)
e estão disponíveis no site.

''', unsafe_allow_html=True)


#Ler tabela de dados da Cota do Rio Negro - pasta pessoal no Google Drive
#Fonte: Porto de Manaus
#https://www.portodemanaus.com.br/?pagina=nivel-do-rio-negro-hoje

url = f'https://docs.google.com/spreadsheets/d/1uUdvyxlTdcJTgIeH_W6M-mXvJ8tcdv08onoR_7TEFzI/gviz/tq?tqx=out:csv&sheet=Cota'
rionegro = pd.read_csv(url)
# converter coluna de datas para um datetime do pandas
rionegro['Data'] = pd.to_datetime(rionegro['Data'], format='%d/%m/%y')

# gráfico 1
st.title(':ocean: Cota Diária do Rio Negro')
st.markdown(':arrow_right: Medição de hoje: **{:.2f} metros**'.format(rionegro['Cota (m)'].iloc[-1]))

fig1 = px.bar(rionegro, x='Data', y="Cota (m)", range_y=(21, 31), height=600,
             labels={"Data": "",
                     "Cota (m)": "Cota do Rio (m)"},
             template='none')

fig1.update_xaxes(tickformat="%d/%B", dtick='M1', tickmode='array',
                 tickvals=['2021-01-01', '2021-02-01', '2021-03-01',
                           '2021-04-01', '2021-05-01', '2021-06-01'],
                 ticktext=['Janeiro', 'Fevereiro', 'Março', 'Abril',
                           'Maio', 'Junho'])
st.plotly_chart(fig1)

# gráfico 2
st.title(':bar_chart: Variação da Cota do Rio')
st.markdown(':arrow_right: Variação de hoje: **{:.2f} centímetros**'.format(rionegro['Variação (cm)'].iloc[-1]))

fig2 = px.area(rionegro, x='Data', y="Variação (cm)", height=600,
             labels={"Data": "",
                     "Variação (cm)": "Variação (cm)"},
             template='none')

fig2.update_xaxes(tickformat="%d/%B", dtick='M1', tickmode='array',
                 tickvals=['2021-01-01', '2021-02-01', '2021-03-01',
                           '2021-04-01', '2021-05-01', '2021-06-01'],
                 ticktext=['Janeiro', 'Fevereiro', 'Março', 'Abril',
                           'Maio', 'Junho'])
st.plotly_chart(fig2)


st.markdown('''
#### Um oferecimento de:
**Meteorol. Me. [Willy Hagi](https://taggo.one/willyhagi)** / [**Meteonorte**.](http://meteonorte.com/)

Fonte de dados: Porto de Manaus.

<div style="padding: 15px; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px; color: #31708f; background-color: #d9edf7; border-color: #bce8f1;">
Sugestões? Entre em contato!
</div>
''', unsafe_allow_html=True)
