from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'minha_chave_secreta'
socketio = SocketIO(app)

# Rota para renderizar a página principal (dispositivos móveis)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para renderizar a página de controle
@app.route('/controle')
def controle():
    return render_template('controle.html')

# Evento para quando um cliente cede a tela
@socketio.on('cedeTela')
def handle_cede_tela(json):
    print('Usuário cedeu a tela:', json)
    emit('feedback', {'data': 'Tela cedida com sucesso!'})

# Evento para alterar a cor da tela
@socketio.on('alterarCor')
def handle_alterar_cor(cor_data):
    print('Alterando cor para:', cor_data)
    emit('alterarCor', cor_data, broadcast=True)  # Envia para todos os conectados

# Evento para mostrar uma imagem
@socketio.on('mostrarImagem')
def handle_mostrar_imagem(img_data):
    print('Mostrando imagem:', img_data)
    emit('mostrarImagem', img_data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3000)
