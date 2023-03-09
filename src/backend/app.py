from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('iniciate.html')

@app.route('/status')
def conection():
    return render_template('status.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/end')
def end():
    return render_template('end.html')

app.run(host = '0.0.0.0', port=3000, debug=True)