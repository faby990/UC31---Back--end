from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    mensagem = ''

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        jogo = request.form.get('formaçao')

        if not nome:
            mensagem = "O campo nome é obrigatório!"

        elif not email:
            mensagem = "O campo e-mail é obrigatório!"

        elif not jogo:
            mensagem = "Selecione um jogo!"

        else:
            mensagem = f"""
            Cadastro realizado com sucesso!<br>
            Nome: {nome}<br>
            E-mail: {email}<br>
            Jogo escolhido: {jogo}
            """

    return render_template('ativi.cadastro.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)