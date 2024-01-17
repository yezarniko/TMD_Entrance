from flask import Flask, render_template, request

app = Flask("TMD_Entrance")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/grade11/', methods=['GET', 'POST'])
def grade11():
    if request.method == 'GET':
        return render_template('grade11.html')
    elif request.method == 'POST':
        pass


@app.route('/grade12', methods=['GET', 'POST'])
def grade12():
    if request.method == 'GET':
        return render_template('grade12.html')
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