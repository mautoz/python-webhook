from flask import Flask, request, redirect, session, flash, url_for, send_from_directory
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

# conn = db_aux.connect_db(db_credentials)

app = Flask(__name__)

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
        total = db_aux.total_rows(conn, "reviews_data")
    return render_template('classificar.html', titulo = "Classificar Review", review=review, total=total)

@app.route('/atualizar')
def atualizar():
    with db_aux.connect_db(db_credentials) as conn:
        review = db_aux.random_review(conn, "reviews_data")
        total = db_aux.total_rows(conn, "reviews_data")
    return render_template('classificar.html', titulo = "Classificar Review", review=review, total=total)

if __name__ == "__main__":
    app.run(debug=True)