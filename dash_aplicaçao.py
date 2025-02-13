from dash import Dash, dcc, Input, Output, html
import plotly.express as px
import pandas as pd

# Carregar o dataset
df = pd.read_csv('ecommerce_estatistica.csv')

lista_Temporada = df['Temporada'].unique()
options = [{'label': nivel, 'value': nivel} for nivel in lista_Temporada]

# Função para criar os gráficos
def criar_graficos(selecao_Temporada):
    filtro_df = df[df['Temporada'].isin(selecao_Temporada)]
    
    # Gráfico de barras
    fig1 = px.bar(
        filtro_df, x='Temporada', y='Desconto', color='Temporada',
        barmode='group', color_discrete_sequence=px.colors.qualitative.Set1
    )
    fig1.update_layout(
        title='Temporada por Frequência de Descontos',
        xaxis_title='Temporada',
        yaxis_title='Frequência de Descontos',
        legend_title='Temporada'
    )
    
    # Gráfico 3D
    fig2 = px.scatter_3d(
        filtro_df, x='Temporada', y='Desconto', z='Gênero', color='Temporada'
    )
    fig2.update_layout(
        title='Temporada vs Frequência de Descontos e Gênero',
        scene=dict(
            xaxis_title='Temporada',
            yaxis_title='Frequência de Descontos',
            zaxis_title='Gênero'
        )
    )   
    
    return fig1, fig2

# Criar a aplicação Dash
def cria_app():
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1('Dashboard Interativo'),
        html.Div("Interatividade entre dados"),
        html.Br(),
        html.H2('Temporada por Frequência de Descontos'),
        dcc.Checklist(
            id='id_selecao_Temporada',
            options=options,
            value=[lista_Temporada[0]]
        ),
        dcc.Graph(id='id_grafico_barra'),
        dcc.Graph(id='id_grafico_3d')
    ])

    # Definir callbacks
    @app.callback(
        [
            Output('id_grafico_barra', 'figure'),
            Output('id_grafico_3d', 'figure')
        ],
        [Input('id_selecao_Temporada', 'value')]
    )
    def atualiza_grafico(selecao_Temporada):
        return criar_graficos(selecao_Temporada)

    return app

# Executar o aplicativo
if __name__ == '__main__':
    app = cria_app()
    app.run_server(debug=True, port=8050)
