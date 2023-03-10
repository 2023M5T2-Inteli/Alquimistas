from flask import Flask, render_template, redirect
import requests
from Dobot import Dobot

app = Flask(__name__)
port = 'http://10.128.64.164'

@app.route('/')
def index():
    return render_template('iniciate.html')

@app.route('/status')
def conection():
    return render_template('status.html')

@app.route('/routine')
def routine():
    arm = Dobot(225, 3, 140, 0)

    arm.moveHome()

    arm.pickToggle()
    arm.moveArmXY(189, 183, 151, 41)
    arm.drawLine(200, 183, -10, 41, -150)
    arm.moveArmXY(189, 183, 151, 41)
    arm.moveHome()
    arm.drawLine(302, 0, -10, 0, -100)
    arm.rotateTool(90)
    arm.moveHome()
    arm.moveArmXY(128, -195, 14, 0)
    # arm.pickToggle()

    return render_template('index.html')

@app.route('/on')
def control_on():
    try:
        requests.get('http://10.128.64.164/ON')
    except:
        return render_template('end.html')
    
@app.route('/off')
def control_off():
    try:
        requests.get('http://10.128.64.164/OFF')
    except:
        return render_template('iniciate.html')
    
@app.route('/stop')
def control_stop():
    try:
        requests.get('http://10.128.64.164/STOP')
    except:
        return 'Gambiarra STOP'

@app.route('/report')
def report():
    return render_template('report.html')


app.run(host = '0.0.0.0', port=3000, debug=True)