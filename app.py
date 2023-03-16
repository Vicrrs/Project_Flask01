from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def principal():
    nome = "Victor Roza"
    idade = 23
    return render_template('index.html', nome=nome, idade=idade)


@app.route("/sobre")
def sobre():
    return render_template('sobre.html')


if __name__ == "__main__":
    app.run(debug=True)
