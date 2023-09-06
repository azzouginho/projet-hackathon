from flask import Flask
from utils import ask_question_to_pdf

app = Flask(__name__)
<<<<<<< HEAD


=======
q_list = []
r_list = []
>>>>>>> 8f4b4a1a72aeca8babcc961650fe6d31dd817656
@app.route("/hello/")
def hello_world():
    return "<p>Hello, World!</p>"


from flask import render_template


@app.route("/")
def hello():
    return render_template("index.html")


from flask import request


@app.route("/prompt", methods=["POST"])
def prompt():
    message = {}
    data = request.form["prompt"]
    message["answer"] = ask_question_to_pdf.gpt3_completion(data)
    return message


@app.route("/question", methods=["GET"])
def question():
    q = ask_question_to_pdf.ask_question_to_pdf("Pose moi une question sur le texte")
    q_list.append(q)
    return {"answer" : q}

@app.route("/answer", methods=["POST"])
def reponse():
    r = request.form["prompt"]
    answer = ask_question_to_pdf.verif(q_list[-1],r)
    return {"answer" : answer}


