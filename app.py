from flask import Flask, render_template

app = Flask(__name__)

PIZZA_VAZIA = {"nome": "Não encontrado", "preco": 0.0, "img": ""}

CARDAPIO = {
    "chocolate": {
        "nome": "Chocolate com Morango",
        "preco": 42.0,
        "img": "https://selecoes.ig.com.br/sabor-de-casa/pizza-de-chocolate-veja-como-fazer-esta-delicia/"
    },
    "queijo": {
        "nome": "Quatro Queijos Premium",
        "preco": 55.9,
        "img": "https://www.ogastronomo.com.br/buffet-em-domicilio/a-arte-e-a-historia-da-pizza-quatro-queijos-um-guia-completo"
    },
    "carne": {
        "nome": "Carne de Sol na Nata",
        "preco": 58.0,
        "img": "https://app.bigdatawifi.com.br/parmegianno-shopping/ofertas/produto/detalhe/34876"
    }
}

@app.route('/')
def home():
    return "<h1>Pizzaria Dev</h1>"

@app.route('/pizzaria/<sabor>')
def pizza(sabor):
    dados = CARDAPIO.get(sabor.lower(), PIZZA_VAZIA)
    return render_template('pizza.html', pizza=dados)

if __name__ == '__main__':
    app.run(debug=True)