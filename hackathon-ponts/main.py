from flask import Flask
from utils import ask_question_to_pdf

app = Flask(__name__)

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
    message['answer']= ask_question_to_pdf.ask_question_to_pdf(data)
    return message

@app.route("/question", methods=["GET"])
def question():
    answer = ask_question_to_pdf.gpt3_completion("Pose moi une question sur le texte")
    return ({"answer": answer})
    # message = {}
    # message["answer"] = ask_question_to_pdf.gpt3_completion("Pose moi une question sur le texte")
    # return message

#def prompt():
    #message={}
    #message ['answer'] = request.form['prompt'] + " double mooooonstre"
    #return message
