from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("index.html", \
        titulo_pagina="Página inicial")
    
@app.route("/sobre")
def sobre():
    return render_template("sobre.html", \
        titulo_pagina="Sobre mim")
    
@app.route("/teste")
def teste():
    return "está atualizando de verdade"
    
@app.route("/menu")
def menu():
    return render_template("menu.html", \
        titulo_pagina="Menu")

@app.route("/carrinho")
def carrinho():
    return render_template("carrinho.html", \
        titulo_pagina="Carrinho")
    
    
if __name__ == "__main__":
    app.run(debug=True)