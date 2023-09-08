from flask import Flask
import ask_question_to_pdf

app = Flask(__name__)
q_list = []
r_list = []
@app.route("/hello/")
def hello_world():
    return "<p>Hello, World!</p>"

from flask import render_template

@app.route('/')
def hello():
    return render_template('index.html')


from flask import request
@app.route('/prompt', methods=['POST'])

def prompt():
    message = {}
    data = request.form['prompt']
    message['answer']= ask_question_to_pdf.gpt3_completion(data)
    return message

@app.route("/question", methods=["GET"])
def question():
    q = ask_question_to_pdf.ask_question_to_pdf("Pose moi une question au hasard sur le texte",ask_question_to_pdf.filename)
    q_list.append(q)
    return {"answer" : q}

@app.route("/answer", methods=["POST"])
def reponse():
    r = request.form["prompt"]
    answer = ask_question_to_pdf.verif(q_list[-1],r,ask_question_to_pdf.filename)
    return {"answer" : answer}

@app.route("/upload" , methods=["POST"])
def upload():
    f = request.files["background"]
    f.save("filename.pdf")
    return "file uploaded"
