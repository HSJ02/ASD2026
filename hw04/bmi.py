from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>BMI 계산기</h1>
    <form action="/bmi">
        키(cm): <input type="text" name="height"><br><br>
        몸무게(kg): <input type="text" name="weight"><br><br>
        <input type="submit" value="계산">
    </form>
    """

@app.route('/bmi')
def bmi():
    height = float(request.args.get("height"))
    weight = float(request.args.get("weight"))

    height = height / 100
    bmi = weight / (height * height)

    if bmi < 18.5:
        result = "저체중"
    elif bmi < 23:
        result = "정상"
    elif bmi < 25:
        result = "과체중"
    else:
        result = "비만"

    return f"""
    <h1>BMI 결과</h1>
    키: {height * 100} cm <br>
    몸무게: {weight} kg <br>
    BMI: {round(bmi, 2)} <br>
    판정: {result} <br><br>
    <a href="/">다시하기</a>
    """

app.run()