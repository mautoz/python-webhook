![EACH-USP](./imagens/each.png)

# ACH2018 - PSGII

Este repositório faz parte do projeto de ACH2018 e funciona em conjunto com o [review-classifier](https://github.com/mautoz/reviews-classifier) e o [review-automation-scripts](https://github.com/mautoz/reviews-automation-scripts).
A função do script é funcionar como uma interface web para facilitar a avaliação humana dos reviews cadastrados no bd. Função indispensável, visto que para o treino da máquina é necessário de dados avaliados por pessoas.

# Pré requisitos

O código foi feito no Ubuntu 18.04.5 LTS e precisa ter instalado:

- Python >=3.6
- Flask 1.1.2
- psycopg2 2.8.6
- Unicode 1.1.1 (Se for usar o pip, existe unicode e Unicode, escolha o último)
- Postgres >=10.14

Não esqueça de antes de executar esta parte, inserir no bd os reviews que estão no repositório [review-classifier](https://github.com/mautoz/reviews-classifier).

# Instruções

1. Os reviews exibidos aqui foram retirados do mesmo bd do repositório [review-classifier](https://github.com/mautoz/reviews-classifier), sendo assim, verifique com cuidado suas configurações no seu PostgreSQL e altere com seus dados o [run](run.sh)!

2. Rode o [Run](run.sh):
```
bash run.sh
```
Por padrão, a porta é 5000, então acesse: [localhost:5000](http://localhost:5000/) ou [127.0.0.1:5000](http://127.0.0.1:5000/).

3. Está pronto para fazer as classificações!

4. (Opcional) Como são muitos reviews, pode ser necessário pedir ajuda! É possivel criar uma URL para seu ambiente local. Caso queira fazer isso, acesse: https://ngrok.com/, cadastre-se e baixe o arquivo! É rápido!

5. (Opcional) Na pasta do ngrok, rode:
```
 ./ngrok http porta
``` 
Se você não alterou nada no Flask, substitua porta por 5000.

6. (Opcional) É só passar a url do "Forwarding" para as pessoas que queiram classificar!

# Exemplo de funcionamento

![index](./imagens/example_index.png)

![classificar](./imagens/example_classificar.png)

# Troubleshooting

- Verifique se em sua máquina o correto para rodar Python é "python' ou 'python3';
- Verifique se em sua máquina o correto para rodar pip é "pip' ou 'pip3';
- É possível que não rode com Python 3.6 e sua máquina tem ambos (3.6 e 3.7) instalados. Verifique a versão certa e altere se necessário com:
```
sudo update-alternatives --config python3;
```
- Utilize o 'Unicode' e não 'unicode'.

# Creditos para das imagens

As imagens utilizadas nas interfaces foram retiradas dos seguintes links:

- [review.png](https://halonotoriedade.com.br/wp-content/uploads/2018/06/review.png)
- [Review.png](https://reviewr.me/como-fazer-uma-gestao-de-reviews-eficiente/)
- [check.png](https://www.pngkey.com/maxpic/u2e6w7t4o0e6y3a9/)
- [stars.png](https://heyyoulanguages.com/wp-content/uploads/2020/08/Componente_5_%E2%80%93_1.png)
- [favicon.ico](https://favicon.io/emoji-favicons/star/)