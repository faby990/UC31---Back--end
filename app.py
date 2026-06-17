from flask import Flask, session, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = 'nao_conte_isso_a_ninguem_123'

@app.route('/contador')
def meu_contador():
    if 'acessos' not in session:
        session['acessos'] = 0
    
    session['acessos'] += 1
    return render_template('contador.html', acessos=session['acessos'])

@app.route('/contador/zerar', methods=['POST'])
def resetar_contador():
    session.pop('acessos', None)
    return redirect(url_for('meu_contador'))

if __name__ == '__main__':
    app.run(debug=True)