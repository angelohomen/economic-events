# Ideias para o estudos de eventos econômicos
No artigo, mostra-se uma forma de clusterizar ativos similares para um portfólio tendo-se os retornos diários usando técnicas deton e denoise de matrizes de correlação.

Para eventos podemos ter:
- Data/hora que saiu,
- Volatilidade que antes/depois da saída,
- Relevância

## Passo 1 - estudo de correlação:
Tratar os eventos como um portfólio de impactos no mini dólar. 
Baseado na porcentagem de variação na variância máxima do ativo 5 minutos antes e 5 minutos depois que o evento teve o dado publicado, elencar a correlação entre eventos com o objetivo de demonstrar analiticamente eventos que causam impacto similar no preço do mini dólar.

Gabarito: 
Os eventos abaixo saem exatamente no mesmo horário e dia, portanto, devem estar demasiadamente correlacionados.
- Ganho Médio por Hora Trabalhada (Mensal)
- Relatório de Emprego (Payroll) não-agrícola
- Relatório de Emprego - Payroll - Privado	
- Taxa de Desemprego
- Pedidos Iniciais de Subsídio de Desemprego

Resultado: A matriz denoised obteve o melhor resultado de correlação. Elencou 9 grupos. Pode-se afirmar que os eventos que pertencem ao mesmo grupo tendem a gerar impactos semelhantes na variância do dólar.

Conclusão: Correlação não é causalidade, pode ser sim que outro fator macro tenha impactado exatamente no mesmo range de minutos a variância do dólar. Apesar disso, é possível perceber que os agrupamentos possuem relacionamento entre si, em especial o usado como gabarito (grupo 2) e encontrou relação entre "Variação de Empregos Privados ADP", "Pedidos Iniciais de Subsídio de Desemprego" e "Taxa de Desemprego" mesmo quando tem seus dados publicados em dias diferentes.

## Passo 2 - o que fazer:
- Modelo de previsão de lado/valor do release:
    -> Feature selection:
        Aplicar modelos de feature selection para seleção dos eventos que seriam utilizados para prever o lado(Classificação)/valor(Regressão) da próxima publicação do evento label
    -> Estudar utilização dos modelos baseado no tipo de abordagem escolhida (classificação ou regressão):
        Separar dados em in-out sample e testar as parametrizações escolhidas. Sempre lembrar que em média temos 190 pontos para cada evento, ou seja, são poucos dados, portanto, muitos modelos serão descartados.
    -> Deploy:
        Gerar pkl e alimentar a primeiro momento manualmente, dado que é um modelo estático, e rodar como API usando flask.

- Modelo de previsão de impacto no mini dolar:
    Aqui o intuito é prever a variância (dependente do lado ou não) do dólar para o próximo release, envolvendo Black Swan. Features como últimos releases de outros eventos, últimos retornos do ativo e momentum. 
    Vejo como output desse modelo ranges de valores e variâncias que o dólar pode chegar, como se fosse um modelo de cenários que, com Monte Carlo, pode trazer uma noção de "como se comportará" o mercado no próximo release.
    Seguir os passos do modelo anterior para construção.

## Observações:
-> Para demais ativos, se deve pensar em bases de dados históricos.
-> Apresentar o MetaTrader5.
-> Apresentar fluxo simples de modelagem no Python.
-> Apresentar fluxo simples de modelagem no MetaTrader5.
-> Sugestão de modelo pra começar.