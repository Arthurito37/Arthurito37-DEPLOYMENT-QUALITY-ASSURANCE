from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Credenciais de exemplo (em uma aplicação real, essas informações seriam armazenadas de forma segura)
usuarios = {
    'usuario1': 'senha123',
    'usuario2': 'senha456'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']
        
        # Verifica as credenciais
        if usuario in usuarios and usuarios[usuario] == senha:
            return redirect(url_for('success'))
        else:
            return render_template('login.html', error='Nome de usuário ou senha incorretos.')

    return render_template('login.html')

@app.route('/success')
def success():
    return 'Login bem-sucedido!'

if __name__ == "__main__":
    app.run(debug=True)