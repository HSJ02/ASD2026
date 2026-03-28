from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("gugudan.html")


@app.route("/gugudan")
def gugudan():
    dan = request.args.get("dan", 5)

    try:
        dan = int(dan)
    except:
        dan = 5

    results = []
    for x in range(1, 10):
        results.append(f"{dan} x {x} = {dan*x}")

    return render_template("result.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)