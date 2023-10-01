from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# Contador para gerar a sequência de protocolo
contador_protocolo = 1

@app.route('/upload', methods=['POST'])
def upload_file():
    global contador_protocolo  # referência ao contador global
    
    data = request.get_data()  # Obtem os dados binários brutos do corpo da requisição
    
    if not data:
        return {"error": "Nenhum dado enviado"}, 400

    # Gerar o número de protocolo
    protocolo = f"TDFT2023{contador_protocolo:04d}"  # :04d garante que o número tenha sempre 4 dígitos, preenchendo com zeros à esquerda se necessário
    
    # Incrementar o contador de protocolo
    contador_protocolo += 1
    
    # Você pode modificar isso para salvar com o nome que preferir, aqui estou usando o número de protocolo como nome do arquivo
    filename = f"{protocolo}.pdf"
    
    with open(filename, 'wb') as f:
        f.write(data)  # Escreve os dados binários no arquivo
    
    # Data atual
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    return {
        "mensagem": f"Recebemos seu pedido com sucesso no SEI.",
        "data_recebimento": data_atual,
        "protocolo": protocolo
    }, 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
