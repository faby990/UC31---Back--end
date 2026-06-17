from flask import Flask, render_template, session, redirect, url_for, request, flash
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave-autenticacao-flask'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'usuario' in session:
        return redirect(url_for('painel'))

    if request.method == 'POST':
        usuario_input = request.form.get('usuario', '').strip()
        senha_input = request.form.get('senha', '')

        if usuario_input == USUARIO_CORRETO and senha_input == SENHA_CORRETA:
            session['usuario'] = usuario_input
            session.permanent = True
            flash(f'Bem-vindo, {usuario_input}!', 'sucesso')
            return redirect(url_for('painel'))
        else:
            flash('Usuário ou senha incorretos. Tente novamente.', 'erro')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/painel')
def painel():
    if 'usuario' not in session:
        flash('Acesso negado! Por favor, faça login primeiro.', 'erro')
        return redirect(url_for('login'))
    
    return render_template('painel.html', usuario=session['usuario'])

@app.route('/logout')
def logout():
    session.clear()
    flash('Você saiu do sistema com sucesso!', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)