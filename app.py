from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/introduction')
def introduction():
    return render_template('introduction.html')

@app.route('/theory')
def theory():
    return render_template('theory.html')

@app.route('/objective')
def objective():
    return render_template('objective.html')

@app.route('/experiment')
def experiment():
    return render_template('experiment.html')

@app.route('/quizzes')
def quizzes():
    return render_template('quizzes.html')

@app.route('/precedure')
def procedure():
    return render_template('procedure.html')

@app.route('/further')
def further():
    return render_template('further.html')

print(__name__)
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0') 