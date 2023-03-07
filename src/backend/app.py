from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('iniciate.html')

@app.route('/status')
def conection():
    return render_template('status.html')

app.run(host = '0.0.0.0', port=3000, debug=True)