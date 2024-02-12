from flask import Flask

app = Flask(__name__)

@app.route('/cadastro')
def get_my_code():
    with open("users.txt", "r") as arquivo:
        conteudo = arquivo.read()
    return conteudo

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
