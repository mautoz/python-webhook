from flask import Flask, request, redirect, session, flash, url_for, send_from_directory
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        "index.html"
    )

@app.route('/imagens/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('imagens', nome_arquivo)

if __name__ == "__main__":
    app.run(debug=True)