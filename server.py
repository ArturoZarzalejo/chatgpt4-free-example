from flask import Flask, request, jsonify
from flask_cors import CORS
from gpt4free import forefront

app = Flask(__name__)
CORS(app)

@app.route('/ejemplo', methods=['POST'])
def ejemplo():
    token = forefront.Account.create(logging=False)
    data = request.get_json()
    texto = ""
    for response in forefront.StreamingCompletion.create(
        token=token,
        prompt=data['nombre'],
        model='gpt-4'
    ):
        texto += response.choices[0].text + "\n"

    respuesta = {'mensaje': texto}
    print(respuesta)

    return jsonify(respuesta)


if __name__ == '__main__':
    app.run()
