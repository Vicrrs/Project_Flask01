from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def principal():
    frutas = []
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template('index.html', frutas=frutas)


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
