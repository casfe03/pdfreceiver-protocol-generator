from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# Contador para gerar a sequência de protocolo
contador_protocolo = 1


@app.route('/upload', methods=['POST'])
def upload_file():
    global contador_protocolo  # referência ao contador global
    
    if 'file' not in request.files:
        return {"error": "Nenhum arquivo enviado"}, 400
    
    file = request.files['file']
    if file.filename == '':
        return {"error": "Arquivo sem nome"}, 400

    if not file or not file.filename.endswith('.pdf'):
        return {"error": "Formato de arquivo inválido. Apenas PDFs são permitidos"}, 400

    # Gerar o número de protocolo
    protocolo = f"TDFT2023{contador_protocolo:04d}"  # :04d garante que o número tenha sempre 4 dígitos, preenchendo com zeros à esquerda se necessário
    
    # Incrementar o contador de protocolo
    contador_protocolo += 1

    # Data atual
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    return {
        "mensagem": f"Recebemos seu pedido com sucesso no SEI.",
        "data_recebimento": data_atual,
        "protocolo": protocolo
    }, 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
