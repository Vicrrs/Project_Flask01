from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def principal():
    # Frutas = ["Uva", "Morango", "Laranja"]
    Frutas = []
    return render_template('index.html', Frutas=Frutas)


@app.route("/sobre")
def sobre():
    notas = {
        "Fulano":5.0,
        "Beltrano":6.0,
        "Aluno":7.0,
        "Sicrano":8.5
    }
    return render_template('sobre.html', notas=notas)


if __name__ == "__main__":
    app.run(debug=True)
