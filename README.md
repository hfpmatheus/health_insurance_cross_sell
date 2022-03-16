# Health Insurance Cross-Sell.

<img src="https://garagem360.com.br/wp-content/uploads/2021/06/Linha-RS-scaled.jpg" alt="drawing" width="70%"/>

## Description: 

This project aims to order a potential client list by propensity score.

## 2.0. Business Problem:

## 3.0. Solution Strategy:

### 3.1. Descrição dos Dados: 
Checagem do dataset por inteiro, como sua dimensão, NA's, tipos de variáveis... Por final, uma descrição estatística.
### 3.2. Feature Engineering: 
Etapa pré análise exploratória. Criação das hipóteses com finalidade de criar as features necessárias para a análise.
### 3.3. Análise Exploratória:
Exploração dos dados com foco no entendimento das métricas do negócio, geração de insights e correlação de variáveis.
### 3.4. Preparação dos Dados: 
Normalização, rescaling e transformação dos dados para os modelos de Machine Learning.
### 3.5. Seleção de Variáveis: 
Utilização do algoritmo Boruta, em conjunto com o conhecimento obtido na análise exploratória, para selecionar as variáveis/features mais importantes para os modelos.
### 3.6. Modelos de Machine Learning:
Aplicação dos modelos de Machine Learning com Cross-Validation para definir o que apresenta melhor resultado.
### 3.7. Tradução dos erros: 
Conversão dos erros do modelo escolhido para resultados financeiros de negócio.
### 3.8. Deploy:
Deploy do script na nuvem Heroku para tornar o modelo acessível em outras máquinas e construção do bot no telegram.

## 4.0. Top 3 Data Insights:

Dentro de 11 hipóteses validadas e desvalidadas, essas são as que mais geraram surpresa:

- H1: Lojas com maior sortimento deveriam vender mais.

**FALSA**. Lojas com maior sortimento vendem menos.

- H2: Lojas com competidores mais próximos deveriam vender menos.

**FALSA**. Lojas com competidores mais próximos vendem mais.

- H3: Lojas com competidores à mais tempo deveriam vender mais.

**FALSA**. Lojas com competidores recentes tem um pico de vendas, e com o tempo as vendas abaixam e se tornam mais constantes.

## 5.0. Machine Learning Model Applied:

Com a solução elaborada no projeto, a rede Rossmann tem como esperada a receita de aproximadamente $ 285,059,456.00 nas próximas seis semanas, com seus respectivos pior/melhor cenários devido a erros do algoritmo calculados abaixo.

<img src="img/business_results.png" alt="drawing" width="40%"/>

A previsão individual de cada loja pode ser consultada pelo Telegram, conforme a [demonstração](https://youtube.com/shorts/iXpcF_Y6k0g?feature=share). Com isso, resolvemos nossa questão de negócio, visto que o CFO pode, a qualquer momento, consultar a receita que está por vir para cacular o budget da reforma para cada uma das lojas.

## 6.0. Machine Learning Model Performance:

## 7.0. Business Results:

## 8.0. Conclusion:

## 9.0. Next Steps to improve:

## 10.0. References:

- O dataset utilizado se encontra no [Kaggle](https://www.kaggle.com/c/rossmann-store-sales/data)
