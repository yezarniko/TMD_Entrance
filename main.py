from flask import Flask, render_template, request
import json


with open('grade10_questions.json', 'r') as file:
    grade10_questions = json.load(file)


app = Flask("TMD_Entrance")

@app.route('/')
def home():
    return render_template('first.html')


@app.route('/entrance')
def entrance():
    return render_template('entrance.html')


@app.route('/grade10test/', methods=['GET', 'POST'])
def grade10_test():
    if request.method == 'GET':
        return render_template('g10test.html', questions=grade10_questions)
    elif request.method == 'POST':
        correct_answers = [q['correct_answer'] for q in grade10_questions] 
        return render_template('result.html', answers=request.form.items(),
                                correct_answers=correct_answers)


@app.route('/grade11test/', methods=['GET', 'POST'])
def grade11_test():
    if request.method == 'GET':
        return render_template('g11test.html')
    elif request.method == 'POST':
        pass


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'GET':
        return render_template('quiz.html')
    elif request.method == 'POST':
        pass


if __name__ == '__main__':
    app.run(debug=True)