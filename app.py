from flask import Flask, render_template, request, redirect
from models import Question, CBT

app = Flask(__name__)

cbt = CBT()

# Add sample questions
cbt.add_question(Question("Capital of Nigeria?", ["Abuja", "Lagos", "Kano"], "Abuja"))
cbt.add_question(Question("2 + 2 =", ["3", "4", "5"], "4"))
cbt.add_question(Question("Color of sky?", ["Blue", "Red", "Green"], "Blue"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        answers = []
        for i in range(len(cbt.questions)):
            answers.append(request.form.get(f"q{i}"))

        result = cbt.grade(answers)
        return redirect("/result")

    return render_template("quiz.html", questions=cbt.questions)


@app.route("/result")
def result():
    result = cbt.get_last_result()
    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)