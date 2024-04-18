import csv
import json
import os

from flask import Flask, render_template, request, jsonify

from megasena import MegasenaClass

app = Flask(__name__, template_folder='../frontend/templates')
app.config['UPLOAD_PATH'] = 'uploads'


@app.route('/')
def home():
    template_name = 'index.html'
    return render_template(template_name)


@app.route('/ocorrencias')
def ocorrencias():
    template_name = 'ocorrencias.html'
    megasena = MegasenaClass()
    ocorrencias = megasena.getOcorrencias()
    return render_template(template_name, len=len(ocorrencias), ocorrencias=ocorrencias)


@app.route('/volante')
def volante():
    template_name = 'cartela.html'
    return render_template(template_name)


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    template_name = 'upload.html'
    if request.method == 'GET':
        return render_template(template_name)
    if 'file' not in request.files:
        return "Nenhum arquivo CSV enviado", 400
    file = request.files['file']
    if file.filename == '':
        return "Nome de arquivo inválido", 400
    if file:
        dir_path = app.config['UPLOAD_PATH']
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file_path = os.path.join(dir_path, file.filename)
        file.save(file_path)
        numbers = ''
        with open(file_path, 'r') as _f:
            csv_file = csv.reader(_f, delimiter=";")
            for row in csv_file:
                numbers += row[0]
        megasena = MegasenaClass()
        resultados = megasena.conferir(numbers)
        if resultados[0] == 0:
            # só der erro apaga o arquivo
            os.remove(file_path)
        megasena.numerosMaisSorteados()
        return render_template(template_name, resultados=resultados)


@app.route('/conferir', methods=['POST'])
def conferir():
    numbers = json.loads(request.data)['numbers']
    megasena = MegasenaClass()
    resultado = megasena.conferir(numbers)
    response_data = {
        'result': resultado,
        'status': 'success'
    }
    return jsonify(response_data), 200


@app.route('/sugerir')
def sugerir():
    template_name = 'sugerir.html'
    megasena = MegasenaClass()
    resultados = megasena.getOcorrencias()[:30]
    return render_template(template_name, resultados=resultados)


@app.route('/sugerir-jogo')
def sugerirJogo():
    template_name = 'sugerir.html'
    megasena = MegasenaClass()
    resultados = megasena.getOcorrencias()[:30]
    megasena.numerosMaisSorteados()
    oitoNumerosEscolhidosAleatorios = megasena.sugerirJogo()
    resultadofinal = megasena.conferir(oitoNumerosEscolhidosAleatorios)
    return render_template(template_name, resultadofinal=resultadofinal, resultados=resultados)


if __name__ == '__main__':
    app.run(debug=True)
