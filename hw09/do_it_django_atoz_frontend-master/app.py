from flask import Flask, request, render_template
import pandas as pd
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blog_list")
def blog_list():
    posts = [
        {"title": "제목 1", "content": "내용 1"},
        {"title": "제목 2", "content": "내용 2"},
        {"title": "제목 3", "content": "내용 3"}
    ]
    df = pd.read_csv("./blog_data2.csv", encoding="utf-8")

    print(df.head())
    posts = []
    for i, row in df.iterrows():
        posts.append({"title": row["title"], "content": row["content"]})
    return render_template("./blog_list2.html", posts=posts)

@app.route("/about")
def about():
    return render_template("./about_me.html")

if __name__ == "__main__":
    app.run(debug=True)