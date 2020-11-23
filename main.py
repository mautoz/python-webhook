from datetime import datetime
from flask import Flask, request, redirect, flash, url_for, send_from_directory
from flask.templating import render_template
import os

import db_aux


db_credentials = {
    'host' : os.getenv('POSTGRES_HOST'),
    'dbname' : os.getenv('POSTGRES_DATABASE'),
    'user' : os.getenv('POSTGRES_USER'),
    'password' : os.getenv('POSTGRES_PASSWORD'),
    'port' : os.getenv('POSTGRES_PORT') 
}


app = Flask(__name__)
app.secret_key = 'ach2018'


@app.route('/')
def index():
    return render_template(
        "index.html"
    )


@app.route('/imagens/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('imagens', nome_arquivo)


@app.route('/classificar')
def classificar():
    with db_aux.connect_db(db_credentials) as conn:
        review = db_aux.random_review(conn, "reviews_data")
        print(f'Review_id: {review[0]}')
    return render_template('classificar.html', titulo = "Classificar Review", review=review)


@app.route('/atualizar', methods=['POST',])
def atualizar():
    reviews_data_id = request.form['id']
    is_a11y = request.form['a11y']
    palavras = request.form['palavras']
    print(reviews_data_id)
    print(is_a11y)
    words = palavras.split(',')
    words = [palavra.strip() for palavra in words]
    print(words)
    with db_aux.connect_db(db_credentials) as conn:
        db_aux.insert_review_words(conn, reviews_data_id, words)
        db_aux.update_is_a11y(conn, reviews_data_id, is_a11y)
    flash(f'Classificado em {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}! Obrigado! Um novo review está disponível abaixo! Por favor, classifique o máximo que puder!')
    return redirect(url_for('classificar'))


@app.route('/reportar')
def reportar():
    return render_template('reportar.html', titulo = "Reportar erro")


@app.route('/enviar', methods=['POST',])
def enviar():
    mensagem = {}
    mensagem["nome"] = request.form['nome']
    mensagem["email"] = request.form['email']
    mensagem["conteudo"] = request.form['conteudo']
    with db_aux.connect_db(db_credentials) as conn:
        db_aux.insert_contato(conn, mensagem)
    return render_template('obrigado.html', titulo = "Obrigado pelo retorno!")


if __name__ == "__main__":
    app.run(debug=True)
